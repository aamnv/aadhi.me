import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

from sections import navbar
from sections import footer
from sections import pic
from sections import bio
from sections import prog
from sections import stocks

server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        layout = dbc.Container(fluid=True, children=[
            navbar.layout,
            dbc.Container(fluid=False, children=[
                dbc.Row(pic.pic_section()),
                dbc.Row(bio.bio_section()),
                dbc.Row(prog.prog_section()),
                dbc.Row(stocks.invest_section()),
            ], style={'max-width': '50em'}),
            footer.layout
        ])

        return layout

    else:
        return '404'

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)