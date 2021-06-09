import numpy as np
import pandas as pd


def generate_nd_data(mu: int, sigma: float, n_samples: int, create_dims: int) -> pd.DataFrame:
    """
    Creates an n-dimensional dataframe from defined parameters.
    """
    dim_list = range(0, create_dims)
    # Create n normal distribution(s)
    normal_data = np.array([np.random.normal(mu, sigma, n_samples) for _ in dim_list]).T
    # Create a pandas df with each distribution as a column
    return pd.DataFrame(data=normal_data, columns=[i for i in dim_list])
