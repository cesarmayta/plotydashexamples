import dash
from dash import dcc, html
import plotly.express as px
import seaborn as sns
import pandas as pd

# Cargar dataset de Seaborn
df = sns.load_dataset("penguins")

# Inicializar la aplicación Dash
app = dash.Dash(__name__,serve_locally=False)


app.layout = html.Div([
    html.H1("Mi primer dashboard de Pingüinos"),
    
    html.Div([
        dcc.Graph(figure=px.scatter(df, x="bill_length_mm", y="bill_depth_mm", color="species"))
    ])
])


if __name__ == "__main__":
    app.run_server(debug=False,port=8055)
