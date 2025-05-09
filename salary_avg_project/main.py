import pandas as pd
from salary_avg import calculate_average_salary_above_30

def main():
    # Dados de exemplo
    data = {
        'id': [1, 2, 3, 4, 5],
        'nome': ['Alice', 'Bob', 'Carlos', 'Daniel', 'Eva'],
        'idade': [25, 30, 35, 40, 45],
        'salario': [5000, 7000, 8000, 10000, 12000]
    }
    df = pd.DataFrame(data)
    
    # Calcula a média salarial
    avg_salary = calculate_average_salary_above_30(df)
    print(f"Média salarial dos funcionários com idade > 30: {avg_salary}")

if __name__ == "__main__":
    main()