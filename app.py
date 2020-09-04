import dash
import dash_bootstrap_components as dbc


app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.LITERA],
    title="aadhi.me | Aadhi's Portfolio",
    assets_folder='assets/'
)

server = app.server