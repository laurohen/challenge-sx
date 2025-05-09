import asyncio
from fetch_urls import fetch_urls

async def main():
    urls = [
        "https://www.example.com",
        "https://www.python.org",
        "https://www.github.com"
    ]
    results = await fetch_urls(urls)
    for url, content in zip(urls, results):
        print(f"\nResultado para {url}:")
        print(content[:200] + "..." if len(content) > 200 else content)

if __name__ == "__main__":
    asyncio.run(main())