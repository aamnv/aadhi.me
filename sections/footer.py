import dash_html_components as html


layout = html.Footer([
    html.Hr(className='my-1'),
    html.Small([
        'Made by ',
        html.A(
            'Aadhi Manivannan',
            href='https://www.linkedin.com/in/aadhimnv',
            target='_blank',
            style={'textDecoration': 'underline'}
        )
    ],
    className='text-muted')
], style={'padding': '1rem'})