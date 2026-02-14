import streamlit as st
import pandas as pd

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(
    page_title="BoardFlow Pro",
    page_icon="📌",
    layout="wide"
)

# ------------------------------
# SESSION STATE ROUTER & AUTH
# ------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "authorized" not in st.session_state:
    st.session_state.authorized = False

# ------------------------------
# CSS STYLING (Apple/Amazon-like premium)
# ------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    color: #e0e0e0;
    font-family: 'Inter', sans-serif;
}

.glass-card {
    background: rgba(30, 41, 59, 0.9);
    border-radius: 24px;
    padding: 40px;
    margin-bottom: 30px;
    box-shadow: 0 25px 50px rgba(0,0,0,0.5);
    border: 1px solid rgba(255,255,255,0.08);
    text-align: center;
    transition: transform 0.2s ease;
}
.glass-card:hover {
    transform: scale(1.02);
}

.stButton>button {
    background: #ec4899;
    color: white;
    border-radius: 12px;
    padding: 14px 30px;
    font-weight: 600;
    width: 100%;
    transition: 0.3s ease;
}
.stButton>button:hover {
    background: #db2777;
    transform: scale(1.03);
}

hr {
    border: 1px solid rgba(255,255,255,0.1);
}

h1,h2,h3,h4,h5 {
    color: #f3f4f6;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# SIDEBAR NAVIGATION
# ------------------------------
with st.sidebar:
    st.title("📌 BoardFlow Pro")
    selection = st.radio("Navigation", ["Home", "Dashboard", "Privacy Policy"])
    st.session_state.page = selection
    st.divider()
    st.caption("© 2026 BoardFlow Digital")

# ------------------------------
# ROUTER / PAGE LOGIC
# ------------------------------
page = st.session_state.page

# ==============================
# HOME PAGE
# ==============================
if page == "Home":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.title("BoardFlow Pro")
    st.markdown("##### Professional Pinterest Business Intelligence")
    st.divider()

    if not st.session_state.authorized:
        if st.button("Authorize Pinterest Account"):
            st.session_state.authorized = True
            st.success("Authorization simulated (OAuth placeholder).")
    else:
        st.success("✅ Authorized!")
        col1, col2, col3 = st.columns(3)
        metrics = {"Boards": 12, "Pins": 482, "Monthly Views": 124_000}
        deltas = {"Boards": 2, "Pins": 18, "Monthly Views": "5%"}
        for col, key in zip([col1, col2, col3], metrics.keys()):
            col.metric(label=key, value=metrics[key], delta=deltas[key])
        
        st.divider()
        with st.expander("Engagement Insights"):
            st.write("• Top performing board: Modern Interiors")
            st.write("• Best posting time: 7PM – 9PM")
            st.write("• Pin save rate: 8.4%")

    if st.button("View Privacy Policy"):
        st.session_state.page = "privacy"

    st.markdown('</div>', unsafe_allow_html=True)

# ==============================
# DASHBOARD PAGE
# ==============================
elif page == "Dashboard":
    if not st.session_state.authorized:
        st.warning("You must authorize your Pinterest account first.")
        st.stop()

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.title("📊 Analytics Dashboard")

    # Pins Table
    st.subheader("Pins per Board")
    df_pins = pd.DataFrame({
        "Board": ["Home Decor", "Fashion", "Travel", "Food", "Tech"],
        "Pins": [120, 85, 60, 50, 35]
    })
    st.table(df_pins)

    # Monthly Views Chart
    st.subheader("Monthly Views")
    df_views = pd.DataFrame({
        "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
        "Views": [80_000, 90_000, 95_000, 110_000, 120_000, 124_000]
    })
    st.line_chart(df_views.set_index("Month"))

    st.markdown('</div>', unsafe_allow_html=True)

# ==============================
# PRIVACY POLICY PAGE
# ==============================
elif page == "privacy":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.title("🛡️ Privacy & Data Policy")

    st.markdown("""
### 1. Data Collection
BoardFlow uses official OAuth 2.0 protocols.  
We never access your Pinterest password.

### 2. Data Usage
Only boards and pins you authorize are accessed.

### 3. Data Storage
No permanent external storage. Processing occurs in your active session.

### 4. Revocation
You may revoke access anytime via Pinterest's Apps and Websites settings.
""")

    # Back button
    if st.button("← Back to Home"):
        st.session_state.page = "Home"

    st.markdown('</div>', unsafe_allow_html=True)
