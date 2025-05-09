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
    print(soup.prettify())

scrape_website("https://docs.pytorch.org/docs/stable/index.html")
