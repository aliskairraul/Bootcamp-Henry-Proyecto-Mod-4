from dash import html


def returned_gasto_component(accumulated_expense: str) -> html.Div:
    """Funcion que retorna el componente que Muestra el Gasto acumulado anual

    Args:
        accumulated_expense (str): Gasto acumulado durante lo que va del año

    Returns:
        html.Div: Componente del Gasto Acumulad Anual
    """
    gastos_component = html.Div(
        [
            html.Label("Gasto Anual", id="expense-annual", className="small-title"),
            html.Br(),
            html.Br(),
            html.Label(
                f"{accumulated_expense}  $",
                id="expense-number",
                className="small-numbers-out",
            ),
        ]
    )
    return gastos_component
