import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from student import Student
from query_data_sqlite import class_list
from dash.dependencies import Input, Output

'''
Script that creates a development server to host browser-based app that displays
a dashboard of student fluency statistics and graphics.

When program is run in a terminal, a server will be created and you can view the
running app at a location displayed in the termainal (usually 127.0.0.1:8050)
'''


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def generate_table(dataframe, max_rows=30):
    '''
    Function that returns an html table when given a dataframe

    assumes you have a "wide-form" data frame with no index
    see https://plotly.com/python/wide-form/ for more options
    '''
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

class_list = [{'label': s[1]+' '+ s[2], 'value': s[0]} for s in class_list(1)]

# Visual layout of app
app.layout = html.Div(children=[
    html.H1(children='Teacher Interface',
        style={
            'textAlign': 'center'
        }
    ),

    html.Div(children='''
        A dashboard for teachers to see comprehensive summaries of students' fluency scores.
    ''', 
        style={
            'textAlign': 'center'
        }

    ),




    dcc.Dropdown(
        id='student-selector',
        options=class_list,
        value= 1
    ),

    html.Div(children=[

        html.Div(
            id='score_table',
            style={'width': '19%', 'float': 'left'}  
        ),

        html.Div(children=[

            dcc.Graph(
                id='bar-graph'
            ),

            
            dcc.Graph(
                id='line-graph'
            ),
        ],style={'width': '79%', 'float': 'right'})
        
    ])

])

# Callback and function that updates charts and table when different student is selected
@app.callback(
    [Output('bar-graph', 'figure'),
    Output('line-graph', 'figure'),
    Output('score_table', 'children')],
    [Input('student-selector', 'value')
    ])
def new_student(studentid):

    student = Student(studentid)
    student.get_scores()

    return student.line_graph(), student.bar_graph(), generate_table(student.scores[['metricid', 'date', 'score']])



if __name__ == '__main__':
    app.run_server(debug=True)
