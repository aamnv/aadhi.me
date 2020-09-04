import dash_bootstrap_components as dbc
import dash_html_components as html


def bio_section():
    layout = dbc.Card([
        dbc.CardBody([
            html.H3('About Me', id='about', className='card-title'),
            html.Hr(className='my-1'),
            html.P(
                "Hi there! My name is Aadhi and I'm an MBA student at the "
                "Tuck School of Business at Dartmouth. In my free time I enjoy "
                "exploring beautiful ol' New Hampshire, but I also like to "
                "program, invest, and build stuff."
            , className='card-text', style={'margin-top': '0.5rem'}),
            html.P([
                "That's why I made this page. ",
                html.A("My LinkedIn", href="https://www.linkedin.com/in/aadhimnv/", target='_blank'),
                " speaks to my work experience. But this page is a portfolio of my "
                "'work product'. Hopefully you enjoy and if you have any questions / "
                "comments - ",
                html.A("feel free to reach out.", href="mailto:aadithyan.manivannan@gmail.com", target='_blank')
            ], className='card-text'),
        ])
    ], style={'border': 'none', 'width': '100%'})

    return layout