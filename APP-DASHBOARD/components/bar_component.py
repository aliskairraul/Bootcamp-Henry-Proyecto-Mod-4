from dash import html, dcc
import plotly.graph_objects as go
import pandas as pd

nombres = [
    "Cabildo",
    "Palermo-1",
    "Palermo-2",
    "Corrientes",
    "Almagro",
    "Caballito",
    "Flores",
    "Alberdi",
    "Deposito",
    "Velez",
    "Vicente Lopez",
    "San Isidro",
    "Caseros",
    "Moron",
    "Castelar",
    "San Justo",
    "Lanus",
    "Avellaneda",
    "Quilmes",
    "La Plata",
    "Mdq-1",
    "Mdq-2",
    "Rosario-1",
    "Rosario-2",
    "Córdoba Centro",
    "Córdoba Quiroz",
    "Cerro de las Rosas",
    "Tucumán",
    "Mendoza-1",
    "Mendoza-2",
    "Bariloche",
]


def returned_bar_component(sucursales: pd.DataFrame) -> html.Div:
    """Funcion que retorna el Componente del Grafico de Barras donde se
       aprecian las ventas acumuladas anuales por sucursal

    Args:
        sucursales (pd.DataFrame): DataFrame que contiene la Data de las Ventas y los
                                   id de las sucursales, de donde se alimenta el grafico
                                   barras

    Returns:
        html.Div: Componente que contiene el Grafico de Barras
    """
    global ids
    fig = go.Figure(
        data=[
            go.Bar(
                x=sucursales["id"],
                y=sucursales["venta"],
                text=nombres,
                marker_color="rgb(123, 255, 239)",
                hovertemplate=None,
                showlegend=False,
            ),
        ]
    )

    fig.update_xaxes(showgrid=False)  # Ocultamos la cuadrícula en el eje X
    fig.update_yaxes(showgrid=False)  # Ocultamos la cuadrícula en el eje Y

    fig.update_layout(
        # title_font=dict(size=1),
        # title="Ventas Anuales por Sucursal",
        xaxis_title="ID de Sucursal",
        yaxis_title="Venta Acumulada Anual",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="rgb(227, 227, 233)"),
        xaxis=dict(
            tickmode="linear",
            dtick=1,
            # tickfont=dict(size=font_tick_x)  # 12
        ),
        margin=dict(t=0, b=0, l=0, r=0),
        plot_bgcolor="rgba(0, 0, 0, 0)",
        showlegend=False,
    )

    bar_component = html.Div(
        [
            html.Label("Venta de Sucursales", id="bar-title"),
            dcc.Graph(
                figure=fig,
                style={
                    "width": "50vw",
                    "height": "40vh",
                    "margin-top": "0.5em",
                    "margin-left": "0.5em",
                },
                config={"displayModeBar": False},
            ),
        ],
        id="bar-container",
    )
    return bar_component
