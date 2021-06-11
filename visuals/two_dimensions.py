import plotly.figure_factory as ff


def plot_2d_density(x_data: 'np.array', y_data: 'np.array') -> ff.create_2d_density:
    return ff.create_2d_density(x_data, y_data, point_size=3)
