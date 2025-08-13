# match_utils.py

import pandas as pd

def match_abilities(df1, df2, how='inner'):
    """
    Match two dataframes on their indices (e.g., abilities) and return aligned dataframes.
    
    Parameters:
        df1 (pd.DataFrame): First dataframe (e.g., O*NET ability-occupation matrix).
        df2 (pd.DataFrame): Second dataframe (e.g., AI application-ability matrix).
        how (str): Type of join to perform. Default is 'inner'. Options: 'inner', 'outer', 'left', 'right'.
    
    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: Aligned dataframes (df1_aligned, df2_aligned).
    """
    # Get common abilities
    common = df1.index.intersection(df2.index) if how == 'inner' else df1.index.union(df2.index)
    
    df1_aligned = df1.loc[common].sort_index()
    df2_aligned = df2.loc[common].sort_index()
    
    return df1_aligned, df2_aligned


def validate_shape(df1, df2):
    """
    Check if two dataframes are aligned for matrix multiplication.
    
    Parameters:
        df1 (pd.DataFrame): First dataframe (e.g., AI x ability).
        df2 (pd.DataFrame): Second dataframe (e.g., ability x occupation).
    
    Returns:
        bool: True if shapes are compatible, else False.
    """
    return df1.shape[1] == df2.shape[0]


def normalize_matrix(df, axis=0):
    """
    Normalize a DataFrame along a given axis using L2 norm.
    
    Parameters:
        df (pd.DataFrame): DataFrame to normalize.
        axis (int): 0 for column-wise, 1 for row-wise.
    
    Returns:
        pd.DataFrame: Normalized DataFrame.
    """
    norm = (df ** 2).sum(axis=axis, keepdims=True) ** 0.5
    return df / norm


def print_shape_info(df1, df2):
    """
    Print shapes and matching info of two matrices.
    """
    print(f"[INFO] Matrix 1 shape: {df1.shape}")
    print(f"[INFO] Matrix 2 shape: {df2.shape}")
    print(f"[INFO] Dimensions match for dot product: {validate_shape(df1.T, df2)}")
