from dash import Dash, html, Input, Output, callback
import pandas as pd
import numpy as np
import locale

from components.title_component import title_component
from components.drop_component import returned_drop_component
from components.gastos_component import returned_gasto_component
from components.compras_component import returned_compras_component
from components.ventas_component import returned_sales_component
from components.margen_component import returned_margen_component
from components.dias_entrega_componente import returned_dias_component
from components.bar_component import returned_bar_component
from components.despacho_component import returned_despacho_component
from components.etario_component import returned_etario_component
from components.canales_component import returned_canales_component
from components.part_2_drop_component import returned_part2_drop_component
from components.irregularidad_component import returned_irregularidad_component


locale.setlocale(locale.LC_ALL, "es_VE.utf8")

options_drop: list

# CARGA DE DATA CSV
tablero = pd.read_csv("data/tablero.csv")
historico = pd.read_csv("data/historico.csv")
despacho = pd.read_csv("data/despacho.csv")
venta_edad = pd.read_csv("data/venta_edad.csv")

tablero = tablero.fillna(0)
options_drop = list(tablero.iloc[:, 1])

for i in range(len(venta_edad)):
    venta_edad.loc[i, "Rango"] = venta_edad.iloc[i, 0][2:]

# perdida = tablero.loc[mask, "perdida_42917"].astype(int).iloc[0]

sucursales = pd.DataFrame()
indices = np.arange(1, 32)
sucursales["id"] = indices
sucursales["venta"] = 0

app = Dash(suppress_callback_exceptions=True)

server = app.server

app.layout = html.Div(
    [
        html.Div([title_component], id="title-container"),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [returned_drop_component(options_drop)],
                                    id="part_1_drop",
                                ),
                                html.Div([], id="part_2_drop"),
                            ],
                            id="drop_container",
                        )
                    ],
                    id="work_1_1_container",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [], id="indicator-days", className="indicators"
                                ),
                                html.Div(
                                    [], id="indicator-expenses", className="indicators"
                                ),
                                html.Div(
                                    [], id="indicator-purchases", className="indicators"
                                ),
                                html.Div(
                                    [], id="indicator-sales", className="indicators"
                                ),
                                html.Div(
                                    [], id="indicator-margin", className="indicators"
                                ),
                            ],
                            id="work_1_2_1_container",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [html.Div([], id="bar_container")],
                                    id="work_1_2_2_1_container",
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Div(
                                                    [], id="irregularidad_container"
                                                )
                                            ],
                                            id="work_1_2_2_2_1_container",
                                        ),
                                        html.Div(
                                            [html.Div([], id="etario_container")],
                                            id="work_1_2_2_2_2_container",
                                        ),
                                    ],
                                    id="work_1_2_2_2_container",
                                ),
                            ],
                            id="work_1_2_2_container",
                        ),
                    ],
                    id="work_1_2_container",
                ),
            ],
            id="work_1_container",
        ),
        html.Div(
            [
                html.Div(
                    [html.Div([], id="despachos_container")], id="work_2_1_container"
                ),
                html.Div(
                    [html.Div([], id="canales_container")], id="work_2_2_container"
                ),
            ],
            id="work_2_container",
        ),
    ],
    id="general-container",
)


