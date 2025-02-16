import os
import pandas as pd

# Função para carregar dados
def load_data(dados_sensores_5000_parquet):
    file_path = os.path.join(os.getcwd(), dados_sensores_5000_parquet)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")
    return pd.read_parquet(file_path, engine='fastparquet')

# Função para detectar outliers
def detect_outliers(df):
    metrics = ['Energia (kWh)', 'Água (m3)', 'CO2 Emissões']
    outliers_dict = {}

    for metric in metrics:
        df[f'{metric}_zscore'] = (df[metric] - df[metric].mean()) / df[metric].std()
        outliers = df[abs(df[f'{metric}_zscore']) > 3]
        outliers_dict[metric] = outliers[['Empresa', 'Setor', metric]]

    return outliers_dict

# Função para calcular insights
def calculate_insights(df):
    insights = {}
    insights['total_empresas'] = df['Empresa'].nunique()
    insights['total_setores'] = df['Setor'].nunique()
    insights['media_energia'] = df['Energia (kWh)'].mean()
    insights['media_agua'] = df['Água (m3)'].mean()
    insights['media_co2'] = df['CO2 Emissões'].mean()
    return insights