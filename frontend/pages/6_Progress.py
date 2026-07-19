import streamlit as st

st.set_page_config(
    page_title="Progress",
    page_icon="📈",
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

st.title("📈 Learning Progress")

st.caption(f"Track your learning journey, {user['name']} 🚀")

st.divider()

# ---------------- Top Cards ----------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🔥 Study Streak", "5 Days")

with col2:
    st.metric("✅ Tasks Completed", "12")

with col3:
    st.metric("📚 Learning Score", "82%")

with col4:
    st.metric("🏆 Badges", "4")

st.divider()

# ---------------- Weekly Progress ----------------

st.subheader("📊 Weekly Progress")

st.progress(75)

st.write("**75% Weekly Goal Completed**")

st.divider()

# ---------------- Subject Progress ----------------

st.subheader("📚 Subject-wise Progress")

sub1, sub2 = st.columns(2)

with sub1:

    st.write("### 💻 Data Structures")

    st.progress(85)

    st.write("85% Completed")

    st.write("### 🗄 DBMS")

    st.progress(70)

    st.write("70% Completed")

with sub2:

    st.write("### 🌐 Computer Networks")

    st.progress(60)

    st.write("60% Completed")

    st.write("### ⚙ Operating System")

    st.progress(80)

    st.write("80% Completed")

st.divider()

# ---------------- Achievement ----------------

st.subheader("🏆 Recent Achievement")

st.success("🎉 Congratulations! You maintained a 5-day learning streak.")

st.divider()

# ---------------- AI Suggestion ----------------

st.subheader("🤖 AI Suggestion")

st.info("""
📌 Focus on **DBMS** this week.

✔ Revise SQL Queries

✔ Complete DBMS Notes

✔ Solve 5 Practice Questions
""")

st.divider()

# ---------------- Motivation ----------------

st.success("💡 Consistency beats intensity. Keep learning every day!")

# ---------------- Footer ----------------

st.markdown("""
---
<center>

Made with ❤️ using <b>FastAPI • PostgreSQL • Streamlit • Machine Learning</b>

</center>
""", unsafe_allow_html=True)