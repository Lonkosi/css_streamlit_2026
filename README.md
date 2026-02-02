# css_streamlit_2026
# 📊 Research Profile & Statistical Consultation App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://css-streamlit-2026.streamlit.app/)

## 📖 Overview
This repository contains the source code for my digital research portfolio and interactive statistical consultation tool. Built with **Python** and **Streamlit**, this application serves two purposes:

1.  **Professional Profile:** Showcases my academic background, teaching experience at Walter Sisulu University, and research expertise in Survival Analysis and Epidemiology.
2.  **Interactive Statistical Demo:** Features a dynamic **Chi-Square Test of Association** calculator. This tool allows researchers to build custom contingency tables, perform real-time hypothesis testing, and visualize results instantly.

## ✨ Key Features

### 1. Professional Portfolio
* **About Me:** Academic history, PhD candidacy details, and over 15 years of lecturing experience.
* **Services:** Overview of consultation areas including GLMs, Survival Analysis, and Experimental Design.
* **Publications:** List of published research and ongoing doctoral work.

### 2. Interactive Chi-Square Calculator
A fully functional statistical tool designed for researchers and students:
* **Dynamic Dimensions:** Set custom row (Groups) and column (Outcomes) sizes (e.g., 2x2, 3x5, etc.).
* **Editable Data:** Interactive grid for inputting observed frequencies.
* **Smart Persistence:** State management ensures your data remains intact while you rename headers or change settings.
* **Real-time Analysis:** Instantly calculates Pearson's $\chi^2$ statistic and associated p-values using SciPy.
* **Visualization:** Generates professional Clustered Bar Charts to identify patterns across groups.



## 🛠️ Technologies Used
* **Streamlit:** Web application framework.
* **Pandas & NumPy:** Data manipulation and state management.
* **SciPy (`scipy.stats`):** Statistical computation.
* **Plotly Express:** Interactive data visualization.

## 🚀 How to Run Locally

If you wish to run this application on your local machine, follow these steps:

### Prerequisites
Ensure you have Python 3.8+ installed.

### Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Lonkosi/css_streamlit_2026.git](https://github.com/Lonkosi/css_streamlit_2026.git)
   cd css_streamlit_2026
