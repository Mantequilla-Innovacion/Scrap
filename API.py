from fastapi import FastAPI, Query
from scraper import scrape_website
from enum import Enum


app = FastAPI()

class Website(str, Enum):
    pandas = "pandas"
    fastapi = "fastapi"
    pytorch = "pytorch"

@app.get("/scrape")
def scrape(
        website: Website = Query(..., description="Nombre del sitio web"),
        url: str = Query(..., description="URL inicial para scrapear"),
        max_depth: int = Query(50, description="Profundidad máxima de scraping")
    ) -> dict:
    """
        Endpoint para iniciar el scraping de una URL.\n
        Devuelve un diccionario con la información scrappeada.
    """
    content = []
    result = scrape_website(url, website, content, max_depth=max_depth)

    return {"scrapped info": result}
