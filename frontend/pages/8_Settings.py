import streamlit as st

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

from pathlib import Path

css_path = Path(__file__).parent.parent / "assets" / "style.css"

with open(css_path, encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- Login Check ----------------

if "logged_in" not in st.session_state:
    st.warning("Please Login First")
    st.switch_page("pages/2_Login.py")

user = st.session_state["user"]

# ---------------- Header ----------------

st.title("⚙️ Settings")

st.caption("Manage your Student Digital Brain preferences")

st.divider()

# ---------------- Profile ----------------

st.subheader("👤 Profile")

col1, col2 = st.columns(2)

with col1:
    st.text_input(
        "Name",
        value=user["name"],
        disabled=True
    )

with col2:
    st.text_input(
        "Email",
        value=user["email"],
        disabled=True
    )

st.divider()

# ---------------- App Preferences ----------------

st.subheader("🎨 App Preferences")

theme = st.selectbox(
    "Theme",
    ["Light", "Dark", "System Default"]
)

notifications = st.toggle(
    "🔔 Enable Notifications",
    value=True
)

study_reminder = st.toggle(
    "📅 Daily Study Reminder",
    value=True
)

ai_recommendation = st.toggle(
    "🤖 Enable AI Recommendation",
    value=True
)

st.divider()

# ---------------- Learning Preferences ----------------

st.subheader("📚 Learning Preferences")

learning_style = st.selectbox(
    "Preferred Learning Style",
    [
        "Visual",
        "Reading",
        "Practice Based",
        "Video Based"
    ]
)

difficulty = st.select_slider(
    "Difficulty Level",
    options=[
        "Easy",
        "Medium",
        "Hard"
    ],
    value="Medium"
)

st.divider()

# ---------------- About ----------------

st.subheader("ℹ️ About Student Digital Brain")

st.info("""
🧠 **Student Digital Brain v1.0**

**Frontend:** Streamlit

**Backend:** FastAPI

**Database:** PostgreSQL

**Machine Learning:** Random Forest

**Developer:** Navya Mangal
""")

st.divider()

# ---------------- Save Button ----------------

if st.button("💾 Save Settings", use_container_width=True):
    st.success("Settings Saved Successfully ✅")

# ---------------- Logout ----------------

if st.button("🚪 Logout", use_container_width=True):
    st.session_state.clear()
    st.success("Logged Out Successfully")
    st.switch_page("pages/2_Login.py")

# ---------------- Footer ----------------

st.markdown("""
---
<div style="text-align:center;">
Made with ❤️ using <b>FastAPI • PostgreSQL • Streamlit • Machine Learning</b>
</div>
""", unsafe_allow_html=True)