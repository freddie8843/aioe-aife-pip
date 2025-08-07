
#  AI Exposure Metrics: AIOE & AIFE Calculator

This repository provides a structured framework to calculate two AI exposure metrics introduced in recent literature:

- **AIOE (AI Occupational Exposure)** – Measures how exposed an occupation is to advances in AI applications.
- **AIFE (AI Firm Exposure)** – Measures how exposed a firm is to AI based on its workforce's occupational composition.

##  What Are AIOE and AIFE?

| Metric | Description | Formula |
|--------|-------------|---------|
| AIOE   | Exposure of occupation _k_ to AI based on how much each ability _j_ (used in _k_) is related to AI applications. | AIOE_k = Σ_j (A_j × (Ijk + Ljk)/2) |
| AIFE   | Exposure of firm _f_ to AI based on weighted average of AIOE scores across its employee occupation distribution. | AIFE_f = Σ_k (share_fk × AIOE_k) |

##  Project Structure

```
├── aioe_calculator.py          # Core logic to compute AIOE for a given occupation
├── aife_calculator.py          # Computes AIFE per firm by calling AIOE module
├── README.md                   # This documentation file
├── data/
│   ├── onet_abilities.csv      # O*NET ability-level data (Ljk, Ijk)
│   ├── ai_application_matrix.csv # Felten's x_ij matrix
│   ├── occupation_mapping.csv  # SOC mapping file
│   └── firm_structure.csv      # Firm → Occupation employee share
```

##  Setup

```bash
git clone https://github.com/your-username/ai-exposure-metrics.git
cd ai-exposure-metrics
pip install -r requirements.txt
```

##  Data Sources

- **O*NET 24.3 Database** (https://www.onetcenter.org/database.html)
- **EFF/Felten et al. (2021) AI Metrics** (https://github.com/AIOE-Data/AIOE)
- **Firm hiring data** (Zhilian, 51job, Liepin 等)
- **CPI (Optional)**: For wage normalization

##  How to Use

1. **Compute AIOE for all occupations:**

```python
from aioe_calculator import compute_aioe_for_all_occupations

aioe_scores = compute_aioe_for_all_occupations(onet_df, xij_matrix)
```

2. **Compute AIFE for each firm:**

```python
from aife_calculator import compute_aife_for_all_firms

aife_scores = compute_aife_for_all_firms(firm_df, aioe_scores)
```

##  Status

- [x] Skeleton functions implemented
- [ ] Data integration
- [ ] Error handling
- [ ] Visualization (optional)

##  To Do

- [ ] Integrate actual O*NET and firm recruitment datasets
- [ ] Add SOC job title mapping NLP pipeline
- [ ] Normalize scores
- [ ] Add wage analysis
