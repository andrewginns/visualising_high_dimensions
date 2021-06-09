from typing import Union

import pandas as pd
import umap
from sklearn.decomposition import TruncatedSVD


def reduce_dim(df: pd.DataFrame, n_dims: int,  method: str)\
     -> tuple[pd.DataFrame, Union[TruncatedSVD, umap.umap_.UMAP]]:
    """
    Reduces data dimensionality to a defined number of dimensions.
    """
    # This should be replaced with structural pattern matching when Python 3.10 is released
    reduce_method = method.lower()
    if reduce_method == 'svd':
        model = TruncatedSVD(n_components=n_dims, random_state=42)
    elif reduce_method == 'densmap':
        # densmap is non-invertible
        model = umap.UMAP(densmap=True, random_state=42)
    else:
        raise NotImplementedError('Please select one of the following: "SVD", "densmap"')

    model.fit(df)
    reduced_df = pd.DataFrame(model.transform(df), columns=[f'latent{i}' for i in range(0, n_dims)])
    return reduced_df, model
