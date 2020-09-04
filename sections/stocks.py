import dash_bootstrap_components as dbc
import dash_html_components as html


def invest_section():
    layout = dbc.Card([
        dbc.CardBody([
            html.H3('Investing', id='investing', className='card-title'),
            html.Hr(className='my-1'),
            dbc.CardDeck([
                dbc.Card([
                    html.H5('Weyerhaeuser', className='card-title'),
                    html.Hr(className='my-1'),
                    html.P(
                        'REITs, Timberlands, and oh so much more.',
                        className='card-text', style={'margin-top': '0.5rem'}
                    ),
                    html.A('Read more', href='https://www.aadhi.rocks/posts/weyerhaeuser-mar-2020/', target='_blank'),
                    html.P('Mar 22, 2020', className='text-muted'),
                ], style={'border': 'none', 'margin-top': '0.5rem'}),
                dbc.Card([
                    html.H5('Materion', className='card-title'),
                    html.Hr(className='my-1'),
                    html.P(
                        'Government monopolies are pretty weird.', 
                        className='card-text', style={'margin-top': '0.5rem'}
                    ),
                    html.A('Read more', href='https://www.aadhi.rocks/posts/materion-mar-2020/', target='_blank'),
                    html.P('Apr 7, 2020', className='text-muted'),
                ], style={'border': 'none', 'margin-top': '0.5rem'}),
                dbc.Card([
                    html.H5('Whirlpool', className='card-title'),
                    html.Hr(className='my-1'),
                    html.P(
                        "People won't stop doing laundry. Right? Right?",
                        className='card-text', style={'margin-top': '0.5rem'}
                    ),
                    html.A('Read more', href='https://www.aadhi.rocks/posts/whirlpool-mar-2020/', target='_blank'),
                    html.P('Mar 27, 2020', className='text-muted'),
                ], style={'border': 'none', 'margin-top': '0.5rem'})
            ])
        ])
    ], style={'border': 'none', 'width': '100%'})

    return layout