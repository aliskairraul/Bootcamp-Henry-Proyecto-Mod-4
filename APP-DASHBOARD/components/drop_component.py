from dash import html, dcc


def returned_drop_component(options_drop: list) -> dcc.Dropdown:
    """Componente DropDown donde el usuario selecciona el periodo
       del cual desea ver la visualizacion

    Args:
        options_drop (list): Todos los periodos a elegir

    Returns:
        dcc.Dropdown: componente DropDpwn
    """
    drop_component = html.Div(
        [
            html.Label("Selecciona Periodo:", id="label-drop"),
            dcc.Dropdown(
                options=options_drop,
                value=options_drop[0],
                style={
                    "backgroundColor": "rgb(199, 253, 254)",
                    "fontSize": 14,
                    "color": "black",
                    "fontFamily": "Arial",
                },
                id="drop-down",
            ),
        ]
    )
    return drop_component