@callback(Output("part_2_drop", "children"), Input("drop-down", "value"))
def handle_return_first_big_component(value: str) -> html.Div:
    """Funcion que gestiona el callback que retorna el componente que muestra
       la informacion que esta debajo del Dropdown

    Args:
        value (str): periodo seleccionado por el usuario

    Returns:
        html.Div: componente con la informacion debajo del Dropdown
    """
    global tablero
    mask = tablero["periodo"] == value
    empleado = tablero.loc[mask, "empleado_mes"].iloc[0]
    empleado_ven = tablero.loc[mask, "empleado_mes_venta"].iloc[0]
    empleado_ven_for = locale.format_string("%d", empleado_ven, grouping=True)
    empleado_per = round(float(tablero.loc[mask, "empleado_mes_porcentaje"].iloc[0]), 2)

    sucursal = tablero.loc[mask, "sucursal_mes"].iloc[0]
    sucursal_ven = tablero.loc[mask, "sucursal_mes_venta"].iloc[0]
    sucursal_ven_for = locale.format_string("%d", sucursal_ven, grouping=True)
    sucursal_per = round(float(tablero.loc[mask, "sucursal_mes_porcentaje"].iloc[0]), 2)

    dia = tablero.loc[mask, "dia_anio"].iloc[0]
    dia_ven = tablero.loc[mask, "dia_anio_venta"].iloc[0]
    dia_ven_for = locale.format_string("%d", dia_ven, grouping=True)
    dia_per = round(float(tablero.loc[mask, "dia_anio_porcentaje"].iloc[0]), 2)

    component = returned_part2_drop_component(
        empleado=empleado,
        empleado_ven=empleado_ven_for,
        empleado_per=empleado_per,
        sucursal_mes=sucursal,
        sucursal_mes_ven=sucursal_ven_for,
        sucursal_mes_per=sucursal_per,
        dia=dia,
        dia_ven=dia_ven_for,
        dia_per=dia_per,
    )
    return component


@callback(Output("indicator-expenses", "children"), Input("drop-down", "value"))
def handle_return_gastos_component(value: str) -> html.Div:
    """Funcion que gestiona el Callback que incorpora el componente que muestra
       el gasto anual acumulado


    Args:
        value (str): Periodo Seleccionado por el Usuario

    Returns:
        html.Div: Componente con el promedio de Dias de entrega
    """
    global tablero
    mask = tablero["periodo"] == value
    gasto_anual = tablero.loc[mask, "gastos"].astype(int).iloc[0]
    gasto_anual_formateado = locale.format_string("%d", gasto_anual, grouping=True)
    component = returned_gasto_component(accumulated_expense=gasto_anual_formateado)
    return component


@callback(Output("indicator-days", "children"), Input("drop-down", "value"))
def handle_return__dias_component(value: str) -> html.Div:
    """Funcion que gestiona el Callback que incorpora el componente que muestra
       el promedio de los dias entrega del mes seleccionado

    Args:
        value (str): Periodo Seleccionado por el Usuario

    Returns:
        html.Div: Componente con el Gasto anual acumulado
    """
    global tablero
    mask = tablero["periodo"] == value
    dias_entrega = tablero.loc[mask, "dias_entrega"].astype(float).iloc[0]
    dias_entrega = round(dias_entrega, 2)
    component = returned_dias_component(dias_entrega_str=dias_entrega)
    return component


@callback(Output("indicator-purchases", "children"), Input("drop-down", "value"))
def handle_return_compras_component(value: str) -> html.Div:
    """Funcion que retorna el callback que retorna las compras anuales acumuladas

    Args:
        value (str): Periodo elegido por el Usuario

    Returns:
        html.Div: Componente con las compras acumuladas anuales
    """
    global tablero
    mask = tablero["periodo"] == value
    compra_anual = tablero.loc[mask, "compras"].astype(int).iloc[0]
    compra_anual_formateado = locale.format_string("%d", compra_anual, grouping=True)

    component = returned_compras_component(
        accumulated_purchases=compra_anual_formateado
    )
    return component


@callback(Output("indicator-sales", "children"), Input("drop-down", "value"))
def handle_return_ventas_component(value: str) -> html.Div:
    """Funcion que gestiona el Callback que retorna el componente con la
       informacion de Ventas acumuladas durante el año

    Args:
        value (str): Periodo Seleccionado por el Usuario

    Returns:
        html.Div: Componente con la informacion de Ventas y ventas_outliers
                  acumuladas durante el año
    """
    global tablero
    mask = tablero["periodo"] == value
    venta_anual = tablero.loc[mask, "ventas"].astype(int).iloc[0]
    venta_anual_formateado = locale.format_string("%d", venta_anual, grouping=True)
    component = returned_sales_component(accumulated_sales=venta_anual_formateado)
    return component


