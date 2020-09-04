import dash_bootstrap_components as dbc
import dash_html_components as html


def prog_section():
    layout = dbc.Card([
        dbc.CardBody([
            html.H3('Programming', id='programming', className='card-title'),
            html.Hr(className='my-1'),
            dbc.CardDeck([
                dbc.Card([
                    html.H5('fred-cli', className='card-title'),
                    html.Hr(className='my-1'),
                    html.A(
                        dbc.CardImg(
                            src='/assets/fredcli.svg', 
                            style={
                                'height': '10rem', 'width': '100%', 'margin-top': '0.5rem',
                                'box-shadow': '1rem 1rem 0.5rem #ccc'
                            }
                        )
                    , href='https://github.com/aamnv/fred-cli', target='_blank'),
                ], style={'border': 'none', 'margin-top': '0.5rem'}),
                dbc.Card([
                    html.H5('XLpup', className='card-title'),
                    html.Hr(className='my-1'),
                    html.A(
                        dbc.CardImg(
                            src='/assets/xlpup.png', 
                            style={
                                'height': '10rem', 'width': '100%', 'margin-top': '0.5rem',
                                'box-shadow': '1rem 1rem 0.5rem #ccc'
                            }
                        )
                    , href='https://github.com/aamnv/fred-cli', target='_blank'),
                ], style={'border': 'none', 'margin-top': '0.5rem'}),
                dbc.Card([
                    html.H5('aadhi.me', className='card-title'),
                    html.Hr(className='my-1'),
                    html.A(
                        dbc.CardImg(
                            src='/assets/fredcli.svg', 
                            style={
                                'height': '10rem', 'width': '100%', 'margin-top': '0.5rem',
                                'box-shadow': '1rem 1rem 0.5rem #ccc'
                            }
                        )
                    , href='https://github.com/aamnv/fred-cli', target='_blank'),
                ], style={'border': 'none', 'margin-top': '0.5rem'})
            ])
        ])
    ], style={'border': 'none', 'width': '100%'})

    return layout