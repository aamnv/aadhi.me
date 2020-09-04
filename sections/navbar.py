import dash_bootstrap_components as dbc
import dash_html_components as html

layout = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink(html.A("About Me", href="#about", ))),
        dbc.NavItem(dbc.NavLink(html.A("Programming", href="#programming"))),
        dbc.NavItem(dbc.NavLink(html.A("Investing", href="#investing"))),
    ],
    brand="aadhi.me",
    brand_href="#",
    color="light",
    light=False,
    dark=False,
    fluid=True,
    sticky='top',
    style={'margin-bottom': '1rem', 'border': 'none', 'border-bottom': 'solid'}
)