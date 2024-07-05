from dash import html


def returned_compras_component(accumulated_purchases: str) -> html.Div:
    """Funcion que retorna el componente que muestra las compras acumuladas
       en lo que va del año

    Args:
        accumulated_purchases (str): compras acumuladas

    Returns:
        html.Div: componente con la compra anual acumulada
    """
    compras_component = html.Div(
        [
            html.Label(
                "Compra Anual",
                id="purchases-annual",
                className="small-title",
            ),
            html.Br(),
            html.Br(),
            html.Label(
                f"{accumulated_purchases}  $",
                id="purchase-number",
                className="small-numbers-out",
            ),
        ]
    )
    return compras_component
