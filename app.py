import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from student import Student
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "wide-form" data frame with no index
# see https://plotly.com/python/wide-form/ for more options

student = Student(1)
student.get_scores()

fig1 = student.line_graph()
fig2 = student.bar_graph()


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig1
    ),

    
    dcc.Graph(
        id='example-graph2',
        figure=fig2
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)
