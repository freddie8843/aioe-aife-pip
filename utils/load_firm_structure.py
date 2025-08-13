# load_firm_structure.py

import pandas as pd

def load_firm_postings(filepath: str, encoding='utf-8') -> pd.DataFrame:
    """
    Load firm-level job postings data from a CSV or Excel file.
    
    Expected columns:
        - firm_id or firm_name
        - occupation_code (e.g., SOC)
        - num_postings (or counts, optional)
    
    Parameters:
        filepath (str): Path to the data file (.csv or .xlsx)
        encoding (str): Encoding type if CSV
    
    Returns:
        pd.DataFrame: Cleaned dataframe of job postings
    """
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath, encoding=encoding)
    elif filepath.endswith('.xlsx'):
        df = pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file type. Only .csv and .xlsx are supported.")
    
    df.columns = df.columns.str.lower().str.strip()
    
    required_cols = {'firm_id', 'occupation_code'}
    if not required_cols.issubset(set(df.columns)):
        raise ValueError(f"Missing required columns: {required_cols - set(df.columns)}")

    # Optional normalization
    if 'num_postings' not in df.columns:
        df['num_postings'] = 1  # assume 1 per row if not provided

    return df


def pivot_firm_structure(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert long format (firm, occupation, num_postings) to wide matrix format:
    Rows = firms, Columns = occupations
    
    Parameters:
        df (pd.DataFrame): Long format DataFrame.
    
    Returns:
        pd.DataFrame: Firm × Occupation matrix.
    """
    matrix = df.pivot_table(
        index='firm_id',
        columns='occupation_code',
        values='num_postings',
        aggfunc='sum',
        fill_value=0
    )
    return matrix


def normalize_firm_matrix(matrix: pd.DataFrame, axis=1) -> pd.DataFrame:
    """
    Normalize firm matrix across firms (axis=1) or occupations (axis=0).
    
    Parameters:
        matrix (pd.DataFrame): Firm-occupation matrix
        axis (int): 0 = normalize each occupation column; 1 = normalize each firm row
    
    Returns:
        pd.DataFrame: Normalized matrix
    """
    norm = (matrix ** 2).sum(axis=axis, keepdims=True) ** 0.5
    return matrix / norm


def print_firm_stats(df: pd.DataFrame):
    """
    Print summary stats of firm data.
    """
    print(f"[INFO] Total firms: {df['firm_id'].nunique()}")
    print(f"[INFO] Total unique occupations: {df['occupation_code'].nunique()}")
    print(f"[INFO] Total rows: {len(df)}")
