import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from plotly import graph_objects as go

from visuals.dash_callbacks import create_callbacks
from visuals.two_dimensions import plot_2d_density


class Dashboard:
    def __init__(self, data: 'pd.DataFrame', orig_cols: list, model: 'Union[TruncatedSVD, umap.umap_.UMAP]') -> None:
        self.app = dash.Dash(__name__)
        self.data = data
        self.latent_cols = self.data.columns
        self.orig_cols = orig_cols
        self.model = model

        create_callbacks(self.app, self.model, self.orig_cols)

    def create_figs(self):
        # Create the components holding figures driven by callbacks
        figs = [go.Figure() for _ in range(0, 2)]

        self.density_2d = dcc.Graph(id='density_2d',
                            figure=plot_2d_density(
                                self.data[self.latent_cols[0]],
                                self.data[self.latent_cols[1]]
                                ),
                            )

        self.table_inverse = dcc.Graph(id='table_inverse', figure=figs[1])
        
        self.latent_vals = [
            dcc.Input(
                id='x_value', type='number', value=0, readOnly=True
                ),
            dcc.Input(
                id='y_value', type='number', value=0, readOnly=True
                ),
            ]

    def define_layout(self):
        # HTML defined components of the visuals
        self.app.layout = html.Div(
            children=[
                html.H1(children='Reduced dimensionality visualisation',),
                html.P(
                    children='Displays a lower dimensional latent space projection'
                    'as well as the original dimensional projection estimate.',
                ),

                dbc.Col(
                    html.Center(
                        children=[self.density_2d],
                    ), 
                    style={'height': '750px'}
                ),
                
                html.Label('Selected latent values, x and y'),
                dbc.Col(
                    html.Center(
                        children=self.latent_vals,
                    ),
                    style={'height': '50px'}
                ),
                
                html.Label(f'Approximate original dimensionality values using {self.model.__class__.__name__}:'),
                dbc.Col(
                    html.Center(
                        children=[self.table_inverse],
                    ),
                    style={'height': '700px'}
                ),
            ],
            style={'height': '750px', 'columnCount': 2}
        )

