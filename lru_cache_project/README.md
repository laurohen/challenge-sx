# LRU Cache Project

Este projeto implementa uma estrutura de dados **LRU Cache** (Least Recently Used) utilizando `OrderedDict` do módulo `collections` em Python. A cache suporta operações de leitura (`get`) e escrita (`put`) com uma capacidade fixa.

## Pré-requisitos

- Python 3.8 ou superior
- Nenhum pacote externo é necessário, pois o projeto utiliza apenas a biblioteca padrão do Python.

## Instalação

1. Clone ou baixe este projeto para o seu computador.
2. Navegue até a pasta do projeto:

   ```bash
   cd lru_cache_project
   ```

## Como Executar

1. Execute o arquivo `main.py` com o comando:

   ```bash
   python main.py
   ```

2. A saída esperada será:

   ```plaintext
   1
   -1
   -1
   3
   4
   ```

## Estrutura do Projeto

- `lru_cache.py`: Contém a implementação da classe `LRUCache`.
- `main.py`: Ponto de entrada do projeto, contém um exemplo de uso da classe `LRUCache`.
- `requirements.txt`: Lista de dependências (vazio, pois não há dependências externas).
- `README.md`: Este arquivo com instruções.

## Detalhes da Implementação

- A classe `LRUCache` utiliza `OrderedDict` para manter a ordem de acesso aos itens.
- O método `get` retorna o valor de uma chave e move a chave para o final (mais recente).
- O método `put` adiciona ou atualiza um par chave-valor, removendo o item menos recente se a capacidade for excedida.
- O `main.py` demonstra o uso da cache com uma sequência de operações.

Para dúvidas ou sugestões, entre em contato!