import plotly.graph_objects as go
import plotly.express as px
from query_data_sqlite import report_student

class Student:
    def __init__(self, studentid):
        self.studentid = studentid

    def get_scores(self):
        self.scores = report_student(self.studentid)

    def line_graph(self, metrics='all'):

        '''
        Function that returns line graph of student's performance
        metrics can be set to all, or a list of metrics to be charted
        '''

        fig = go.Figure()

        if metrics=='all':
            metricid_list = self.scores.metricid.unique()

        else:
            metricid_list = metrics


        for id in metricid_list:
            fig.add_trace(go.Scatter(x=self.scores[self.scores.metricid==id].date, y=self.scores[self.scores.metricid==id].score, name='linear', line_shape='linear'))



        return fig


    def bar_graph(self, metrics='all'):
        
        '''
        Function that returns bar graph of most recent test scores for each
        metric for a given student
        '''
        
        fig = go.Figure()

        if metrics=='all':
            metricid_list = self.scores.metricid.unique()

        else:
            metricid_list = metrics

        y = []

        for metric in metricid_list:
            temp = self.scores[self.scores.metricid == metric]

            y.append(temp[temp.date==max(temp.date)].score.values[0])

        fig = go.Figure(data=[go.Bar(x=metricid_list, y=y, text=y, textposition='auto')])

        fig['layout']['yaxis1'].update(range=[0, 105], autorange=False)

        fig.add_shape(type='line', x0=0.5, y0=70, x1=len(metricid_list)+0.5, y1=70) 

        fig.add_shape(type='line', x0=0.5, y0=100, x1=len(metricid_list)+0.5, y1=100) 
 

        return fig



