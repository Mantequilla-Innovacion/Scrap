import re


def cleaner(soup, website) -> str:
    """
        Limpia el HTML y extrae texto con buena legibilidad.
        Elimina scripts, estilos, sidebars, etc. y conserva encabezados y texto útil.
    """
    main_selectors = {
        "pandas": lambda s: s.find("main"),
        "fastapi": lambda s: s.select_one(".md-container"),
        "pytorch": lambda s: s.find(class_="pytorch-container"),
        "geeksforgeeks": lambda s: s.find("article"),
        "nodejs": lambda s: s.find("div", id="content")
    }

    main_content = main_selectors[website](soup)

    for tag in main_content(["script", "style", "noscript"]):
        tag.decompose()

    bricks = []

    for elem in main_content.descendants:
        if elem.name in ["h1", "h2", "h3"]:
            text = elem.get_text(" ", strip=True).upper()
        elif elem.name in ["p", "li", "pre"]:
            text = elem.get_text(" ", strip=True)
        else:
            continue

        if text:
            text = re.sub(r"\s+", " ", text).strip()
            bricks.append(text)

    return "\n\n".join(bricks)


def next_page_link(soup, website) -> str:
    """
        Devuelve el enlace a la siguiente página de un sitio web específico.
        Si no hay más páginas, devuelve None.
    """
    selectors = {
        "pandas": lambda s: s.find("a", class_="right-next"),
        "fastapi": lambda s: s.select_one("a.md-footer__link--next"),
        "pytorch": lambda s: s.find("a", rel="next"),
        "geeksforgeeks": lambda s: s.find("a", class_="pg-head"),
        "nodejs": lambda s: (
            s.find("a", class_="active")
            .find_parent("li")
            .find_next_sibling("li")
            .find("a")
        )
    }

    if website in selectors:
        tag = selectors[website](soup)
        return tag['href'] if tag and 'href' in tag.attrs else None

    return None