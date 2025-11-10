# Solar Challenge Week 0

## Overview
This project analyzes solar farm data from Benin, Sierra Leone, and Togo to identify high-potential regions for solar installation. The analysis focuses on solar radiation measurements, environmental factors, and their correlations to support data-driven investment decisions for MoonLight Energy Solutions.

## Project Structure
```
solar-challenge-week0/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── notebooks/
│   ├── benin_eda.ipynb
│   ├── sierraleone_eda.ipynb
│   ├── togo_eda.ipynb
│   └── compare_countries.ipynb
├── scripts/
│   └── data_processing.py
├── tests/
│   └── test_data.py
└── app/
    ├── main.py
    └── utils.py
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/BeamlakTamirat/solar-challenge-week0.git
cd solar-challenge-week0
```

### 2. Create Virtual Environment
```bash
# Using venv
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Data Setup
- Place your CSV files in the `data/` directory (not tracked by git)
- Expected files:
  - `benin-malanville.csv`
  - `sierraleone-bumbuna.csv`
  - `togo-dapaong_qc.csv`

## Usage

### Run Jupyter Notebooks
```bash
jupyter notebook
```

### Run Streamlit Dashboard
```bash
streamlit run app/main.py
```

## Dataset Description
The dataset includes solar radiation measurements with the following key variables:
- **GHI** (W/m²): Global Horizontal Irradiance
- **DNI** (W/m²): Direct Normal Irradiance
- **DHI** (W/m²): Diffuse Horizontal Irradiance
- **Tamb** (°C): Ambient Temperature
- **RH** (%): Relative Humidity
- **WS** (m/s): Wind Speed
- **BP** (hPa): Barometric Pressure

## Analysis Tasks
1. **Data Profiling & Cleaning**: Summary statistics, outlier detection, missing value handling
2. **Exploratory Data Analysis**: Time series analysis, correlation studies, distribution analysis
3. **Cross-Country Comparison**: Statistical testing and comparative visualizations
4. **Interactive Dashboard**: Streamlit-based visualization tool


## Contributors
- Beamlak Tamirat

## License
MIT License
