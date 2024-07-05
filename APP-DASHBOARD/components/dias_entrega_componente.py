from dash import html


def returned_dias_component(dias_entrega_str: str) -> html.Div:
    """Funcion que retorna el componente que muestra los dias de entrega
       del periodo seleccionado

    Args:
        dias_entrega_str (str): Metrica de los dias promedio del periodo
                                seleccionado

    Returns:
        html.Div: componente con los dias promedio del periodo
    """
    dias_entrega_component = html.Div(
        [
            html.Label(
                "Dias de Entrega",
                id="prom-dias-entrega",
                className="small-title",
            ),
            html.Br(),
            html.Br(),
            html.Label(
                f"{dias_entrega_str} ",
                id="dias-number",
                className="small-numbers-out",
            ),
        ]
    )
    return dias_entrega_component
