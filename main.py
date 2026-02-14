import streamlit as st
import os

# -------------------------------
# CONFIG (MUST BE FIRST)
# -------------------------------
st.set_page_config(
    page_title="BoardFlow Pro",
    page_icon="📌",
    layout="centered"
)

# -------------------------------
# SESSION STATE INIT
# -------------------------------
if "authorized" not in st.session_state:
    st.session_state.authorized = False

# -------------------------------
# CUSTOM CSS
# -------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #f5f7fa 0%, #dfe9f3 100%);
}

.glass-card {
    background: rgba(255, 255, 255, 0.75);
    backdrop-filter: blur(20px);
    border-radius: 24px;
    border: 1px solid rgba(255,255,255,0.4);
    padding: 45px;
    box-shadow: 0 25px 50px rgba(0,0,0,0.08);
    text-align: center;
}

.status-badge {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 0.8rem;
    font-weight: 600;
}

.status-standby {
    background: #fff4e5;
    color: #b26a00;
}

.status-active {
    background: #e6f7ed;
    color: #0a7a32;
}

.stButton>button {
    background: black;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 12px 28px;
    font-weight: 600;
    transition: 0.3s ease;
}

.stButton>button:hover {
    transform: scale(1.02);
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# SIDEBAR NAVIGATION
# -------------------------------
with st.sidebar:
    st.title("📌 BoardFlow")
    page = st.radio("Navigation", ["Home", "Dashboard", "Privacy Policy"])
    st.divider()
    st.caption("© 2026 BoardFlow Digital")

# -------------------------------
# HOME PAGE
# -------------------------------
if page == "Home":

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.title("BoardFlow Pro")
    st.markdown("#### Professional Pinterest Business Intelligence")

    st.divider()

    CLIENT_ID = os.environ.get("PINTEREST_CLIENT_ID")

    if not CLIENT_ID:
        st.markdown(
            '<span class="status-badge status-standby">Developer Verification Mode</span>',
            unsafe_allow_html=True
        )
        st.write("")
        st.info("Pinterest V5 API connection is currently in standby mode.")
        st.caption("Secure OAuth 2.0 gateway will activate once credentials are configured.")
    else:
        st.markdown(
            '<span class="status-badge status-active">System Active</span>',
            unsafe_allow_html=True
        )
        st.write("")
        if st.button("Authorize Pinterest Account"):
            st.session_state.authorized = True
            st.success("Authorization flow initiated (OAuth redirect placeholder)")

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# DASHBOARD PAGE
# -------------------------------
elif page == "Dashboard":

    st.title("📊 Analytics Dashboard")

    if not st.session_state.authorized:
        st.warning("You must authorize your Pinterest account first.")
        st.stop()

    st.success("Connected Successfully")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Boards", "12", "+2")

    with col2:
        st.metric("Total Pins", "482", "+18")

    with col3:
        st.metric("Monthly Views", "124K", "+5%")

    st.divider()

    with st.expander("Engagement Insights"):
        st.write("• Top performing board: *Modern Interiors*")
        st.write("• Best posting time: 7PM – 9PM")
        st.write("• Pin save rate: 8.4%")

# -------------------------------
# PRIVACY PAGE
# -------------------------------
elif page == "Privacy Policy":

    st.title("🛡️ Privacy & Data Policy")

    st.markdown("""
### 1. Data Collection
BoardFlow connects via official OAuth 2.0 protocols.  
We never see or store your Pinterest password.

### 2. Data Usage
Only boards and pins you authorize are accessed.  
Data is used exclusively for analytics generation.

### 3. Data Storage
No permanent external storage.  
Processing occurs within encrypted active sessions.

### 4. Revocation
Access can be revoked anytime from Pinterest's "Apps and Websites" settings.
""")
