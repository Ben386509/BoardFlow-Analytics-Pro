import streamlit as st
import os
import plotly.express as px
import pandas as pd
import time

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(
    page_title="BoardFlow Pro",
    page_icon="📌",
    layout="wide"
)

# ------------------------------
# SESSION STATE
# ------------------------------
if "authorized" not in st.session_state:
    st.session_state.authorized = False

if "page" not in st.session_state:
    st.session_state.page = "Home"

# ------------------------------
# STYLING
# ------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    color: white;
    font-family: 'Inter', sans-serif;
}

/* Glass card */
.glass-card {
    background: rgba(30, 41, 59, 0.85);
    border-radius: 20px;
    padding: 40px;
    margin-bottom: 20px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    border: 1px solid rgba(255,255,255,0.08);
    text-align: center;
}

/* Buttons */
.stButton>button {
    background: #ec4899;
    color: white;
    border-radius: 10px;
    padding: 12px 28px;
    font-weight: 600;
    width: 100%;
    transition: 0.2s;
}
.stButton>button:hover {
    background: #db2777;
    transform: scale(1.02);
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# SIDEBAR NAVIGATION
# ------------------------------
with st.sidebar:
    st.title("📌 BoardFlow Pro")
    page = st.radio("Navigation", ["Home", "Dashboard", "Privacy Policy"])
    st.divider()
    st.caption("© 2026 BoardFlow Digital")
    st.session_state.page = page

# ------------------------------
# HOME PAGE
# ------------------------------
if st.session_state.page == "Home":

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.title("BoardFlow Pro")
    st.markdown("##### Professional Pinterest Business Intelligence")
    st.divider()

    CLIENT_ID = os.environ.get("PINTEREST_CLIENT_ID")
    if not CLIENT_ID:
        st.warning("Developer Verification Mode")
        st.caption("OAuth will activate once credentials are configured.")
    else:
        if st.button("Authorize Pinterest Account"):
            st.session_state.authorized = True
            st.success("Authorization initiated.")

    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.authorized:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Dashboard Preview")
        col1, col2, col3 = st.columns(3)

        # Animated metric simulation
        metrics = {"Boards": 12, "Total Pins": 482, "Monthly Views": 124_000}
        deltas = {"Boards": 2, "Total Pins": 18, "Monthly Views": "5%"}
        for col, key in zip([col1, col2, col3], metrics.keys()):
            col.metric(label=key, value=metrics[key], delta=deltas[key])

        st.markdown('</div>', unsafe_allow_html=True)

        # Engagement Insights
        with st.expander("Engagement Insights"):
            st.write("• Top performing board: Modern Interiors")
            st.write("• Best posting time: 7PM – 9PM")
            st.write("• Pin save rate: 8.4%")

# ------------------------------
# DASHBOARD PAGE
# ------------------------------
elif st.session_state.page == "Dashboard":
    if not st.session_state.authorized:
        st.warning("You must authorize your Pinterest account first.")
        st.stop()

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.title("📊 Analytics Dashboard")

    # Sample Charts
    st.subheader("Monthly Views")
    df_views = pd.DataFrame({
        "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
        "Views": [80_000, 90_000, 95_000, 110_000, 120_000, 124_000]
    })
    fig_views = px.line(df_views, x="Month", y="Views", markers=True, template="plotly_dark")
    st.plotly_chart(fig_views, use_container_width=True)

    st.subheader("Pins per Board")
    df_pins = pd.DataFrame({
        "Board": ["Home Decor", "Fashion", "Travel", "Food", "Tech"],
        "Pins": [120, 85, 60, 50, 35]
    })
    fig_pins = px.bar(df_pins, x="Board", y="Pins", template="plotly_dark", color="Pins", color_continuous_scale=px.colors.sequential.Pinkyl)
    st.plotly_chart(fig_pins, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------
# PRIVACY PAGE
# ------------------------------
elif st.session_state.page == "Privacy Policy":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.title("🛡️ Privacy & Data Policy")

    st.markdown("""
### 1. Data Collection
BoardFlow uses official OAuth 2.0 protocols.  
We never access your password.

### 2. Data Usage
Only boards and pins you authorize are accessed.

### 3. Data Storage
No permanent external storage.

### 4. Revocation
You may revoke access anytime in Pinterest's Apps and Websites settings.
""")
    st.markdown('</div>', unsafe_allow_html=True)
