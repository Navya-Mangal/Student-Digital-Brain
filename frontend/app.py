import streamlit as st

st.set_page_config(
    page_title="Student Digital Brain",
    page_icon="🧠",
    layout="wide"
)

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
# 🧠 Student Digital Brain

### AI Powered Personalized Learning Platform
""")

st.write(
"""
Manage your studies, organize tasks, track progress and get AI-powered learning recommendations.
"""
)

st.markdown("---")

st.subheader("🚀 Features")

col1,col2,col3=st.columns(3)

with col1:

    st.markdown("""
<div class="feature-card">

<h3>📚 Smart Task Manager</h3>

Organize daily study tasks.

</div>
""",unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="feature-card">

<h3>📈 Progress Tracker</h3>

Track learning progress.

</div>
""",unsafe_allow_html=True)

with col3:

    st.markdown("""
<div class="feature-card">

<h3>🤖 AI Assistant</h3>

Personalized recommendations.

</div>
""",unsafe_allow_html=True)

st.markdown("---")

st.success("👉 Use the left sidebar to explore all modules.")