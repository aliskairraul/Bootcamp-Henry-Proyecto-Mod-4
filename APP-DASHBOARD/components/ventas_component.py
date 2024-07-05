from dash import html


def returned_sales_component(accumulated_sales: str) -> html.Div:
    """Funcion que retorna la el componente donde se muestra las ventas totales
       acumuladas durante el año.

    Args:
        accumulated_sales (str): Ventas acumuladas en el año

    Returns:
        html.Div: Componente con la informacion de las ventas
                  acumuladas durante el año
    """
    ventas_component = html.Div(
        [
            html.Label(
                "Venta Anual",
                id="sales-annual",
                className="small-title",
            ),
            html.Br(),
            html.Br(),
            html.Label(
                f"{accumulated_sales}  $",
                id="purchase-number",
                className="small-numbers-out",
            ),
        ],
        id="third-small-container",
    )
    return ventas_component
