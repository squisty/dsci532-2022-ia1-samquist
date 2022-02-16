import altair as alt
from dash import Dash, dcc, html, Input, Output
from vega_datasets import data

app = Dash(__name__)
server = app.server

bar = data.barley()

def plot_altair(variety):
    chart = alt.Chart(bar[bar['variety'] < variety]).mark_point().encode(
        x='site',
        y='yield',
        tooltip='variety').interactive()
    return chart.to_html()

app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div([
        dcc.Dropdown(
            id='variety', value='variety',
            options=[{'label': i, 'value': i} for i in bar['variety'].unique()]),
        html.Iframe(
            id='scatter',
            style={'border-width': '0', 'width': '100%', 'height': '400px'},
            srcDoc=plot_altair(variety='Manchuria'))])
        
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('variety', 'value'))
def update_output(xmax):
    return plot_altair(xmax)

if __name__ == '__main__':
    app.run_server(debug=True)