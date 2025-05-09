from bs4 import BeautifulSoup
from urllib.parse import urljoin
from response_helper import response
from helpers import cleaner, next_page_link

def scrape_website(url, website, content, visited=None, depth=1, max_depth=50) -> list:
    """
        Scrapea paginas web de forma recursiva hasta un maximo de max_depth.
        Se detiene si ya ha visitado la url o si el maximo de profundidad es alcanzado.
        Devuelve una lista de diccionarios con la url y el texto limpiado.
    """
    if visited is None:
        visited = set()

    normalized_url = url.split('#')[0]
    if normalized_url in visited or depth > max_depth:
        return content

    visited.add(normalized_url)
    html = response(url)
    if html is None:
        return content

    soup = BeautifulSoup(html, 'html.parser')

    cleaned = cleaner(soup, website)
    if cleaned:
        print(f"Contenido limpiado de {url}")
        content.append({"url": url, "text": cleaned})
    
    next_href = next_page_link(soup, website)
    if next_href:
        next_url = urljoin(url, next_href)
        return scrape_website(next_url, website, content, visited, depth + 1, max_depth)
    else:
        print(f"[{website}] No hay más páginas")
        return content