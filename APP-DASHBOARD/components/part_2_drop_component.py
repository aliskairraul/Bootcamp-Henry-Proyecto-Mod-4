from dash import html


def returned_part2_drop_component(
    empleado: str,
    empleado_ven: str,
    empleado_per: float,
    sucursal_mes: str,
    sucursal_mes_ven: str,
    sucursal_mes_per: float,
    dia: str,
    dia_ven: str,
    dia_per: float,
) -> html.Div:
    """Funcion que gestiona el Componente que esta Justo debajo del Dropdown
       donde el usuario selecciona el periodo que desea visualizar

    Args:
        empleado (str): empleado destacado del mes
        empleado_ven (str): monto en ventas del empleado
        empleado_per (float): porcentaje con respecto al total
        sucursal_mes (str): sucursal destacada en el mes
        sucursal_mes_ven (str): venta en el periodo seleccionado
        sucursal_mes_per (float): porcentaje respecto al total
        dia (str): dia de la semana que mas a tenido ventas en el año
        dia_ven (str): venta de ese dia especifico durante el año
        dia_per (float): porcentaje respecto al total

    Returns:
        html.Div: Componente con la informacion antes descrita
    """
    part_2_drop = html.Div(
        [
            html.Div(
                [
                    html.Br(),
                    html.Label(
                        "Empleado destacado del Mes", className="first-big-titles"
                    ),
                    html.Br(),
                    html.Label(f"{empleado}", className="first-big-names"),
                    html.Br(),
                    html.Label(
                        f"{empleado_ven}  --  {empleado_per} %  ",
                        className="first-big-numbers",
                    ),
                    html.Br(),
                    html.Br(),
                ],
                id="empleado",
                className="empleado-sucursal-dia",
            ),
            html.Div(
                [
                    html.Br(),
                    html.Label(
                        "Sucursal destacada en el Mes", className="first-big-titles"
                    ),
                    html.Br(),
                    html.Label(f"{sucursal_mes}", className="first-big-names"),
                    html.Br(),
                    html.Label(
                        f"{sucursal_mes_ven}  --   {sucursal_mes_per} %",
                        className="first-big-numbers",
                    ),
                    html.Br(),
                    html.Br(),
                ],
                id="sucursal-mes",
                className="empleado-sucursal-dia",
            ),
            html.Div(
                [
                    html.Br(),
                    html.Label(
                        "Dia con mas Ventas en el Año",
                        className="first-big-titles",
                    ),
                    html.Br(),
                    html.Label(f"{dia}", className="first-big-names"),
                    html.Br(),
                    html.Label(
                        f"{dia_ven}   --  {dia_per} %  ",
                        className="first-big-numbers",
                    ),
                    # html.Label(f"{dia_per} %", className="first-big-percentages"),
                ],
                id="dia",
                className="empleado-sucursal-dia",
            ),
        ],
        id="first-big-content",
    )
    return part_2_drop
