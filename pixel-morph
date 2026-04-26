import streamlit as st
from PIL import Image
import io

# 1. Page Config
st.set_page_config(page_title="PixelMorph Utility", page_icon="🖼️")

# 2. Vibrant Styling
st.markdown("""
    <style>
    .stApp { background: #0e1117; color: #00ffcc; }
    section[data-testid="stSidebar"] { background-color: #1a1c24; }
    .stButton>button { 
        background: linear-gradient(45deg, #00f2fe, #4facfe); 
        color: white; border: none; border-radius: 10px; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🖼️ PixelMorph: Image Utility")
st.write("Upload an image to resize, flip, or convert formats instantly.")

# 3. Sidebar Settings
st.sidebar.header("⚙️ Transformation Settings")
format_choice = st.sidebar.selectbox("Convert to:", ["PNG", "JPEG", "WebP"])
resize_factor = st.sidebar.slider("Resize %", 10, 200, 100)
rotate_choice = st.sidebar.degree_slider = st.sidebar.slider("Rotate Degrees", 0, 360, 0)

# 4. Main Upload Logic
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:
    # Open Image
    img = Image.open(uploaded_file)
    
    # Apply Transformations
    if rotate_choice != 0:
        img = img.rotate(rotate_choice)
    
    if resize_factor != 100:
        new_size = (int(img.width * resize_factor/100), int(img.height * resize_factor/100))
        img = img.resize(new_size)

    # Show Preview
    st.image(img, caption="Preview of Changes", use_container_width=True)

    # 5. Export Logic
    buf = io.BytesIO()
    img.save(buf, format=format_choice)
    byte_im = buf.getvalue()

    st.download_button(
        label=f"🚀 Download as {format_choice}",
        data=byte_im,
        file_name=f"converted_image.{format_choice.lower()}",
        mime=f"image/{format_choice.lower()}"
    )
    st.balloons()
else:
    st.info("Waiting for an image upload... Try dragging a photo here!")
