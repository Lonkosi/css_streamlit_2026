import streamlit as st
import profile_functions as pf  # Importing your custom module
import pandas as pd
import numpy as np
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Ido Jubane - Research Consultant", page_icon="📈", layout="wide")

# --- CUSTOM FONT CSS ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
        
        /* Target specific text elements to avoid breaking icons */
        html, body, p, li, .stMarkdown, .stDataFrame { 
            font-family: 'Roboto', sans-serif !important; 
        }
        
        /* Headers color and font */
        h1, h2, h3 { 
            color: #2E86C1 !important;
            font-family: 'Roboto', sans-serif !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Consultations", "Publications", "Contact"])

# --- PAGE 1: HOME ---
if page == "Home":
    st.title("🎓 Ido Jubane")
    st.subheader("Statistics Lecturer | Research Consultant | Data Analyst")
    
    if os.path.exists("ido.jpg"):
        st.image("ido.jpg", caption="Ido Jubane", width=250)
    else:
        st.warning("⚠️ Image 'ido.jpg' not found. Please ensure it is in the same folder.")
        st.image("https://placehold.co/250x250", caption="Ido Jubane (Placeholder)") 
    
    st.header("About Me")
    st.write("""
    I am an accomplished lecturer with over 15 years of experience in teaching statistics and 
    mathematics. I currently serve as a **Statistics Lecturer** at **Walter Sisulu University**.
    My expertise lies in **Survival Analysis**, **Epidemiology**, and **Quantitative Modelling**.
    """)
    st.info("👈 Select 'Consultations' to see how I can support your research!")

# --- PAGE 2: CONSULTATIONS ---
elif page == "Consultations":
    st.title("💡 Statistical Consultation Services")
    st.error("⚠️ **The Golden Rule:** Consult a statistician *before* you collect your data!")
    
    st.markdown("""
    ### Why Consult Early?
    **"To consult the statistician after an experiment is finished is often merely to ask him to conduct a post mortem examination."** — *Ronald Fisher*
    """)
    st.divider()
    
    st.subheader("🧪 Areas of Statistical Expertise")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Advanced Modelling:** Survival Analysis, GLMs, Mixed Effects.")
    with col2:
        st.markdown("**Testing & Design:** Multivariate Analysis, Power Analysis, Experimental Design.")
    st.divider()
    
    # --- INTERACTIVE DEMO SECTION (UPDATED) ---
    st.subheader("📊 Interactive Demo: Chi-Square Test of Association")
    st.markdown("""
    This tool demonstrates how we determine if two **Categorical Variables** are related (e.g., *Treatment Type* vs. *Health Outcome*). 
    We use the **Pearson Chi-Square Test** to see if the observed patterns differ significantly from what we would expect by chance.
    """)

    st.markdown("---")

    # --- TWO COLUMN LAYOUT ---
    col_text, col_demo = st.columns([1, 2])
    
    # LEFT COLUMN: EXPLANATION
    with col_text:
        st.info("### 📌 How It Works")
        st.write("""
        **1. Build the Table:**
        Define your groups (rows) and outcomes (columns).
        
        **2. Enter Data:**
        Input your observed frequencies.
        
        **3. The Statistical Test:**
        The app calculates **Pearson's $\chi^2$**.
        * **P < 0.05:** Significant Association (The variables are related).
        * **P ≥ 0.05:** No Association (They are independent).
        
        **4. Visualization:**
        The **Clustered Bar Chart** helps identify where the differences lie.
        """)
        
    # RIGHT COLUMN: DYNAMIC CALCULATOR
    with col_demo:
        st.write("#### 👇 Build Your Contingency Table")
        
        # A. SETUP DIMENSIONS
        c1, c2 = st.columns(2)
        n_rows = c1.number_input("Number of Rows (Groups)", min_value=2, max_value=10, value=2)
        n_cols = c2.number_input("Number of Columns (Outcomes)", min_value=2, max_value=10, value=2)

        # B. SETUP HEADERS (Editable)
        with st.expander("✏️ Rename Row & Column Headers", expanded=False):
            row_input = st.text_input(f"Row Names (comma separated, need {n_rows})", 
                                      value="Drug A, Drug B" if n_rows==2 else ",".join([f"Row {i+1}" for i in range(n_rows)]))
            col_input = st.text_input(f"Column Names (comma separated, need {n_cols})", 
                                      value="Cured, Not Cured" if n_cols==2 else ",".join([f"Col {i+1}" for i in range(n_cols)]))
        
        # Process headers safely
        row_names = [x.strip() for x in row_input.split(',')]
        col_names = [x.strip() for x in col_input.split(',')]
        
        # Fallback if user types too few/many names
        if len(row_names) != n_rows: row_names = [f"Row {i+1}" for i in range(n_rows)]
        if len(col_names) != n_cols: col_names = [f"Col {i+1}" for i in range(n_cols)]

        # C. CREATE & EDIT DATA
        # Initialize with random reasonable numbers if it's a new shape
        default_data = pd.DataFrame(
            np.random.randint(10, 100, size=(n_rows, n_cols)),
            index=row_names,
            columns=col_names
        )
        
        st.caption("Double-click cells to edit the values:")
        edited_df = st.data_editor(default_data, use_container_width=True)
        
        # D. RUN ANALYSIS
        st.divider()
        chi2_stat, p_val, conclusion, color = pf.calculate_chisquare_result(edited_df)
        
        # Display Metrics
        m1, m2 = st.columns(2)
        m1.metric("Pearson $\chi^2$ Statistic", f"{chi2_stat:.2f}")
        m2.metric("P-Value", f"{p_val:.4f}")
        
        if color == "green":
            st.success(f"{conclusion} (p < 0.05)")
        else:
            st.warning(f"{conclusion} (p >= 0.05)")

        # E. PLOT
        fig = pf.plot_clustered_bar(edited_df)
        st.plotly_chart(fig, use_container_width=True)

# --- PAGE 3: PUBLICATIONS ---
elif page == "Publications":
    st.title("📚 Research & Publications")
    st.subheader("Published Work")
    st.write("**Fagbamila, T., Qin, Y., Jubane, I., & Odularu, G. (2013).** Preventing HIV/AIDS Deaths in South Africa. Journal of Social and Economic Policy.")
    st.subheader("Ongoing / Unpublished")
    st.write("*PhD Thesis:* Advanced Survival Analysis utilizing Wearable Biomarker Data.")

# --- PAGE 4: CONTACT ---
elif page == "Contact":
    st.title("📬 Get in Touch")
    st.write("I am available for academic collaboration and consultation.")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**📍 Office Address:**")
        st.write("Walter Sisulu University (NMD Campus)\nPrivate Bag X1, Mthatha")
    with col2:
        st.markdown("**📧 Contact Details:**")
        st.write("📧 ijubane@wsu.ac.za")
        st.markdown("🔗 [LinkedIn Profile](https://www.linkedin.com/in/ido-jubane-b2150586)")