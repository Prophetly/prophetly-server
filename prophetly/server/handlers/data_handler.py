import ast
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
#from fbprophet import Prophet

from main_handler import MainHandler


class DataHandler(MainHandler):
    def get(self):
        pass
        """
        # read the DataFrame on file system
        df = pd.read_csv(UPLOAD_DIR + '/' + self.get_arguments('file')[0])

        # create a new DataFrame using selected columns
        new_df = pd.DataFrame()
        new_df['ds'] = df[self.get_arguments('ds')[0]]
        new_df['y'] = df[self.get_arguments('y')[0]]

        try:
            prophet.fit(new_df)
            future = prophet.make_future_dataframe(periods=int(self.get_arguments('futureDurationValue')[0]))
            forecast = prophet.predict(future)

            # convert matplotlib figure to plotly
            plot_object = prophet.plot(forecast)
            plotly_fig = tls.mpl_to_plotly(plot_object)

            # collect the data points from plotly figure for the prediction
            prediction_fig_data = plotly_fig['data']

            # component plots (trend, weekly, yearly)
            components_plot_object = prophet.plot_components(forecast)
            components_plotly_fig = tls.mpl_to_plotly(components_plot_object)

            if self.get_arguments('plotComponents')[0] == 'true':
                trend_fig_data = [go.Scatter(
                    mode='lines',
                    x=components_plotly_fig['data'][0].x,
                    y=components_plotly_fig['data'][0].y
                )]

                weekly_fig_data = [go.Scatter(
                    mode='lines',
                    x=components_plotly_fig['data'][1].x,
                    y=components_plotly_fig['data'][1].y
                )]

                yearly_fig_data = [go.Scatter(
                    mode='lines',
                    x=components_plotly_fig['data'][2].x,
                    y=components_plotly_fig['data'][2].y
                )]

                res = {
                    'prediction': ast.literal_eval(prediction_fig_data.__str__()),
                    'trend': ast.literal_eval(trend_fig_data.__str__()),
                    'weekly': ast.literal_eval(weekly_fig_data.__str__()),
                    'yearly': ast.literal_eval(yearly_fig_data.__str__()),
                }
            else:
                res = {
                    'prediction': ast.literal_eval(prediction_fig_data.__str__()),
                }

            self.write({'plots': res})

        except Exception as e:
            self.clear()
            self.set_status(500)
            self.finish("{0}: {1}".format(e.__class__.__name__, str(e)))
            """
