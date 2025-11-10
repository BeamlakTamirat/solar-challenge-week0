"""
Data processing utilities for solar farm analysis
"""

import pandas as pd
import numpy as np
from scipy import stats


def load_solar_data(filepath):
    """
    Load solar data from CSV file
    
    Args:
        filepath (str): Path to CSV file
        
    Returns:
        pd.DataFrame: Loaded dataframe
    """
    df = pd.read_csv(filepath)
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    return df


def detect_outliers_zscore(df, columns, threshold=3):
    """
    Detect outliers using Z-score method
    
    Args:
        df (pd.DataFrame): Input dataframe
        columns (list): List of column names to check
        threshold (float): Z-score threshold (default: 3)
        
    Returns:
        pd.DataFrame: Boolean dataframe indicating outliers
    """
    z_scores = np.abs(stats.zscore(df[columns].dropna()))
    outliers = z_scores > threshold
    return outliers


def clean_solar_data(df, key_columns=['GHI', 'DNI', 'DHI']):
    """
    Clean solar data by handling missing values and outliers
    
    Args:
        df (pd.DataFrame): Input dataframe
        key_columns (list): Key columns that must not have missing values
        
    Returns:
        pd.DataFrame: Cleaned dataframe
    """
    # Create a copy
    df_clean = df.copy()
    
    # Drop rows with missing values in key columns
    df_clean = df_clean.dropna(subset=key_columns)
    
    # Optional: Fill other missing values with median
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if df_clean[col].isna().sum() > 0:
            df_clean[col].fillna(df_clean[col].median(), inplace=True)
    
    return df_clean


def calculate_summary_stats(df, columns):
    """
    Calculate summary statistics for specified columns
    
    Args:
        df (pd.DataFrame): Input dataframe
        columns (list): List of column names
        
    Returns:
        pd.DataFrame: Summary statistics
    """
    return df[columns].describe()


def analyze_cleaning_impact(df, module_cols=['ModA', 'ModB']):
    """
    Analyze the impact of cleaning on module performance
    
    Args:
        df (pd.DataFrame): Input dataframe
        module_cols (list): Module column names
        
    Returns:
        pd.DataFrame: Grouped statistics by cleaning flag
    """
    if 'Cleaning' in df.columns:
        return df.groupby('Cleaning')[module_cols].mean()
    return None
