from dash import html


def returned_irregularidad_component(perdida: str, margen: str) -> html.Div:
    """Funcion que retorna el componente con los datos de la Perdida por
       el factor 42917 y cual sería el margen sin este

    Args:
        perdida (str): perdida por el factor 42917
        margen (str): margen de no existeir el 42917

    Returns:
        html.Div: componente con los valores descritos
    """

    irregularidad_component = html.Div(
        [
            html.Br(),
            html.Label(
                perdida,
                id="perdida-42917",
                className="irregularidad",
            ),
            html.Br(),
            html.Br(),
            html.Label(
                margen,
                id="margen-42917",
                className="irregularidad",
            ),
        ]
    )
    return irregularidad_component
