import streamlit as st

# Page Configuration
st.set_page_config(page_title="CBSE Class 10 Pro Portal 2026", layout="wide")

# Custom CSS for Visuals
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    .reportview-container .main .block-container{ padding-top: 2rem; }
    .card { padding: 20px; border-radius: 10px; background-color: white; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# App Title
st.title("🎓 CBSE Class 10 Ultimate Resource Portal (2026)")
st.info("Updated with 50% Competency-Based Weightage & New Exam Pattern")

# Sidebar Navigation
subject = st.sidebar.selectbox("Select Subject", ["Mathematics (Standard)", "Science", "Social Science", "English", "Hindi"])
resource_type = st.sidebar.radio("Resource Category", ["NCERT Solutions", "Past 5 Years Papers", "Competency Questions", "RealFeel Sample Papers"])

# --- SUBJECT DATA MAPPING ---
# In a real app, you would link these to PDF URLs or local files
data = {
    "Mathematics (Standard)": {
        "Competency": ["Case Study: Height & Distances in Real Life", "Assertion-Reason: Quadratic Equations", "Real-world Probability Models"],
        "PYQs": ["2025 Set 1/2/3", "2024 Set A", "2023 All Regions"],
        "Level": "Advanced (Standard)"
    },
    "Science": {
        "Competency": ["Data Interpretation: pH Scale", "Case Study: Modern Periodic Table", "Experimental Logic: Electricity"],
        "PYQs": ["2025 Board Paper", "2024 All Sets"],
        "Level": "Conceptual"
    }
}

# --- DYNAMIC CONTENT RENDERING ---

col1, col2 = st.columns([2, 1])

with col1:
    st.header(f"📚 {subject} - {resource_type}")
    
    if resource_type == "NCERT Solutions":
        st.write("### Chapter-wise Detailed Solutions")
        chapters = ["Real Numbers", "Polynomials", "Triangles", "Trigonometry"] if "Math" in subject else ["Chemical Reactions", "Life Processes"]
        for ch in chapters:
            with st.expander(f"Chapter: {ch}"):
                st.write(f"Detailed step-by-step solutions for {ch} as per NCERT 2026.")
                st.button(f"Download PDF for {ch}", key=ch)

    elif resource_type == "Past 5 Years Papers":
        st.write("### Previous Year Question Papers (With Answer Key)")
        years = ["2025", "2024", "2023", "2022", "2021"]
        for year in years:
            st.markdown(f"""<div class="card">
                <h4>Year {year} Board Examination</h4>
                <p>Includes Set 1, 2, and 3 with Official Marking Scheme.</p>
                <a href="#">Download Solution Set</a>
            </div>""", unsafe_allow_html=True)

    elif resource_type == "Competency Questions":
        st.warning("New Trend: 50% Weightage on Competency Questions")
        st.write("### Extra Practice for Standard Maths/Science")
        q_types = st.tabs(["Case Study", "Assertion-Reason", "MCQs (Application)"])
        
        with q_types[0]:
            st.subheader("Case Study Based Questions")
            st.write("**Scenario:** A bridge architect uses parabolic arches...")
            st.image("https://via.placeholder.com/600x300.png?text=Parabolic+Arch+Case+Study", caption="Real-world Math Application")
            st.selectbox("Difficulty Level", ["Basic", "Standard", "HOTS"], key="math_lvl")
        
        with q_types[1]:
            st.write("**Assertion:** Every composite number can be expressed as a product of primes.")
            st.write("**Reason:** The Fundamental Theorem of Arithmetic states uniqueness.")
            st.radio("Correct Option", ["A", "B", "C", "D"])

    elif resource_type == "RealFeel Sample Papers":
        st.success("Simulated Board Environment")
        st.write("### Sample Paper 2026 (Strictly as per CBSE Specimen)")
        st.markdown("""
        - **Section A:** 20 MCQs (1 Mark each)
        - **Section B:** 5 VSA (2 Marks each)
        - **Section E:** 3 Case Studies (4 Marks each)
        """)
        st.button("Start 3-Hour Timer & View Paper")

with col2:
    st.subheader("Exam Insights")
    st.progress(80, text="Syllabus Completion Guide")
    st.metric(label="Competency Focus", value="50%", delta="Increased from 2024")
    st.markdown("""
    **Preparation Tips:**
    - Focus on 'Why' not 'What'.
    - Practice Exemplar for Standard Maths.
    - Revise diagrams for Science.
    """)
