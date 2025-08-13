import pandas as pd
import os

def load_onet_level_importance(onet_dir: str):
    """
    Load Level (Ljk) and Importance (Ijk) from O*NET Excel files.
    Required files:
        - Abilities.xlsx (for ability ID mapping)
        - Skills.xlsx (for skill ID mapping, if needed)
        - Abilities to Work Context.xlsx (optional if crosswalk needed)
        - Occupation Data.xlsx (SOC mappiSng)
        - Level Scale Anchors.xlsx (optional reference)
        - Task Ratings.xlsx (if extending with tasks)
    """
    # Load abilities metadata
    abilities = pd.read_excel(os.path.join(onet_dir, "Abilities.xlsx"))
    print(f"Loaded Abilities metadata: {abilities.shape}")

    # Load level and importance scores
    work_context_level = pd.read_excel(os.path.join(onet_dir, "Abilities to Work Context.xlsx"))
    print(f"Loaded Level/Importance matrix: {work_context_level.shape}")

    # (Optional) Clean and merge if needed, depends on file structure
    # Usually columns are: 'O*NET-SOC Code', 'Element ID', 'Scale ID', 'Data Value'
    level_data = work_context_level[work_context_level['Scale ID'] == 'LV']
    importance_data = work_context_level[work_context_level['Scale ID'] == 'IM']

    # Pivot to wide format: rows = occupation, columns = ability
    level_pivot = level_data.pivot(index='O*NET-SOC Code', columns='Element ID', values='Data Value')
    importance_pivot = importance_data.pivot(index='O*NET-SOC Code', columns='Element ID', values='Data Value')

    # Fill NAs with 0 (optional, depends on data quality)
    level_pivot.fillna(0, inplace=True)
    importance_pivot.fillna(0, inplace=True)

    print(f"Level matrix shape: {level_pivot.shape}, Importance matrix shape: {importance_pivot.shape}")
    return level_pivot, importance_pivot
