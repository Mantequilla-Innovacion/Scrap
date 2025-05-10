import os
from dotenv import load_dotenv
from scraper import scrape_website


load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT")


if __name__ == "__main__":

    if ENVIRONMENT == "dev":
        website = input("¿Qué web quieres scrappear? (pandas, fastapi, pytorch) \n").strip().lower()
        start_url = input(f"¿Url de {website}? \n").strip()
        try:
            max_depth = int(input("¿Cuántas páginas quieres scrappear? (50 por defecto) \n") or 50)
        except ValueError:
            max_depth = 49

        content = []
        result = scrape_website(start_url, website, content, max_depth=max_depth)

        if not os.path.exists(f"scrapper/{website}"):
            os.makedirs(f"scrapper/{website}")

        for i, entry in enumerate(result):
            with open(os.path.join(f"scrapper/{website}", f"pagina_{i+1}.txt"), "w", encoding="utf-8") as f:
                f.write(entry["text"] + "\n\n" + entry["url"])

    elif ENVIRONMENT == "prod":
        import uvicorn
        uvicorn.run("API:app", host="127.0.0.1", port=8000, reload=True)