import dash
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output
from dimreduce.expand_dimensionality import expand_dims
from plotly import graph_objects as go


def create_callbacks(app, model: 'Union[TruncatedSVD, umap.umap_.UMAP]', orig_tags: list) -> go.Figure:
    """
    Callback functions drive the data shown in the figures defined in dash_app.py.
    """
    
    # Click event updates
    @app.callback([Output('x_value', 'value'),
                   Output('y_value', 'value')], [Input('x_value', 'value'),
                                                      Input('y_value', 'value'),
                                                      Input('density_2d', 'clickData')])
    def update_on_2d_click(x, y, clickData):
        """
        Updates the value of x and y when a click is detected on the 2D density plot
        """
        if dash.callback_context.triggered:
            if dash.callback_context.triggered[0]['prop_id'] == 'density_2d.clickData':
                # use clicked value to update x and y values
                x = clickData['points'][0]['x']
                y = clickData['points'][0]['y']

        return x, y    

    # Create table approximating reprojection to original dimensionality
    @app.callback(Output('table_inverse', 'figure'), [Input('x_value', 'value'),
                                                     Input('y_value', 'value')])
    def approx_projection_table(x: float, y: float) -> go.Figure:
        """
        Performs an approximate inverse transform of the reduced components back into the original space.
        """
        # use a trained model to perform the inverse transform on components
        reproj = expand_dims(model, vals=[x, y])
        # build a table
        fig = go.Figure(data=[go.Table(
            header=dict(values=['Tag', 'Value'],
                        align='left'),
            cells=dict(values=[np.array([[t] for t in orig_tags]), reproj.T],
                       align='left'))
        ], layout={'autosize': True})
        return fig
