import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Solar Farm Analysis", layout="wide")

st.title("☀️ Solar Farm Analysis Dashboard")

@st.cache_data
def load_data():
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