@callback(Output("indicator-margin", "children"), Input("drop-down", "value"))
def handle_return_fourt_small_component(value: str) -> html.Div:
    """Funcion que gestiona el callback que retorna el componente que muestra
       el margen anual

    Args:
        value (str): Periodo seleccionado por el usuario

    Returns:
        html.Div: componente con la informacion del margen anual acumulado
    """
    global tablero
    mask = tablero["periodo"] == value
    compra_anual = tablero.loc[mask, "compras"].astype(int).iloc[0]
    gastos_anual = tablero.loc[mask, "gastos"].astype(int).iloc[0]
    venta_anual = tablero.loc[mask, "ventas"].astype(int).iloc[0]

    margin_str = str(round(100 * (1 - (compra_anual + gastos_anual) / venta_anual), 2))
    # margin_str_sin_42917 = str(
    #     round(100 * (1 - (compra_anual + gastos_anual - perdida) / venta_anual), 2)
    # )
    # if perdida > 0:
    #     mensaje_margen_sin_42917 = "Margen sin 42917 ---->" + margin_str_sin_42917 + "%"
    # else:
    #     mensaje_margen_sin_42917 = ""
    component = returned_margen_component(accumulated_margin=margin_str)
    return component


@callback(Output("bar_container", "children"), Input("drop-down", "value"))
def handle_return_bar_component(value: str) -> html.Div:
    """Funcion que gestiona el callback que devuelve el grafico de barras de las
       ventas acumuladas anuales de las sucursales

    Args:
        value (str): periodo seleccionado por el usuario

    Returns:
        html.Div: componente con el grafico de barras
    """
    global tablero
    global historico
    global sucursales
    # Creo nuevos DataFrame para Trabajar
    historico_filtrado = pd.DataFrame()
    mask = tablero["periodo"] == value
    # localizo el año
    anio_search = tablero.loc[mask, "anio"].unique()[0]
    # localizo el mes
    mes_search = tablero.loc[mask, "mes"].unique()[0]

    mask = historico["anio"] == anio_search
    # Creo la copia con el historico ya filtrado por año
    historico_filtrado = historico[mask]

    # Creo la mascara segun el mes a buscar

    sucursales["venta"] = 0
    for i in range(len(sucursales)):
        mask_2 = (historico_filtrado["mes"] <= mes_search) & (
            historico_filtrado["id_sucursal"] == sucursales.iloc[i, 0]
        )
        sucursales.iloc[i, 1] = historico_filtrado[mask_2]["venta"].sum()

    component = returned_bar_component(sucursales=sucursales)
    return component


@callback(Output("despachos_container", "children"), Input("drop-down", "value"))
def handle_return_despacho_component(value: str) -> html.Div:
    """Funcion que retorna el callback que devuelve el componente del grafico de burbujas
       que representan los despachos del periodo seleccionado

    Args:
        value (str): periodo seleccionado por el usuario

    Returns:
        html.Div: Componente que contiene el grafico de burbujas
    """
    global tablero
    global despacho
    mask = tablero["periodo"] == value
    # localizo el año
    anio_search = tablero.loc[mask, "anio"].unique()[0]
    # localizo el mes
    mes_search = tablero.loc[mask, "mes"].unique()[0]
    mask = (
        (despacho["Anio"] == anio_search)
        & (despacho["Mes"] == mes_search)
        & (despacho["Venta"] <= 10000)
        & (despacho["Distancia"] <= 2000)
    )
    desp_filtrado = despacho[mask].copy()
    kilometros = list(desp_filtrado["Distancia"])
    montos = list(desp_filtrado["Venta"])
    dias = list(desp_filtrado["TiempoEntrega"])
    hover_inf = list(desp_filtrado["HoverInf"])
    component = returned_despacho_component(
        kilometros=kilometros, dias=dias, montos=montos, hover_inf=hover_inf
    )
    return component


