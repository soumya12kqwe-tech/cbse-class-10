import streamlit as st
from gtts import gTTS
from io import BytesIO

# --- PAGE CONFIG ---
st.set_page_config(page_title="Class 12 Chem Pro 2026", layout="wide")

# --- AUDIO GENERATOR FUNCTION ---
def get_audio(text):
    tts = gTTS(text=text, lang='en')
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    return audio_fp

# --- APP TITLE ---
st.title("🧪 CBSE Class 12 Chemistry (2026 Trend)")
st.markdown("---")

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Select Chapter")
chapter = st.sidebar.selectbox("Chapters", [
    "1. Solutions", 
    "2. Electrochemistry", 
    "3. Chemical Kinetics",
    "4. d & f Block Elements",
    "5. Coordination Compounds",
    "6. Haloalkanes & Haloarenes",
    "7. Alcohols, Phenols & Ethers",
    "8. Aldehydes, Ketones & Carboxylic Acids",
    "9. Amines",
    "10. Biomolecules"
])

# --- DATA FOR CONTENT ---
# We use a dictionary to store 'Real Life' summaries for Audio
chapter_data = {
    "1. Solutions": {
        "audio_text": "In Solutions, focus on Raoult's Law and Colligative properties. The 2026 trend shows 3-mark questions on Van't Hoff factor. Remember, abnormal molar mass occurs due to association or dissociation.",
        "weightage": "7 Marks",
        "key_formula": r"P_1 = P_1^0 \chi_1"
    },
    "2. Electrochemistry": {
        "audio_text": "Electrochemistry is the highest weightage chapter. Master the Nernst Equation and Kohlrausch Law. 2026 papers often include case studies on Fuel Cells and Corrosion.",
        "weightage": "9 Marks",
        "key_formula": r"E_{cell} = E^0_{cell} - \frac{0.059}{n} \log Q"
    }
}

# --- DYNAMIC PAGE CONTENT ---
col1, col2 = st.columns([2, 1])

with col1:
    st.header(chapter)
    st.info(f"Exam Weightage: {chapter_data.get(chapter, {}).get('weightage', 'TBD')}")
    
    # AUDIO REVISION BUTTON
    st.subheader("🔊 Quick Audio Revision")
    if st.button("Listen to Summary"):
        summary_text = chapter_data.get(chapter, {}).get('audio_text', "Content coming soon.")
        audio_file = get_audio(summary_text)
        st.audio(audio_file, format='audio/mp3')

    # NCERT SOLUTIONS & PYQ SECTION
    tab_n, tab_p, tab_c = st.tabs(["NCERT Solutions", "Past 5 Years", "Competency Lab"])
    
    with tab_n:
        st.write("Click below to download Step-by-Step NCERT Solutions for 2026.")
        st.button(f"📥 Download {chapter} PDF")

    with tab_p:
        st.write("### Past 5 Years Trends (2021-2025)")
        st.write("- 2025: Focus on Numericals from this chapter.")
        st.write("- 2024: 1 MCQ and 1 Long Answer (5 Marks).")

with col2:
    st.subheader("Formula / Concept Box")
    st.latex(chapter_data.get(chapter, {}).get('key_formula', ''))
    
    st.warning("🎯 2026 Tip: 50% of the paper is Competency Based. Don't just cram; understand the 'Why'!")
