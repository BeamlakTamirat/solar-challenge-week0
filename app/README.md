# Streamlit Dashboard

Interactive dashboard for visualizing solar farm data across Benin, Sierra Leone, and Togo.

## Features
- Country selection filters
- Interactive boxplots for GHI, DNI, DHI comparison
- Summary statistics tables
- Correlation heatmaps
- Multi-metric bar charts

## Run Locally
```bash
streamlit run app/main.py
```

## Requirements
- Cleaned CSV files must be in `data/` directory:
  - benin_clean.csv
  - sierraleone_clean.csv
  - togo_clean.csv
