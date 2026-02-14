import streamlit as st

# --- 1. SETTINGS & THEME ---
st.set_page_config(page_title="BoardFlow Pro", page_icon="📌", layout="centered")

# Custom Apple-style CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { 
        font-family: 'Inter', sans-serif; 
        background-color: #f5f5f7; 
    }
    .main-card {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(20px);
        border-radius: 30px;
        padding: 40px;
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow: 0 20px 40px rgba(0,0,0,0.05);
    }
    .stButton>button {
        background: #0071e3; 
        color: white; 
        border-radius: 20px;
        width: 100%; 
        border: none; 
        padding: 10px; 
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. UI ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.title("BoardFlow")
st.write("Professional Pinterest Analytics & Automation")

st.divider()

col1, col2 = st.columns(2)
col1.metric("API Version", "v5.0")
col2.metric("Status", "Reviewing")

st.info("OAuth 2.0 connection is ready. Awaiting Client Secret from Pinterest.")

if st.button("Connect Pinterest Account"):
    st.write("Redirecting to secure OAuth portal...")

st.markdown('</div>', unsafe_allow_html=True)

# --- 3. FOOTER (Essential for Approval) ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size: 13px; color: gray;'>
    © 2026 BoardFlow Digital. 
    <a href="https://github.com/YOUR_USER/YOUR_REPO/blob/main/PRIVACY.md" target="_blank">
    Privacy Policy
    </a>
    </div>
    """,
    unsafe_allow_html=True
)
