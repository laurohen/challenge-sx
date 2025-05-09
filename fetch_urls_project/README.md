# Fetch URLs Project

Este projeto implementa uma função assíncrona que faz requisições HTTP para múltiplas URLs em paralelo e retorna os conteúdos das páginas utilizando as bibliotecas `asyncio` e `aiohttp` em Python.

## Pré-requisitos

- Python 3.8 ou superior
- Biblioteca `aiohttp`
- Conexão à internet para realizar as requisições HTTP

## Instalação

1. Clone ou baixe este projeto para o seu computador.
2. Navegue até a pasta do projeto:

   ```bash
   cd fetch_urls_project
   ```

3. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

4. Instale as dependências listadas em `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Como Executar

1. Execute o arquivo `main.py` com o comando:

   ```bash
   python main.py
   ```

2. A saída mostrará o conteúdo (ou erros) das requisições para as URLs especificadas, limitado a 200 caracteres por URL. Exemplo de saída parcial:

   ```plaintext
   Resultado para https://www.example.com:
   <!doctype html><html><head><title>Example Domain</title>...

   Resultado para https://www.python.org:
   <!doctype html><!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]...

   Resultado para https://www.github.com:
   <!DOCTYPE html><html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark">...
   ```

## Estrutura do Projeto

- `fetch_urls.py`: Contém as funções `fetch_url` e `fetch_urls` para requisições HTTP.
- `main.py`: Ponto de entrada do projeto, contém um exemplo de uso com três URLs.
- `requirements.txt`: Lista a dependência `aiohttp`.
- `README.md`: Este arquivo com instruções.

## Detalhes da Implementação

- A função `fetch_url` realiza uma requisição HTTP para uma única URL.
- A função `fetch_urls` executa requisições para múltiplas URLs em paralelo usando `asyncio.gather`.
- O `main.py` define uma lista de URLs e exibe os resultados das requisições.
- Erros de conexão ou respostas com status diferente de 200 são capturados e retornados como mensagens.

Para dúvidas ou sugestões, entre em contato!