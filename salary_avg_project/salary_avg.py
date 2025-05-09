import pandas as pd

def calculate_average_salary_above_30(df: pd.DataFrame) -> float:
    """
    Calcula a média salarial dos funcionários com idade superior a 30 anos.
    
    Args:
        df (pd.DataFrame): DataFrame com colunas 'idade' e 'salario'.
    
    Returns:
        float: Média salarial dos funcionários com idade > 30.
    """
    filtered_df = df[df['idade'] > 30]
    return filtered_df['salario'].mean()