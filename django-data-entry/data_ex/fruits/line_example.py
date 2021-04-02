import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

from django_plotly_dash import DjangoDash


external_stylesheet = ['https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css']

app = DjangoDash('LineExample', external_stylesheets=external_stylesheet)   # replace dash.Dash

df = pd.read_csv('fruits/assets/historical.csv')

x = df['DATE'].to_list()
y = df['PRICE'].to_list()

fig = px.line(df, x, y)


colors = {
    'background': 'black',
    'paper': 'black',
    'text': 'navajowhite'
}

fig.update_layout(
    plot_bgcolor=colors['background'], # background
    paper_bgcolor=colors['paper'],     # graph area
    font_color=colors['text']          # text
)

app.layout = html.Div([
    dcc.Graph(
        id='graph-1',
        figure=fig
    )
])


# app.layout = html.Div([
#     dcc.RadioItems(
#         id='dropdown-color',
#         options=[{'label': c, 'value': c.lower()} for c in ['Red', 'Green', 'Blue']],
#         value='red'
#     ),
#     html.Div(id='output-color'),
#     dcc.RadioItems(
#         id='dropdown-size',
#         options=[{'label': i,
#                 'value':j} for i, j in [('L', 'Large'), ('M', 'Medium'), ('S', 'Small')]],
#         value='Medium'
#     ),
#     html.Div(id='output-size')

# ])

# @app.callback(
#     dash.dependencies.Output('output-color', 'children'),
#     [dash.dependencies.Input('dropdown-color', 'value')]
# )
# def callback_color(dropdown_value):
#     return "The selected color is %s." %dropdown_value

# @app.callback(
#     dash.dependencies.Output('output-size', 'children'),
#     [dash.dependencies.Input('dropdown-color', 'value'),
#     dash.dependencies.Input('dropdown-size', 'value')]
# )
# def callback_size(dropdown_color, dropdown_size):
#     return "The chosen T-Shirt is a %s %s one." %(dropdown_size, dropdown_color)