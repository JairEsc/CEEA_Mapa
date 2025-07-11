import dash
import dash_bootstrap_components as dbc  # Importa Dash Bootstrap Components
from dash import html, dcc, callback, Input, Output
from app import anios_nh
dash.register_page(
    __name__,
    path='/not_home',
    title='Otro titulo',
    name='Otro nombre'
)
slider_periodo_nh = dcc.Slider(
    id="slider_periodo_nh",
    step=None,
    marks=anios_nh,
    value=list(anios_nh.keys())[-1],
    className="slider-custom-R"
)
encabezado_nh =  dbc.Row([
        dbc.Col(
            html.H2("Indicadores de Calidad del Agua", style={'color': 'white', 'margin':'0', 'padding': '2vh 0 0 10px'}), # paddin arriba, derecha abajo izquierda
            width = 7,
            xxl = 7, xl = 7, lg = 7, md = 7, sm = 12,  xs = 12, 
            style = {'backgroundColor': '#9C2448', 'padding': '0','margin':'0'} 
        ),
        dbc.Col(
            #html.H2("Barra", style={'color': 'white', 'margin':'0', 'padding': '0'}),
            html.A(
                html.Img(src="./assets/Imagenes/Planeacion_dorado.png", style={'width': '100%', 'height': '70%', 'padding': '1vh 0 0 10px'}),
                href = "https://sigeh.hidalgo.gob.mx/", 
                target= "_blank"
            ),
            width = 3,
            xxl = 3, xl = 3, lg = 3, md = 3, sm = 7,  xs = 7, 
            style = {'backgroundColor': '#9C2448', 'padding': '0', 'margin':'0'}
        ),
        dbc.Col(
            html.A(
                html.Img(src="./assets/Imagenes/CEAA_dorado.png", style={'width': '75%', 'height': '75%', 'padding': '1vh 0 0 10px'}),
                href = "https://ceaa.hidalgo.gob.mx/",
                target= "_blank" 
            ),
            width = 2,
            xxl = 2, xl = 2, lg = 2, md = 2, sm = 5,  xs = 5, 
            style = {'backgroundColor': '#9C2448', 'padding': '0', 'margin':'0'}
        )
    ], 
    style={"height": "12vh", 'width': '100vw' , 'padding':'0', 'margin':'0'}
    )


enmedio_nh = dbc.Row([
    dbc.Col(
        children= slider_periodo_nh,
        width = 12,
        xxl = 12, xl = 12, lg = 12, md = 12, sm = 12,  xs = 12, 
        style = {'backgroundColor': '#BC955B', 'padding': '0','margin':'0'} 
    )
],
    style={"height": "8vh", 'width': '100vw' , 'padding':'0', 'margin':'0'}
)
mapa_nh = dbc.Row(
    dbc.Col(
        html.Iframe(src= "", 
                    id="mapa_nh",
                    style={'width': '100vw', 'height': '79vh', 'border': '0', 'padding': '0', 'margin': '0'}),
        width = 12,
        xxl = 12, xl = 12, lg = 12, md = 12, sm = 12,  xs = 12, 
        style = {'backgroundColor': '#9C2448', 'padding': '0','margin':'0'} 
    ),
    style={"height": "80vh", 'width': '100vw' , 'padding':'0', 'margin':'0'}
)



layout = html.Div([
    html.Button('Go to Home', id='navigate-button2'),
    dcc.Location(id='url2', refresh=True),
    encabezado_nh,
    enmedio_nh,
    mapa_nh,
]
)
