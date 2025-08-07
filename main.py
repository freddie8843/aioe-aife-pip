# main.py
# 入口脚本，用于加载数据、计算 AIOE 与 AIFE，并输出结果

from compute.compute_aioe import compute_aioe_all
from compute.compute_aife import compute_aife_all
from utils.load_onet import load_onet_data
from utils.load_matrix import load_ai_ability_matrix, compute_Aij_matrix
from utils.load_firm_structure import load_firm_occupation_data

if __name__ == "__main__":
    print("Loading O*NET ability and importance data...")
    onet_abilities = load_onet_data()

    print("Loading AI-ability relevance matrix and computing Aij...")
    xij_matrix = load_ai_ability_matrix()
    Aij_matrix = compute_Aij_matrix(xij_matrix)

    print("Computing AIOE for each occupation...")
    aioe_dict = compute_aioe_all(Aij_matrix, onet_abilities)

    print("Loading firm-level occupational data...")
    firm_occupation_df = load_firm_occupation_data()

    print("Computing AIFE for each firm and year...")
    aife_df = compute_aife_all(firm_occupation_df, aioe_dict)

    # 输出结果（示例：存为 CSV）
    aife_df.to_csv("output/AIFE_results.csv", index=False)
    print("All done. AIFE results saved to output/AIFE_results.csv")
