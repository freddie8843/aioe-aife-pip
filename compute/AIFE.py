# aife.py
# This module computes AIFE (AI Firm Exposure) using occupation-level AIOE scores

from collections import defaultdict
from typing import Dict, List
import pandas as pd

# Optional: import AIOE computation if needed
from aioe import compute_aioe_for_all_occupations

def compute_aife(firm_occupation_data: pd.DataFrame, aioe_scores: Dict[str, float]) -> pd.DataFrame:
    """
    Compute AI Firm Exposure (AIFE) based on occupation composition and AIOE scores.

    Parameters:
    - firm_occupation_data: pd.DataFrame with columns:
        - firm_id (str)
        - occupation_code (str)
        - count (int) or share (float)
    - aioe_scores: dict mapping SOC occupation code to AIOE score

    Returns:
    - pd.DataFrame with columns:
        - firm_id (str)
        - aife_score (float)
    """
    firm_scores = defaultdict(float)

    for _, row in firm_occupation_data.iterrows():
        firm_id = row["firm_id"]
        occupation_code = row["occupation_code"]
        share = row["share"] if "share" in row else row["count"]  # fallback

        aioe = aioe_scores.get(occupation_code)
        if aioe is not None:
            firm_scores[firm_id] += share * aioe

    return pd.DataFrame([
        {"firm_id": fid, "aife_score": round(score, 4)} for fid, score in firm_scores.items()
    ])

# Example usage (to be replaced with real data pipeline later)
if __name__ == "__main__":
    # Load firm-occupation data
    firm_occ_df = pd.read_csv("firm_occupation_data.csv")  # Replace with actual data path

    # Load or compute AIOE scores
    aioe_scores_dict = compute_aioe_for_all_occupations()  # Assume you already implemented this

    # Compute AIFE
    result_df = compute_aife(firm_occ_df, aioe_scores_dict)
    result_df.to_csv("aife_scores.csv", index=False)
    print("AIFE computation complete. Output saved to aife_scores.csv")
