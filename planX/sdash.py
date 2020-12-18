import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go

df = px.data.tips()
default_fig = px.scatter(df, x="total_bill", y="tip", 
                         facet_col="sex", height=400)
default_fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("Figure Width"),
    dcc.Slider(id='width', min=200, max=500, step=25, value=300,
               marks={x: str(x) for x in [200, 300, 400, 500]}),
    dcc.Graph(id="graph", figure=default_fig),
])

@app.callback(
    Output("graph", "figure"), 
    [Input('width', 'value')], 
    [State("graph", "figure")])
def resize_figure(width, fig_json):
    fig = go.Figure(fig_json)
    fig.update_layout(width=int(width))

    return fig

app.run_server(debug=True)