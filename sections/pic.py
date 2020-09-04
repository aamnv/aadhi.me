import dash_bootstrap_components as dbc
import dash_html_components as html


def pic_section():
    layout = dbc.Card([
        html.H1('Aadhi Manivannan', className='card-title'),
        dbc.CardImg(
            src='/assets/aadhi_pic.png', bottom=True,
            style={'border-radius': '50%', 'height': 'auto', 'width': '25%'}
        ),
    ], style={'border': 'none', 'align-items': 'center'})


    return layout