# Learning Git 


import streamlit as st
import ollama

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Study AI",
    page_icon="🤖",
    layout="centered"
)

# -------------------------
# Custom Styling (Glassmorphism & Dark Mode)
# -------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

    /* Global Font Override */
    html, body, [class*="css"], .stApp {
        font-family: 'Outfit', sans-serif !important;
    }

    /* Background styling: Deep Matte Black with dark grey glow */
    [data-testid="stAppViewContainer"] {
        background-color: #0c0c0c !important;
        background-image: 
            radial-gradient(at 0% 0%, rgba(82, 82, 91, 0.15) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(38, 38, 38, 0.15) 0px, transparent 50%) !important;
        background-attachment: fixed !important;
    }

    /* Header transparent glass styling */
    [data-testid="stHeader"] {
        background: rgba(12, 12, 12, 0.6) !important;
        backdrop-filter: blur(12px) !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
    }

    /* Sidebar glassmorphic styling */
    [data-testid="stSidebar"] {
        background: rgba(23, 23, 23, 0.8) !important;
        backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.04) !important;
    }

    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        color: #d4d4d4 !important;
    }

    /* Custom Gradient Title (Charcoal to Silver/White) */
    h1 {
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        background: linear-gradient(135deg, #ffffff 0%, #a3a3a3 60%, #525252 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        margin-bottom: 0px !important;
    }

    /* Subheadings styling */
    h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif !important;
        font-weight: 600 !important;
        color: #f5f5f5 !important;
    }

    /* Caption styling */
    div[data-testid="stCaptionContainer"] {
        color: #737373 !important;
        font-size: 14px !important;
        margin-top: -8px !important;
        margin-bottom: 24px !important;
    }

    /* Text inputs */
    div[data-testid="stTextInput"] label {
        font-weight: 500 !important;
        color: #a3a3a3 !important;
        font-size: 15px !important;
    }

    div[data-testid="stTextInput"] input {
        background-color: rgba(38, 38, 38, 0.4) !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        border-radius: 12px !important;
        color: #e5e5e5 !important;
        padding: 12px 16px !important;
        font-size: 15px !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(8px) !important;
    }

    div[data-testid="stTextInput"] input:focus {
        border-color: #737373 !important;
        box-shadow: 0 0 0 3px rgba(115, 115, 115, 0.25) !important;
        background-color: rgba(38, 38, 38, 0.6) !important;
    }

    /* Button: Generate Notes (Black/Charcoal with Silver glow on hover) */
    div[data-testid="stButton"] button {
        background: #171717 !important;
        border: 1px solid #404040 !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        padding: 12px 24px !important;
        border-radius: 12px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 14px 0 rgba(0, 0, 0, 0.5) !important;
        width: 100% !important;
    }

    div[data-testid="stButton"] button:hover {
        transform: translateY(-2px) !important;
        background: #262626 !important;
        border-color: #737373 !important;
        box-shadow: 0 6px 20px 0 rgba(255, 255, 255, 0.05) !important;
    }

    div[data-testid="stButton"] button:active {
        transform: translateY(0) !important;
    }

    /* Button: Download Notes */
    div[data-testid="stDownloadButton"] button {
        background: rgba(23, 23, 23, 0.3) !important;
        border: 1px solid rgba(163, 163, 163, 0.4) !important;
        color: #e5e5e5 !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        padding: 12px 24px !important;
        border-radius: 12px !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        backdrop-filter: blur(8px) !important;
    }

    div[data-testid="stDownloadButton"] button:hover {
        background: rgba(255, 255, 255, 0.05) !important;
        border-color: #ffffff !important;
        box-shadow: 0 4px 12px 0 rgba(255, 255, 255, 0.05) !important;
        transform: translateY(-1px) !important;
    }

    /* Container for generated notes */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(23, 23, 23, 0.4) !important;
        backdrop-filter: blur(16px) !important;
        border: 1px solid rgba(255, 255, 255, 0.04) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        margin-top: 24px !important;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.6) !important;
    }

    /* Sidebar Divider & list tweaks */
    hr {
        border-color: rgba(255, 255, 255, 0.05) !important;
    }
    
    /* Code blocks formatting */
    code {
        background: rgba(23, 23, 23, 0.8) !important;
        color: #e5e5e5 !important;
        border-radius: 6px !important;
        padding: 2px 6px !important;
        font-family: monospace !important;
        font-size: 14px !important;
    }
    
    pre code {
        display: block !important;
        padding: 12px !important;
        overflow-x: auto !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------
# Header
# -------------------------
# -------------------------
# Header with SVG Robot Logo
# -------------------------
st.markdown(
    """
<div style="display: flex; align-items: center; gap: 18px; margin-bottom: 28px; margin-top: 10px;">
<svg width="58" height="58" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(0 0 12px rgba(255,255,255,0.18));">
<!-- Antenna -->
<rect x="11.25" y="1" width="1.5" height="4" rx="0.75" fill="#a3a3a3"/>
<circle cx="12" cy="1.5" r="1.5" fill="#ffffff"/>
<!-- Head -->
<rect x="4" y="5" width="16" height="12" rx="3" fill="#171717" stroke="#404040" stroke-width="1.5"/>
<!-- Eyes -->
<circle cx="8.5" cy="10.5" r="1.5" fill="#ffffff"/>
<circle cx="15.5" cy="10.5" r="1.5" fill="#ffffff"/>
<!-- Ears -->
<rect x="2.5" y="9" width="1.5" height="4" rx="0.75" fill="#404040"/>
<rect x="20" y="9" width="1.5" height="4" rx="0.75" fill="#404040"/>
<!-- Mouth -->
<path d="M8 14H16" stroke="#a3a3a3" stroke-width="1.5" stroke-linecap="round"/>
<!-- Neck -->
<rect x="10" y="17" width="4" height="1.5" fill="#262626"/>
<!-- Body -->
<path d="M6 18.5H18L19 23H5L6 18.5Z" fill="#171717" stroke="#404040" stroke-width="1.5"/>
</svg>
<div>
<h1 style="margin: 0; font-family: 'Outfit', sans-serif; font-weight: 700; font-size: 2.6rem; line-height: 1.1; background: linear-gradient(135deg, #ffffff 0%, #a3a3a3 60%, #525252 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; border: none !important; box-shadow: none !important; box-decoration-break: clone !important;">Study AI</h1>
<p style="margin: 2px 0 0 0; color: #737373; font-size: 13.5px; font-weight: 500; font-family: 'Outfit', sans-serif; letter-spacing: 0.5px;">Powered by Ollama + Gemma 3</p>
</div>
</div>
""",
    unsafe_allow_html=True
)

# -------------------------
# Sidebar
# -------------------------
with st.sidebar:
    st.header("📖 About")
    st.write(
        """
        Generate concise study notes on any topic using a local LLM
        powered by Ollama and Gemma 3.
        """
    )

    st.markdown("---")

    st.write("### Features")
    st.write("✅ AI-generated notes")
    st.write("✅ Download notes")
    st.write("✅ Runs locally")
    st.write("✅ Powered by Ollama")

# -------------------------
# Input
# -------------------------
topic = st.text_input(
    "Enter a topic",
    placeholder="Example: Machine Learning"
)

# -------------------------
# Generate Button
# -------------------------
if st.button("Generate Notes", use_container_width=True):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        with st.spinner("Generating notes..."):

            response = ollama.chat(
                model="gemma3:1b",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
Write concise study notes about {topic}.

Format:
1. Definition
2. Key Points
3. Examples
4. Summary

Keep the notes easy to understand.
"""
                    }
                ]
            )

        notes = response["message"]["content"]

        st.success("Notes generated successfully!")

        st.subheader("📚 Study Notes")

        with st.container(border=True):
            st.markdown(notes)

        st.download_button(
            label="📥 Download Notes",
            data=notes,
            file_name=f"{topic}_notes.txt",
            mime="text/plain",
            use_container_width=True
        )

# -------------------------
# Footer
# -------------------------
st.divider()

st.caption(
    "Built using Streamlit, Ollama and Gemma 3"
)
