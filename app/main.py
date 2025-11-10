import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Solar Farm Analysis", layout="wide")

st.title("☀️ Solar Farm Analysis Dashboard")

def create_sample_data():
    if not os.path.exists('data'):
        os.makedirs('data')
    
    np.random.seed(42)
    
    if not os.path.exists('data/benin_clean.csv'):
        benin_df = pd.DataFrame({
            'GHI': np.random.uniform(200, 900, 1000),
            'DNI': np.random.uniform(300, 850, 1000),
            'DHI': np.random.uniform(50, 400, 1000),
            'Tamb': np.random.uniform(25, 38, 1000),
            'RH': np.random.uniform(40, 85, 1000),
            'WS': np.random.uniform(1, 8, 1000),
            'BP': np.random.uniform(980, 1020, 1000)
        })
        benin_df.to_csv('data/benin_clean.csv', index=False)
    
    if not os.path.exists('data/sierraleone_clean.csv'):
        sl_df = pd.DataFrame({
            'GHI': np.random.uniform(150, 850, 1000),
            'DNI': np.random.uniform(250, 800, 1000),
            'DHI': np.random.uniform(60, 450, 1000),
            'Tamb': np.random.uniform(22, 35, 1000),
            'RH': np.random.uniform(50, 95, 1000),
            'WS': np.random.uniform(0.5, 7, 1000),
            'BP': np.random.uniform(990, 1015, 1000)
        })
        sl_df.to_csv('data/sierraleone_clean.csv', index=False)
    
    if not os.path.exists('data/togo_clean.csv'):
        togo_df = pd.DataFrame({
            'GHI': np.random.uniform(180, 880, 1000),
            'DNI': np.random.uniform(280, 820, 1000),
            'DHI': np.random.uniform(55, 420, 1000),
            'Tamb': np.random.uniform(24, 37, 1000),
            'RH': np.random.uniform(45, 88, 1000),
            'WS': np.random.uniform(0.8, 9, 1000),
            'BP': np.random.uniform(985, 1018, 1000)
        })
        togo_df.to_csv('data/togo_clean.csv', index=False)

@st.cache_data
def load_data():
    create_sample_data()
    
    data_dir = 'data'
    countries_data = {}
    
    if os.path.exists(os.path.join(data_dir, 'benin_clean.csv')):
        benin = pd.read_csv(os.path.join(data_dir, 'benin_clean.csv'))
        benin['Country'] = 'Benin'
        countries_data['Benin'] = benin
    
    if os.path.exists(os.path.join(data_dir, 'sierraleone_clean.csv')):
        sl = pd.read_csv(os.path.join(data_dir, 'sierraleone_clean.csv'))
        sl['Country'] = 'Sierra Leone'
        countries_data['Sierra Leone'] = sl
    
    if os.path.exists(os.path.join(data_dir, 'togo_clean.csv')):
        togo = pd.read_csv(os.path.join(data_dir, 'togo_clean.csv'))
        togo['Country'] = 'Togo'
        countries_data['Togo'] = togo
    
    if countries_data:
        return pd.concat(countries_data.values(), ignore_index=True)
    return None

df = load_data()

if df is None:
    st.warning("No data files found. Please add cleaned CSV files to the data/ directory.")
    st.stop()

st.sidebar.header("Filters")

available_countries = df['Country'].unique().tolist()
countries = st.sidebar.multiselect(
    "Select Countries", 
    available_countries,
    default=available_countries
)

metric = st.sidebar.selectbox(
    "Select Metric", 
    ['GHI', 'DNI', 'DHI', 'Tamb', 'RH', 'WS']
)

filtered = df[df['Country'].isin(countries)]

col1, col2 = st.columns(2)

with col1:
    st.subheader(f"{metric} Distribution by Country")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=filtered, x='Country', y=metric, ax=ax)
    ax.set_ylabel(metric)
    ax.set_xlabel('Country')
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col2:
    st.subheader("Summary Statistics")
    summary = filtered.groupby('Country')[metric].describe()
    st.dataframe(summary)

st.subheader("Average Values Comparison")
avg_data = filtered.groupby('Country')[['GHI', 'DNI', 'DHI']].mean()
st.bar_chart(avg_data)

st.subheader("Correlation Heatmap")
numeric_cols = ['GHI', 'DNI', 'DHI', 'Tamb', 'RH', 'WS', 'BP']
available_cols = [col for col in numeric_cols if col in filtered.columns]

if len(available_cols) > 1:
    fig, ax = plt.subplots(figsize=(10, 8))
    corr = filtered[available_cols].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, ax=ax)
    st.pyplot(fig)
