import pandas as pd
import numpy as np
from scipy import stats


def load_solar_data(filepath):
    df = pd.read_csv(filepath)
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    return df


def detect_outliers_zscore(df, columns, threshold=3):
    z_scores = np.abs(stats.zscore(df[columns].dropna()))
    outliers = z_scores > threshold
    return outliers


def clean_solar_data(df, key_columns=['GHI', 'DNI', 'DHI']):
    df_clean = df.copy()
    df_clean = df_clean.dropna(subset=key_columns)
    
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if df_clean[col].isna().sum() > 0:
            df_clean[col].fillna(df_clean[col].median(), inplace=True)
    
    return df_clean


def calculate_summary_stats(df, columns):
    return df[columns].describe()


def analyze_cleaning_impact(df, module_cols=['ModA', 'ModB']):
    if 'Cleaning' in df.columns:
        return df.groupby('Cleaning')[module_cols].mean()
    return None
