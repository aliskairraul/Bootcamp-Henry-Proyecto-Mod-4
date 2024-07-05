from dash import html, dcc
import plotly.graph_objects as go


def returned_canales_component(values: list) -> html.Div:
    """
    Función que retorna un componente con el gráfico de donut personalizado.

    Args:
        values (list): Valores de las ventas acumuladas
                       de los distintos canales

    Returns:
        html.Div: Componente con el gráfico
    """
    # Colores específicos para cada canal
    colors = {
        "Presencial": "rgb(123, 253, 255)",
        "Telefonico": "rgb(67, 139, 130)",
        "On Line": "rgb(42, 87, 83)",
    }
    labels = ["On Line", "Telefonico", "Presencial"]
    # Crear el gráfico de donut
    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.4,
                marker=dict(colors=[colors[label] for label in labels]),
                textposition="outside",
            )
        ]
    )

    fig.update_traces(
        textfont=dict(color="rgb(227, 227, 233)"),  # size=13
        hoverinfo="label+percent",
    )

    fig.update_layout(
        title="Ventas Por Canal",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="rgb(227, 227, 233)"),  # size=13
        margin=dict(t=0, b=0, l=0, r=0),
        legend=dict(x=1.5, y=1.1),
    )

    canales_component = html.Div(
        [
            dcc.Graph(
                figure=fig,
                style={"width": "21vw", "height": "33vh", "margin-left": "0.5em"},
                config={"displayModeBar": False},
            ),
        ],
        id="etario-mes",
    )
    return canales_component