@callback(Output("etario_container", "children"), Input("drop-down", "value"))
def handle_return_etario_anio_component(value: str) -> html.Div:
    """Funcion que gestiona el callback que retorna el grafico de las
       ventas por rango etario acumuladas en el año

    Args:
        value (str): periodo seleccionado

    Returns:
        html.Div: componente con el grafico tipo pie
    """
    global tablero
    global venta_edad
    rangos = [
        "Hasta 30 años",
        "De 31 a 40 años",
        "De 41 a 50 años",
        "De 51 a 60 años",
        "Desde 61 años",
    ]
    labels = [
        "Hasta 30 ",
        "31 a 40 ",
        "41 a 50 ",
        "51 a 60 ",
        "Desde 61 ",
    ]
    mask = tablero["periodo"] == value
    # localizo el año
    anio_search = tablero.loc[mask, "anio"].unique()[0]
    # localizo el mes
    mes_search = tablero.loc[mask, "mes"].unique()[0]
    values = []
    for rango in rangos:
        mask = (
            (venta_edad["Anio"] == anio_search)
            & (venta_edad["Mes"] <= mes_search)
            & (venta_edad["Rango"] == rango)
        )
        values.append(venta_edad.loc[mask, "Venta"].sum())
    component = returned_etario_component(labels=labels, values=values)
    return component


@callback(Output("canales_container", "children"), Input("drop-down", "value"))
def handle_return_second_big_component(value: str) -> html.Div:
    """Funcion que gestiona el callback que devuelve el componente con el
       grafico tipo Dount que muestra la proporcion de ventas por canal de
       Distribucion

    Args:
        value (str): periodo seleccionado por el usuario

    Returns:
        html.Div: Componente que contiene el grafico tipo donut
    """
    global tablero
    mask = tablero["periodo"] == value

    online = round(float(tablero.loc[mask, "online_anio"].iloc[0]), 2)
    presencial = round(float(tablero.loc[mask, "presencial_anio"].iloc[0]), 2)
    telefono = round(float(tablero.loc[mask, "telefono_anio"].iloc[0]), 2)
    values = [online, telefono, presencial]
    component = returned_canales_component(values=values)
    return component


@callback(Output("irregularidad_container", "children"), Input("drop-down", "value"))
def handle_return_irregularidad_component(value: str) -> html.Div:
    """Funcion que gestiona el callback que devuelve el componente con los
       valores de la Perdida por el factor 42917 y cual sería el margen de la
       cadena sin este factor

    Args:
        value (str): periodo seleccionado por el usuario

    Returns:
        html.Div: Componente que contiene el Valor de la Perdida a causa del factor 42917
                  y cuanto seria el Margen de la cadena sin ese factor
    """

    global tablero
    mask = tablero["periodo"] == value
    compras = tablero.loc[mask, "compras"].iloc[0]
    gastos = tablero.loc[mask, "gastos"].iloc[0]
    ventas = tablero.loc[mask, "ventas"].iloc[0]
    perdida = tablero.loc[mask, "perdida_42917"].astype(int).iloc[0]

    perdida_formateada = locale.format_string("%d", perdida, grouping=True)

    margen = str(round(100 * (1 - (compras + gastos - perdida) / ventas), 2))
    if perdida > 0:
        mensaje_perdida_42917 = "Factor ID (42917) ----> " + perdida_formateada + " $"
        mensaje_margen_sin_42917 = "Margen sin ID (42917) ----> " + margen + " %"
        component = returned_irregularidad_component(
            margen=mensaje_margen_sin_42917, perdida=mensaje_perdida_42917
        )
        return component
    return None


if __name__ == "__main__":
    app.run_server(debug=False)
