# load_matrix.py

import pandas as pd

def load_matrix_from_csv(filepath, index_col=None):
    """
    Load a matrix (e.g., ability-occupation or AI relevance matrix) from a CSV file.

    Parameters:
        filepath (str): Path to the CSV file.
        index_col (int or str, optional): Column to use as the row labels of the DataFrame.

    Returns:
        pd.DataFrame: The loaded matrix as a pandas DataFrame.
    """
    try:
        df = pd.read_csv(filepath, index_col=index_col)
        print(f"[INFO] Successfully loaded matrix from: {filepath}")
        return df
    except Exception as e:
        print(f"[ERROR] Failed to load matrix from {filepath}: {e}")
        return None
