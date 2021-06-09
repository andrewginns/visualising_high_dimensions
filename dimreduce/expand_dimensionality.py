import pandas as pd


def expand_dims(model: 'Union[TruncatedSVD, umap.umap_.UMAP]', vals: list) -> pd.DataFrame:
    labels = [f'ldim{i}' for i in range(0, len(vals))]
    if len(labels) == 2:
        try:
            expanded_pd = model.inverse_transform(pd.DataFrame({labels[0]: [vals[0]], labels[1]: [vals[1]]}))
        except ValueError as e:
            print(f'{e}\nModel is not invertible, no data will be output.')
    return expanded_pd

def expand_dims_table(model: 'Union[TruncatedSVD, umap.umap_.UMAP]', df_data: pd.DataFrame, cols: list) -> pd.DataFrame:
    try:
        return pd.DataFrame(model.inverse_transform(df_data), columns=cols)
    except ValueError as e:
        print(f'{e}\nModel is not invertible, no data will be output.')