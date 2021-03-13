import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.graph_objs as go
import pandas as pd

from django_plotly_dash import DjangoDash

from django.contrib.staticfiles.storage import staticfiles_storage
directorio = staticfiles_storage.location + '/dados/dado.csv'
data = pd.read_csv(directorio)
data['date'] = data.iloc[:, 0]
ret = data['retorno_acumu'].tolist()
dat = data['date'].tolist()
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Example'),
    dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color':'#ffffff'}),
    dcc.Slider(
        id='slider-updatemode',
        marks={i:'{}'.format(i) for i in range(20)},
        max=20,
        value=2,
        step=1,
        updatemode='drag',
    ),
])

@app.callback(
    Output('slider-graph', 'figure'),
    [Input('slider-updatemode', 'value')]
    )



def display_value(value):

    graph = go.Bar(
        x=dat,
        y=ret,
        name='Manipulate Graph'
    )
    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',

        font=dict(color='white'),
    )
    return {'data':[graph], 'layout':layout}
