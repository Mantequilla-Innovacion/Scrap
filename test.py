import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error {response.status_code} al acceder a {url}")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')
    next_link = next_page_link(soup, "nodejs")
    if next_link:
        print(f"Enlace a la siguiente página: {next_link}")
    else:
        print("No hay más páginas disponibles.")
    # ul = soup.find('div', id='column2')
    # active_a = ul.find("a", class_="active")
    # print("Actual:", active_a['href'])

    # # Sube al <li> contenedor
    # li_tag = active_a.find_parent("li")

    # # Encuentra el siguiente <li>
    # next_li = li_tag.find_next_sibling("li")
    
    # if next_li:
    #     next_a = next_li.find("a")
    #     if next_a:
    #         print("Siguiente:", next_a['href'])
    #     else:
    #         print("No se encontró <a> en el siguiente <li>")
    # else:
    #     print("No hay siguiente <li>")



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

scrape_website("https://nodejs.org/docs/latest-v23.x/api/debugger.html")
