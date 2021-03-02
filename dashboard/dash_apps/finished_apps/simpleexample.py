import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.graph_objs as go
import pandas as pd

from django_plotly_dash import DjangoDash

url = 'https://raw.githubusercontent.com/lucasdmarten/dadoEURUSD/main/Tab_v01_EURUSD_lucro%20(1).csv'
data = pd.read_csv(url)
data['date'] = data.iloc[:, 0]
ret = data['retorno_acumu'].values[:-10]
dat = data['date'].values[:-10]
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Gain money simulator'),
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
