from dash import html


def returned_margen_component(accumulated_margin: str) -> html.Div:
    """Funcion que retorna el componente que muestra como va el margen en el
       Anual acumulado

    Args:
        accumulated_margin (str): margen del acumulado anual

    Returns:
        html.Div: componente del margen anual acumulado
    """
    margen_component = html.Div(
        [
            html.Label(
                "Margen Anual",
                id="margin-annual",
                className="small-title",
            ),
            html.Br(),
            html.Br(),
            html.Label(
                f"{accumulated_margin}  %",
                id="margin-number",
                className="small-numbers-out",
            ),
        ]
    )
    return margen_component
