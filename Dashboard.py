import dash
from dash import dcc, html
import plotly.express as px
from data_processing import load_data, detect_outliers

# Carregar o ficheiro Parquet
df = load_data('dados_sensores_5000.parquet')

# Detectar outliers
outliers_dict = detect_outliers(df)

# Inicializar o app Dash
app = dash.Dash(__name__)

# Layout do dashboard
app.layout = html.Div([
    html.H1("Dashboard de Outliers"),
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label=metric, children=[
            dcc.Graph(
                figure=px.scatter(outliers, x='Empresa', y=metric, color='Setor', title=f'Outliers em {metric}')
            )
        ]) for metric, outliers in outliers_dict.items()
    ])
])

# Executar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)