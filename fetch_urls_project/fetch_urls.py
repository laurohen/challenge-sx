import asyncio
import aiohttp

async def fetch_url(session, url: str) -> str:
    """
    Faz uma requisição HTTP para uma URL e retorna o conteúdo.
    
    Args:
        session: Sessão aiohttp.ClientSession.
        url (str): URL a ser acessada.
    
    Returns:
        str: Conteúdo da página ou mensagem de erro.
    """
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            return f"Erro ao acessar {url}: Status {response.status}"
    except Exception as e:
        return f"Erro ao acessar {url}: {str(e)}"

async def fetch_urls(urls: list) -> list:
    """
    Faz requisições HTTP para múltiplas URLs em paralelo.
    
    Args:
        urls (list): Lista de URLs.
    
    Returns:
        list: Lista com os conteúdos das páginas ou mensagens de erro.
    """
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)