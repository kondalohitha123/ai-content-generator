import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader
from docx import Document
from PIL import Image
import os

# Page configuration
st.set_page_config(page_title="AI Content Writing Platform", layout="wide")

st.title("🚀 AI Social Media Content Generator")
st.markdown("Generate tailored social media campaign schedules for specific industries with custom reference contexts.")

# Configure API Key securely
api_key = st.sidebar.text_input("Gemini API Key", type="password", value=os.environ.get("GEMINI_API_KEY", ""))

if not api_key:
    st.info("Please enter your Gemini API Key in the sidebar or set it in your environment to continue.")
    st.stop()

genai.configure(api_key=api_key)

# 1. Industry Selection
st.subheader("1. Industry Selection")
industry = st.selectbox(
    "Select target industry:",
    ["Real Estate", "Jewellery", "Product - Perfume", "FMCG - Food"]
)

# Industry tone mapping instructions
INDUSTRY_PROMPTS = {
    "Real Estate": "Focus on property value, lifestyle benefits, location highlights, investment potential, trust, and luxury appeal.",
    "Jewellery": "Focus on elegance, craftsmanship, emotion, celebration, heritage, luxury, and premium aesthetics.",
    "Product - Perfume": "Focus on sensory descriptions, elegance, mood, scent notes, individuality, and personal attraction.",
    "FMCG - Food": "Focus on taste, freshness, quality ingredients, convenience, appetite appeal, and everyday enjoyment."
}

# 2. Content Duration & Quantity
st.subheader("2. Content Duration & Quantity")
plan = st.radio(
    "Select plan duration:",
    options=["1 Week (3 Posts)", "2 Weeks (6 Posts)", "1 Month (12 Posts)"]
)

PLAN_MAPPING = {
    "1 Week (3 Posts)": 3,
    "2 Weeks (6 Posts)": 6,
    "1 Month (12 Posts)": 12
}
num_posts = PLAN_MAPPING[plan]

# 3. Reference File Upload
st.subheader("3. Reference File Upload")
uploaded_files = st.file_uploader(
    "Upload reference files for context (PDF, DOCX, TXT, Images):",
    type=["pdf", "docx", "txt", "png", "jpg", "jpeg"],
    accept_multiple_files=True
)

reference_text = ""
if uploaded_files:
    for file in uploaded_files:
        filename = file.name.lower()
        if filename.endswith(".pdf"):
            reader = PdfReader(file)
            for page in reader.pages:
                reference_text += page.extract_text() or ""
        elif filename.endswith(".docx"):
            doc = Document(file)
            for p in doc.paragraphs:
                reference_text += p.text + "\n"
        elif filename.endswith(".txt"):
            reference_text += file.read().decode("utf-8") + "\n"
        elif filename.endswith((".png", ".jpg", ".jpeg")):
            reference_text += f"[Image File Uploaded: {file.name}]\n"

# 4. Content Generation
st.subheader("4. Generate Content")

if st.button("Generate Content", type="primary"):
    with st.spinner("Creating social media campaign schedule..."):
        prompt = f"""
        Act as an expert social media strategist and content developer.
        
        Industry: {industry}
        Strategy Context: {INDUSTRY_PROMPTS[industry]}
        Total Posts Required: {num_posts}
        
        Additional Reference Context Provided by User:
        {reference_text if reference_text else "No extra reference uploaded. Generate purely based on industry best practices."}
        
        Task:
        Generate exactly {num_posts} social media posts formatted strictly as follows for each post:
        
        ---
        ### Post [Number]
        **Date / Timeline:** [e.g. Day 1 / Week 1, Day 3, etc.]
        **Post Caption:** [Write a complete, high-converting social media caption with relevant hashtags and emojis appropriate for the {industry} industry]
        **Image Caption / Visual Direction:** [Detailed visual description of what image or graphic should be designed/used for this post]
        ---
        """
        
        try:
            model = genai.GenerativeModel("gemini-3.6-flash")
            response = model.generate_content(prompt)
            
            st.success("Content Plan Generated Successfully!")
            st.markdown("### 5. Content Output Plan")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error generating content: {e}")