# css_streamlit_2026
# 📊 Research Profile & Statistical Consultation App

## 📖 Overview
This repository contains the source code for my digital research portfolio and interactive statistical consultation tool. Built with **Python** and **Streamlit**, this application serves two purposes:

1.  **Professional Profile:** showcases my academic background, teaching experience at Walter Sisulu University, and research expertise in Survival Analysis and Epidemiology.
2.  **Interactive Statistical Demo:** Features a dynamic **Chi-Square Test of Association** calculator. This tool allows researchers to build custom contingency tables, perform real-time hypothesis testing, and visualize results without needing expensive software.

## ✨ Key Features

### 1. Professional Portfolio
* **About Me:** Academic history, PhD candidacy details, and lecturing experience.
* **Services:** Overview of consultation areas (GLMs, Survival Analysis, Experimental Design).
* **Publications:** List of published and ongoing research work.

### 2. Interactive Chi-Square Calculator
A fully functional statistical tool designed for educational and consultation purposes:
* **Dynamic Dimensions:** Users can set custom row (Groups) and column (Outcomes) sizes (e.g., 2x2, 3x5).
* **Editable Data:** Interactive table that allows users to input their own observed frequencies.
* **Smart Persistence:** Uses `st.session_state` to prevent data loss during app interactions.
* **Real-time Analysis:** Instantly calculates Pearson's $\chi^2$ statistic and p-value.
* **Visualization:** Generates professional Clustered Bar Charts using Plotly Express.

## 🛠️ Technologies Used
* **Streamlit:** Web application framework.
* **Pandas & NumPy:** Data manipulation and state management.
* **SciPy (`scipy.stats`):** Statistical computation (Chi-Square contingency tests).
* **Plotly Express:** Interactive data visualization.

## 🚀 How to Run Locally

To run this app on your own machine, follow these steps:

### Prerequisites
Make sure you have Python installed (version 3.8 or higher).

### Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name
