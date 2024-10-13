from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('./data/output.csv')
app = Dash()

app.layout = [
    html.H1(children='Pink Morsel Sales', style={'textAlign':'center'}),
    dcc.RadioItems(
        list(df.Region.unique()) + ['all'], 
        df.Region.unique()[0], 
        id='region-selection',
        style={'display': 'flex', 'justifyContent': 'center'}
        ),
    dcc.Graph(id='graph-content')
]


@callback(
    Output('graph-content', 'figure'),
    Input("region-selection", "value"),
)
def update_graph(region):
    if region == 'all':
        dff = df
    else:
        dff = df[df.Region==region]
    fig = px.line(dff, x='Date', y='Sales')
    fig.update_traces(line_color='#F23127')
    return fig


if __name__ == '__main__':
    app.run(debug=True)
