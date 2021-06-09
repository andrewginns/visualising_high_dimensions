# from sklearn.pipeline import Pipeline


from visuals.dash_app import Dashboard
from gendata.create_nd_data import generate_nd_data
from dimreduce.reduce_dimensionality import reduce_dim

if __name__ == "__main__":
    # Data loading
    data_df = generate_nd_data(0, 1, 1000, 4)
    # Dim reduction goes here
    latent_df, model = reduce_dim(data_df, 2, 'svd')
    # Create the app
    dash_app = Dashboard(latent_df, data_df.columns, model)
    dash_app.create_figs()
    dash_app.define_layout()
    

    dash_app.app.run_server(debug=True)