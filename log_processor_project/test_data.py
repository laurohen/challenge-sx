from datetime import datetime, timedelta
import random

def generate_test_logs(num_logs=10000):
    """
    Gera uma lista de logs fictícios para teste.
    
    Args:
        num_logs (int): Número de logs a gerar.
    
    Returns:
        list: Lista de dicionários com chaves 'timestamp', 'level', 'message'.
    """
    levels = ['INFO', 'WARNING', 'ERROR', 'DEBUG']
    logs = []
    
    for i in range(num_logs):
        log = {
            'timestamp': datetime.now() - timedelta(seconds=random.randint(0, 3600)),
            'level': random.choice(levels),
            'message': f'System event {i}: {random.choice(["User login", "File processed", "Error detected", "Data updated"])}'
        }
        logs.append(log)
    
    return logs