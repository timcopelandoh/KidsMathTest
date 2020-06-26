import plotly.graph_objects as go
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




stud = Student(1)

stud.get_scores()

fig = stud.line_graph()

fig.show()
