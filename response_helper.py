import requests

def response(url) -> str:
    """
        Realiza una solicitud HTTP GET a la URL proporcionada y devuelve el contenido HTML.
        Si la solicitud falla, imprime un mensaje de error y devuelve None.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content
        else:
            return None
    except Exception as e:
        return(f"Error de conexión con {url}: {e}")