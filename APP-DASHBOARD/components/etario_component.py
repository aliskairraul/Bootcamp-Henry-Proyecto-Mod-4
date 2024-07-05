from dash import html, dcc
import plotly.graph_objects as go


def returned_etario_component(labels: list, values: list) -> html.Div:
    """
    Función que retorna un componente con el gráfico de barras horizontales
    que muestra la información de las ventas por rango de edades acumuladas
    durante el año en estudio.

    Args:
        labels (list): distintos rangos de edades
        values (list): Valores de las ventas acumuladas

    Returns:
        html.Div: Componente con el gráfico
    """
    fig = go.Figure(
        data=[
            go.Bar(
                y=labels,
                x=values,
                orientation="h",
                marker_color="rgb(123, 255, 239)",
                width=0.4,
                hovertemplate=None,
            )
        ]
    )

    fig.update_traces(
        texttemplate="%{x:.0f}", textposition="inside", insidetextanchor="start"
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    fig.update_layout(
        # title="Ventas Por Rango Etario",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="rgb(227, 227, 233)"),
        margin=dict(t=0, b=0, l=0, r=0),
        xaxis_title="Ventas Acumuladas",
        yaxis_title="Rango -- Edades",
    )

    etario_anio = html.Div(
        [
            dcc.Graph(
                figure=fig,
                style={
                    "width": "20vw",
                    "height": "28vh",
                    "margin-top": "0.8em",
                    "margin-left": "0.5em",
                },
                config={"displayModeBar": False},
            ),
        ],
        id="etario-mes",
    )
    return etario_anio
