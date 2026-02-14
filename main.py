import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="BoardFlow | Pro Analytics",
    page_icon="📌",
    layout="centered"
)

# --- SECURE CONFIG LOADING (Cloud + Local Compatible) ---
CLIENT_ID = st.secrets.get(
    "PINTEREST_CLIENT_ID",
    os.environ.get("PINTEREST_CLIENT_ID")
)

# --- APPLE-INSPIRED CUSTOM CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

.stApp {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    font-family: 'Inter', sans-serif;
}

.glass-card {
    background: rgba(255, 255, 255, 0.75);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border-radius: 28px;
    border: 1px solid rgba(255, 255, 255, 0.4);
    padding: 42px;
    box-shadow: 0 25px 50px rgba(0,0,0,0.06);
    text-align: center;
    margin-top: 60px;
}

h1 {
    color: #1d1d1f;
    font-weight: 600;
    letter-spacing: -0.5px;
}

p {
    color: #6e6e73;
}

.stButton>button {
    background: #000000;
    color: #ffffff;
    border-radius: 14px;
    border: none;
    padding: 12px 28px;
    font-weight: 600;
    width: 100%;
    transition: all 0.25s ease;
}

.stButton>button:hover {
    background: #2c2c2e;
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

# --- MAIN UI ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.title("BoardFlow")
st.caption("Professional Pinterest Business Intelligence")

st.divider()

if not CLIENT_ID:
    st.info("System Status: Developer Verification Mode")
    st.write(
        "The Pinterest v5 API connection is currently in standby. "
        "OAuth 2.0 authorisation will initialise once valid credentials "
        "have been configured."
    )
else:
    st.success("System Status: Active")
    if st.button("Authorise via Pinterest"):
        st.write("Redirecting to secure Pinterest authentication...")

st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size: 0.8rem; color: #6e6e73;'>
        © 2026 BoardFlow Digital. Built for Pinterest Developers.<br>
        <a href='https://github.com/YOUR_USER/YOUR_REPO/blob/main/PRIVACY.md' 
           target='_blank' 
           style='text-decoration:none;'>
           Privacy Policy
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
