import streamlit as st

st.set_page_config(
    page_title="Privacy Policy | BoardFlow",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Privacy & Data Policy")

st.markdown("""
### 1. Data Collection
BoardFlow connects using official OAuth 2.0 protocols.  
We never store or see your Pinterest password.

### 2. Data Usage
We access only the boards and pins you explicitly authorize.  
Data is used strictly for analytics purposes.

### 3. Data Storage
We do not permanently store user data.  
Processing occurs within secure encrypted sessions.

### 4. Revocation
You may revoke access anytime via Pinterest's  
**Apps and Websites** settings.
""")

st.divider()

# 🔙 Back Link
st.page_link("Home.py", label="Back to Home", icon="←")
