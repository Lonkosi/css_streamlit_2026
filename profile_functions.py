# -*- coding: utf-8 -*-
"""
Profile Functions
Contains the statistical logic for the Consultations demo.
"""
import pandas as pd
import plotly.express as px
import numpy as np

# --- STATISTICAL FUNCTIONS (For Consultations) ---

def generate_clt_distribution(n_samples, sample_size):
    """
    Simulates the Central Limit Theorem.
    1. Generates skewed data (non-normal exponential distribution).
    2. Takes 'n_samples' (1000) of size 'sample_size'.
    3. Calculates the means of those samples.
    """
    # Create a skewed population (e.g., exponential distribution)
    # Using a fixed seed for reproducibility isn't strictly necessary but good practice
    population_data = np.random.exponential(scale=1.0, size=10000)
    
    # Take samples and calculate means
    sample_means = []
    for _ in range(n_samples):
        # Randomly select 'sample_size' items
        sample = np.random.choice(population_data, size=sample_size)
        sample_means.append(np.mean(sample))
        
    return sample_means

def plot_clt_histogram(sample_means, sample_size):
    """
    Plots the distribution of sample means using Plotly.
    """
    df_clt = pd.DataFrame({'Sample Means': sample_means})
    
    fig = px.histogram(
        df_clt, 
        x='Sample Means', 
        nbins=40, 
        title=f"Distribution of Sample Means (Sample Size n = {sample_size})",
        color_discrete_sequence=['#2E86C1'], # Professional Data Blue
        opacity=0.8
    )
    
    # Clean up the layout for a professional look
    fig.update_layout(
        xaxis_title="Sample Mean",
        yaxis_title="Frequency",
        bargap=0.05,
        template="plotly_white"
    )
    return fig