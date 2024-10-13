from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('./data/output.csv')
app = Dash()

app.layout = [
    html.H1(children='Pink Morsel Sales', style={'textAlign':'center'}),
    dcc.Dropdown(df.Region.unique(), 'north', id='region-selection'),
    dcc.Graph(id='graph-content')
]


@callback(
    Output('graph-content', 'figure'),
    Input("region-selection", "value"),
)
def update_graph(region):
    dff = df[df.Region==region]
    fig = px.line(dff, x='Date', y='Sales')
    return fig


if __name__ == '__main__':
    app.run(debug=True)
