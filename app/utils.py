import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_country_data(filepath, country_name):
    df = pd.read_csv(filepath)
    df['Country'] = country_name
    return df


def create_boxplot(data, x_col, y_col, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=data, x=x_col, y=y_col, ax=ax)
    ax.set_title(title)
    return fig


def create_correlation_heatmap(data, columns):
    fig, ax = plt.subplots(figsize=(10, 8))
    corr = data[columns].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, ax=ax)
    return fig


def calculate_country_summary(data, metric):
    return data.groupby('Country')[metric].describe()
