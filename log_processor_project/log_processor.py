import psycopg2
from psycopg2.extras import execute_batch
from datetime import datetime

def process_log(logs, batch_size=1000):
    """
    Processa uma lista de logs e insere no banco de dados PostgreSQL em lotes.
    
    Args:
        logs (list): Lista de dicionários com chaves 'timestamp', 'level', 'message'.
        batch_size (int): Tamanho do lote para inserção em lote.
    
    Returns:
        bool: True se a inserção for bem-sucedida, False caso contrário.
    """
    try:
        # Conexão com o banco usando context manager
        with psycopg2.connect(
            dbname="test",
            user="postgres",
            password="secret",
            host="localhost"
        ) as conn:
            with conn.cursor() as cursor:
                # Prepara os dados para inserção em lote
                values = [
                    (log['timestamp'], log['level'], log['message'])
                    for log in logs
                ]
                
                # Insere em lotes usando execute_batch
                execute_batch(
                    cursor,
                    "INSERT INTO logs (timestamp, level, message) VALUES (%s, %s, %s)",
                    values,
                    page_size=batch_size
                )
                
            # Commit da transação
            conn.commit()
            return True
            
    except psycopg2.Error as e:
        print(f"Erro ao processar logs: {e}")
        return False

# Exemplo de uso
if __name__ == "__main__":
    # Logs fictícios para teste
    sample_logs = [
        {
            'timestamp': datetime.now(),
            'level': 'INFO',
            'message': f'Log message {i}'
        }
        for i in range(1000)
    ]
    
    # Processa os logs
    success = process_log(sample_logs)
    print("Processamento concluído com sucesso!" if success else "Falha no processamento.")