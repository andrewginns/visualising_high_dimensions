# Dimensionality Reduction and Visualisation

This code respository explores different methods of taking high dimensional data and presenting it in a lower dimensional latent space.

Visualisations use Plotly graph objects and a Dash web app interface.

A number of different techniques will be explored:
1. Truncated SVD
    * Taking the top eigenvectors by variance
2. Densmap
    * An extention of umap that preserves density
3. VAE
    * An encoder-decoder architecture that creates a lower dimensional embedding of the data