import streamlit as st
import profile_functions as pf  # Importing your custom module
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Ido Jubane - Research Consultant", page_icon="📈", layout="wide")

# --- CUSTOM FONT CSS ---
st.markdown("""
    <style>
        /* Import a nice font from Google */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

        html, body, [class*="st-"] {
            font-family: 'Roboto', sans-serif;
        }
        
        /* Optional: Change header colors to be more 'Research Blue' */
        h1, h2, h3 {
            color: #2E86C1; 
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Navigation")
# Removed "Data Showcase" from the menu
page = st.sidebar.radio("Go to:", ["Home", "Consultations", "Publications", "Contact"])

# --- PAGE 1: HOME ---
if page == "Home":
    st.title("🎓 Ido Jubane")
    st.subheader("Statistics Lecturer | Research Consultant | Data Analyst")
    
    # --- PHOTO LOGIC ---
    if os.path.exists("ido.jpg"):
        st.image("ido.jpg", caption="Ido Jubane", width=250)
    else:
        st.warning("⚠️ Image 'ido.jpg' not found. Please ensure it is in the same folder as this script.")
        st.image("https://placehold.co/250x250", caption="Ido Jubane (Placeholder)") 
    
    st.header("About Me")
    st.write("""
    I am an accomplished lecturer with over 15 years of experience in teaching statistics and 
    mathematics. I currently serve as a **Statistics Lecturer** at **Walter Sisulu University** (Department of Maths, Science & Computing).
    
    My expertise lies in bridging the gap between complex statistical theory and practical research application. 
    I specialize in **Survival Analysis**, **Epidemiology**, and **Quantitative Modelling**.
    """)
    
    st.subheader("Education")
    st.markdown("""
    * **PhD Candidate (Current):** Survival Analysis & Wearable Biomarkers.
    * **MSc in Biostatistics and Epidemiology** - University of Fort Hare.
    * **BSc Hons in Applied Statistics** - University of Fort Hare.
    * **BSc in Computer Science & Mathematical Statistics** - University of Fort Hare.
    """)
    
    st.info("👈 Select 'Consultations' to see how I can support your research!")

# --- PAGE 2: CONSULTATIONS (Expanded & Updated) ---
elif page == "Consultations":
    st.title("💡 Statistical Consultation Services")
    
    st.error("⚠️ **The Golden Rule:** Consult a statistician *before* you collect your data!")
    
    st.markdown("""
    ### Why Consult Early?
    **"To consult the statistician after an experiment is finished is often merely to ask him to conduct a post mortem examination. He can perhaps say what the experiment died of."** — *Ronald Fisher*
    
    I provide rigorous statistical support for Master's, PhD, and corporate research projects.
    """)
    
    st.divider()
    
    st.subheader("🧪 Areas of Statistical Expertise")
    st.write("I utilize advanced methodologies to ensure robust, publishable results.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Advanced Modelling")
        st.markdown("""
        * **Survival Analysis:** Kaplan-Meier, Cox Proportional Hazards.
        * **Generalized Linear Models (GLM):** Logistic, Poisson, & Negative Binomial Regression.
        * **Mixed Effects Models:** For longitudinal or hierarchical data.
        * **Structural Equation Modelling (SEM):** Path analysis and latent variables.
        """)
        
    with col2:
        st.markdown("#### Testing & Design")
        st.markdown("""
        * **Multivariate Analysis:** MANOVA, PCA, and Factor Analysis (EFA/CFA).
        * **Power Analysis:** Precision Sample Size calculation (G*Power/R).
        * **Experimental Design:** RCTs, Block Designs, and Factorial Experiments.
        * **Non-Parametric Tests:** Mann-Whitney, Kruskal-Wallis, Wilcoxon.
        """)
        
    st.divider()
    
    st.subheader("🎓 Demonstration: The Power of Sample Size")
    st.markdown("""
    One of the most common questions I get is: *"How large should my sample be?"*
    
    The simulation below demonstrates the **Central Limit Theorem (CLT)**. It shows that even if your raw data is skewed (messy), taking a large enough sample size ensures your results follow a Normal Distribution—allowing us to use powerful parametric tests.
    """)
    
    # Interactive Controls
    col_input1, col_input2 = st.columns([1, 2])
    with col_input1:
        st.markdown("**👇 Experiment here:**")
        n = st.slider("Select Sample Size (n):", min_value=2, max_value=500, value=30)
        
        if n < 30:
            st.warning("⚠️ **Small Sample (n < 30):** The distribution is irregular. Results may be unreliable.")
        else:
            st.success("✅ **Adequate Sample:** The distribution approaches Normality. Parametric tests are valid.")
            
    with col_input2:
        # Logic from profile_functions.py
        sample_means = pf.generate_clt_distribution(n_samples=1000, sample_size=n)
        fig = pf.plot_clt_histogram(sample_means, sample_size=n)
        st.plotly_chart(fig, use_container_width=True)

# --- PAGE 3: PUBLICATIONS ---
elif page == "Publications":
    st.title("📚 Research & Publications")
    
    st.subheader("Published Work")
    st.markdown("""
    * **Fagbamila, T., Qin, Y., Jubane, I., & Odularu, G. (2013).**
      *Preventing HIV/AIDS Deaths in South Africa: Strategic Policy Suggestions.*
      Journal of Social and Economic Policy, 10(1), 1-8.
    """)
    
    st.subheader("Ongoing / Unpublished")
    st.markdown("""
    * *Forth Industrial Revolution (4IR) Capabilities and its Implications for Graduate Employment Opportunities*.
    * *PhD Thesis:* Advanced Survival Analysis utilizing Wearable Biomarker Data.
    """)

# --- PAGE 4: CONTACT ---
elif page == "Contact":
    st.title("📬 Get in Touch")
    
    st.write("I am available for academic collaboration, guest lecturing, and private consultation.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**📍 Office Address:**")
        st.write("""
        Faculty of Natural Sciences
        Department of Mathematics, Science & Computing
        Walter Sisulu University (NMD Campus)
        Private Bag X1, Mthatha
        """)
        
    with col2:
        st.markdown("**📧 Contact Details:**")
        st.write("📧 ijubane@wsu.ac.za")
        st.write("📧 lonkosi@gmail.com")
        st.markdown("🔗 [LinkedIn Profile](https://www.linkedin.com/in/ido-jubane-b2150586)")