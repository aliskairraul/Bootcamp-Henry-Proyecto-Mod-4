from dash import html
import datetime

now = datetime.datetime.now(datetime.timezone.utc)
formatted_date = now.strftime("%B %d, %Y %H:%M (UTC)")

title_component = html.Div(
    [
        html.Div(html.Img(src="assets/henry.png"), id="image"),
        html.Div(
            html.Label("Proyecto Integrador Modulo IV Data-PT10 - Grupo 1"),
            id="central-title",
            className="text-title",
        ),
        html.Div(html.H3(formatted_date), id="date-title"),
    ],
    id="header-container",
)
