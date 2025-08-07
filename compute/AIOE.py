# aioe_calculator.py

import pandas as pd
import numpy as np

def compute_aioe(onet_df: pd.DataFrame, relevance_matrix: pd.DataFrame) -> pd.DataFrame:
    """
    计算 AIOE（AI 职业暴露）

    Parameters:
    - onet_df: 包含 O*NET 职业能力重要性（Ijk）和水平（Ljk）数据的 DataFrame，需包含：
        - 'occupation_code'：SOC 职业代码
        - 'ability_id'：能力 ID（1~52）
        - 'importance'：Ijk
        - 'level'：Ljk
    - relevance_matrix: AI 应用与能力相关性的 DataFrame，需包含：
        - ability_id 为 index（或列）
        - application_name 为列名，值为 xij（相关性分数，[0, 1]）

    Returns:
    - aioe_df: 包含每个职业的 AIOE 得分的 DataFrame，包含字段：
        - 'occupation_code'
        - 'aioe_score'
    """

    # Step 1: 计算能力层级暴露 Aj（xij 对每个能力求和）
    # relevance_matrix 应该是 shape (52, 10) — 52 个能力 × 10 个 AI 应用
    aj_series = relevance_matrix.sum(axis=1)  # axis=1 表示对应用求和
    aj_series.name = "Aj"

    # Step 2: 把 Aj 合并到 onet_df 上（按 ability_id 匹配）
    merged_df = onet_df.merge(aj_series, left_on="ability_id", right_index=True)

    # Step 3: 计算职业暴露值：AIOE_k = Σj (Ijk × Aj)（重要性加权平均）
    merged_df["Ijk_x_Aj"] = merged_df["importance"] * merged_df["Aj"]

    aioe_df = merged_df.groupby("occupation_code")["Ijk_x_Aj"].sum().reset_index()
    aioe_df = aioe_df.rename(columns={"Ijk_x_Aj": "aioe_score"})

    return aioe_df
