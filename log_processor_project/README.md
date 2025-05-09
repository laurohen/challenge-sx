# Log Processor Project

Este projeto otimiza o processamento de logs em tempo real, inserindo logs em um banco de dados PostgreSQL de forma eficiente utilizando inserções em lote com `psycopg2`. Inclui uma configuração Docker para facilitar testes e uma massa de dados de teste.

## Pré-requisitos

- Python 3.8 ou superior
- Docker e Docker Compose instalados
- Biblioteca `psycopg2-binary` (instalada via Docker ou manualmente)

## Configuração do Ambiente com Docker

1. Clone ou baixe este projeto para o seu computador.
2. Navegue até a pasta do projeto:

   ```bash
   cd log_processor_project
   ```

3. Suba o banco de dados PostgreSQL e a aplicação com Docker Compose:

   ```bash
   docker-compose up --build
   ```

4. A saída mostrará o processamento de 10.000 logs fictícios, algo como:

   ```plaintext
   Gerados 10000 logs para processamento.
   Processamento concluído com sucesso!
   ```

5. Para verificar os dados inseridos no banco:

   ```bash
   docker exec -it log_processor_project_db_1 psql -U postgres -d test -c "SELECT * FROM logs LIMIT 5;"
   ```

6. Para parar os serviços:

   ```bash
   docker-compose down
   ```

## Configuração Manual (Sem Docker)

### Configuração do Banco de Dados

1. Instale o PostgreSQL, se ainda não estiver instalado.
2. Crie um banco de dados chamado `test`:

   ```bash
   createdb test
   ```

3. Crie a tabela `logs` no banco `test`:

   ```sql
   psql -d test -c "CREATE TABLE logs (
       id SERIAL PRIMARY KEY,
       timestamp TIMESTAMP NOT NULL,
       level VARCHAR(50) NOT NULL,
       message TEXT NOT NULL
   );"
   ```

4. Verifique se o usuário `postgres` com senha `secret` tem acesso ao banco. Ajuste as variáveis de ambiente no `docker-compose.yml` ou no ambiente local se necessário.

### Instalação

1. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

2. Instale as dependências listadas em `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

### Como Executar

1. Certifique-se de que o PostgreSQL está em execução e o banco `test` está configurado.
2. Execute o arquivo `main.py` para processar a massa de dados de teste:

   ```bash
   python main.py
   ```

3. A saída esperada será:

   ```plaintext
   Gerados 10000 logs para processamento.
   Processamento concluído com sucesso!
   ```

4. Verifique os dados inseridos no banco:

   ```bash
   psql -d test -c "SELECT * FROM logs LIMIT 5;"
   ```

## Estrutura do Projeto

- `log_processor.py`: Contém a função `process_log` otimizada.
- `main.py`: Ponto de entrada do projeto, chama `process_log` com a massa de dados de teste.
- `test_data.py`: Gera 10.000 logs fictícios para teste.
- `requirements.txt`: Lista a dependência `psycopg2-binary`.
- `Dockerfile`: Configura a imagem da aplicação Python.
- `docker-compose.yml`: Configura o PostgreSQL e a aplicação.
- `init.sql`: Script SQL para criar a tabela `logs`.
- `README.md`: Este arquivo com instruções.

## Detalhes da Implementação

- **Inserção em Lote**: Usa `psycopg2.extras.execute_batch` para inserir logs em lotes, reduzindo chamadas ao banco.
- **Context Managers**: Utiliza `with` para gerenciar conexões e cursores, garantindo fechamento correto.
- **Conexão Única**: Mantém uma única conexão ao banco para todo o processamento.
- **Massa de Dados**: `test_data.py` gera 10.000 logs com timestamps variados, níveis (INFO, WARNING, ERROR, DEBUG) e mensagens realistas.
- **Docker**: O `docker-compose.yml` configura um banco PostgreSQL e a aplicação, com inicialização automática da tabela `logs`.
- **Variáveis de Ambiente**: O `main.py` usa variáveis de ambiente para configurar a conexão com o banco, compatível com Docker.

## Notas

- No Docker, o `DB_HOST` é definido como `db` (nome do serviço no `docker-compose.yml`). Para execução manual, ajuste para `localhost` ou o host apropriado.
- O `batch_size` padrão (1000) pode ser ajustado em `main.py` para otimizar o desempenho.
- Para logs muito grandes, considere usar o comando `COPY` do PostgreSQL (não implementado aqui, mas pode ser adicionado).
- Os dados de teste são gerados em `test_data.py`. Modifique a função `generate_test_logs` para personalizar os logs.

Para dúvidas ou sugestões, entre em contato!