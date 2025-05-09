# Salary Average Project

Este projeto implementa uma função que calcula a média salarial de funcionários com idade superior a 30 anos utilizando a biblioteca `pandas` em Python.

## Pré-requisitos

- Python 3.8 ou superior
- Biblioteca `pandas`

## Instalação

1. Clone ou baixe este projeto para o seu computador.
2. Navegue até a pasta do projeto:

   ```bash
   cd salary_avg_project
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

2. A saída esperada será:

   ```plaintext
   Média salarial dos funcionários com idade > 30: 10000.0
   ```

## Estrutura do Projeto

- `salary_avg.py`: Contém a função `calculate_average_salary_above_30`.
- `main.py`: Ponto de entrada do projeto, contém um exemplo de uso com um DataFrame.
- `requirements.txt`: Lista a dependência `pandas`.
- `README.md`: Este arquivo com instruções.

## Detalhes da Implementação

- A função `calculate_average_salary_above_30` filtra o DataFrame para incluir apenas funcionários com idade superior a 30 anos e calcula a média da coluna `salario`.
- O `main.py` cria um DataFrame de exemplo e chama a função para demonstrar o cálculo.

Para dúvidas ou sugestões, entre em contato!