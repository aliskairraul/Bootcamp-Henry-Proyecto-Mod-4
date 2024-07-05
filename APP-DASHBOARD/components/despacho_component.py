from screeninfo import get_monitors
from dash import html, dcc
import plotly.graph_objects as go

alto_monitor = get_monitors()[0].height
ancho_monitor = get_monitors()[0].width

# t=0, b=20, l=65, r=30
margen_botton = round(alto_monitor * 0.045)
margen_right = round(ancho_monitor * 0.01)
margen_left = round(ancho_monitor * 0.02)
alto = round(alto_monitor * 0.2)
font_size = round(alto_monitor * 0.011)
font_size2 = round(alto_monitor * 0.012)


def returned_despacho_component(
    kilometros: list, dias: list, montos: list, hover_inf: list
) -> html.Div:
    """Componente del Grafico de Burbujas Sobre Despachos

    Args:
        kilometros (list): Distancias de los Despachos
        dias (list): Dias de Entrega de los Despachos
        montos (list): Montos de los Despachos
        hover_inf (list): Informacion que se muestra al pasar el
                          mouse por la burbuja

    Returns:
        html.Div: Componente de Despachos
    """

    colorscale = [[0, "rgb(24, 67, 63)"], [1, "rgb(199, 253, 254)"]]
    fig = go.Figure()
    # Crear un gráfico de burbujas (scatter plot)
    fig.add_trace(
        go.Scatter(
            x=montos,
            y=kilometros,
            mode="markers",
            marker=dict(
                size=12,
                sizemode="diameter",
                sizeref=8,
                color=dias,
                colorscale=colorscale,
                opacity=0.7,
                showscale=True,
                colorbar_title="Dias",
            ),
            hovertext=hover_inf,
            hoverinfo="text",
        )
    )

    fig.update_xaxes(showgrid=False)  # Ocultamos la cuadrícula en el eje X
    fig.update_yaxes(showgrid=False)  # Ocultamos la cuadrícula en el eje Y

    fig.update_layout(
        # title="Demora en los Tiempos de Entrega de Los Pedidos",
        yaxis_title="Distancia (Mts)",
        # xaxis_title="Monto en Pesos ($)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="rgb(227, 227, 233)"),  # size=12
        margin=dict(t=0, b=0, l=0, r=0),  # t=0, b=20, l=65, r=30
        plot_bgcolor="rgba(0, 0, 0, 0)",
        # height=alto,  # 190
        annotations=[
            dict(
                text="Despachos - Periodo Seleccionado -- Eje X (Valor en Pesos $)",
                showarrow=False,
                xref="paper",
                yref="paper",
                x=0.80,
                y=1,
                align="right",
                font=dict(color="rgb(227, 227, 233)"),  # size=14
            )
        ],
    )

    despacho_mes = html.Div(
        [
            dcc.Graph(
                figure=fig,
                style={
                    "width": "74vw",
                    "height": "23vh",
                    "margin-left": "0.2em",
                    "margin-top": "0.4em",
                },
                config={"displayModeBar": False},
            ),
        ],
        id="despacho-mes",
    )
    return despacho_mes


"""
escalas de dolores
"Viridis"
"Cividis"
"Plasma"
"Inferno" 1
"Magma"
"Jet"
"Rainbow"
"""
