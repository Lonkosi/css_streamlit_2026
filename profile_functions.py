# -*- coding: utf-8 -*-
"""
Profile Functions
Contains the statistical logic for the Consultations demo.
"""
import pandas as pd
import plotly.express as px
import scipy.stats as stats

def calculate_chisquare_result(df):
    """
    Takes a contingency table (DataFrame), performs Chi-Square test,
    and returns the Test Statistic, p-value, conclusion, and color.
    """
    # Run the test
    # stats.chi2_contingency returns: chi2 stat, p-value, dof, expected_matrix
    chi2_stat, p, dof, expected = stats.chi2_contingency(df)
    
    # Interpret results
    if p < 0.05:
        conclusion = "Result: **Statistically Significant Association**"
        color = "green"
    else:
        conclusion = "Result: **No Significant Association**"
        color = "red"
        
    return chi2_stat, p, conclusion, color

def plot_clustered_bar(df):
    """
    Converts a contingency table into a Clustered Bar Chart for "Categorical vs Categorical" analysis.
    Handles dynamic dataframe sizes.
    """
    # 1. Reset index to turn the Row Labels (e.g., Drug A/Drug B) into a proper column
    df_reset = df.reset_index()
    
    # Use the name of the index if it exists, otherwise call it 'Group'
    index_name = df.index.name if df.index.name else "Group"
    df_reset = df_reset.rename(columns={'index': index_name})
    
    # 2. "Melt" the table from wide format to long format for Plotly
    # Wide: Group | Col1 | Col2 ...
    # Long: Group | Outcome (Variable) | Count (Value)
    df_long = df_reset.melt(id_vars=index_name, var_name='Category', value_name='Count')
    
    # 3. Create Clustered Bar Chart
    fig = px.bar(
        df_long, 
        x=index_name, 
        y="Count", 
        color='Category', 
        barmode="group",
        title="Visualizing the Association (Clustered Bar Chart)",
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    
    fig.update_layout(
        xaxis_title=index_name,
        yaxis_title="Frequency",
        template="plotly_white",
        legend_title="Categories"
    )
    
    return fig