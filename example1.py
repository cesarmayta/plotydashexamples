import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Cargar dataset de penguins
df = px.data.penguins()

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Layout de la aplicación
app.layout = html.Div([
    html.H1("Dashboard de Pingüinos"),
    html.P("Selecciona una especie:"),
    dcc.Dropdown(
        id="dropdown_especie",
        options=[{"label": especie, "value": especie} for especie in df["species"].unique()],
        value="Adelie",
        clearable=False
    ),
    dcc.Graph(id="grafico_dispersion")
])

# Callback para actualizar el gráfico
@app.callback(
    Output("grafico_dispersion", "figure"),
    Input("dropdown_especie", "value")
)
def actualizar_grafico(especie):
    df_filtrado = df[df["species"] == especie]
    fig = px.scatter(df_filtrado, x="bill_length_mm", y="bill_depth_mm", color="sex",
                     title=f"Longitud vs Profundidad del Pico ({especie})")
    return fig

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run_server(debug=True)
