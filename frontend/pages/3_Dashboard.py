import streamlit as st
from utils.api import dashboard
from datetime import datetime

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
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

# ---------------- Sidebar ----------------

st.sidebar.markdown("""
# 🧠 Student Digital Brain

### AI Learning Platform

---
""")

st.sidebar.success("🟢 Online")

st.sidebar.write(f"👤 **{user['name']}**")
st.sidebar.caption(user["email"])

st.sidebar.divider()

st.sidebar.success("🎓 Keep Learning Every Day")

if st.sidebar.button("🚪 Logout", use_container_width=True):
    st.session_state.clear()
    st.switch_page("pages/2_Login.py")

# ---------------- Header ----------------

today = datetime.now().strftime("%d %b %Y")

col1, col2 = st.columns([4,1])

with col1:

    st.markdown(f"""
# 👋 Welcome, {user['name']}

### Let's make today productive 🚀
""")

with col2:

    st.info(f"📅 {today}")

# ---------------- Dashboard API ----------------

with st.spinner("Loading Dashboard..."):
    response = dashboard()

if response.status_code == 200:

    data = response.json()

    st.divider()

    # ---------------- Stats Cards ----------------

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.markdown(f"""
<div class="dashboard-card">

<div class="card-icon">📚</div>

<div class="card-title">

Total Tasks

</div>

<div class="card-value">

{data['total_tasks']}

</div>

</div>
""", unsafe_allow_html=True)

    with c2:

        st.markdown(f"""
<div class="dashboard-card">

<div class="card-icon">✅</div>

<div class="card-title">

Completed

</div>

<div class="card-value">

{data['completed_tasks']}

</div>

</div>
""", unsafe_allow_html=True)

    with c3:

        st.markdown(f"""
<div class="dashboard-card">

<div class="card-icon">⏳</div>

<div class="card-title">

Pending

</div>

<div class="card-value">

{data['pending_tasks']}

</div>

</div>
""", unsafe_allow_html=True)

    with c4:

        st.markdown("""
<div class="dashboard-card">

<div class="card-icon">🔥</div>

<div class="card-title">

Learning Streak

</div>

<div class="card-value">

5 Days

</div>

</div>
""", unsafe_allow_html=True)

    st.divider()

    left, right = st.columns([2,1])

    # ---------------- LEFT ----------------

    with left:

        st.markdown(f"""
<div class="goal-card">

<h2>🎯 Today's Goal</h2>

<p>{data['today_goal']}</p>

</div>
""", unsafe_allow_html=True)

        st.write("")

        st.subheader("💡 Daily Motivation")

        st.success(
            "Small progress every day leads to big success."
        )
            # ---------------- RIGHT ----------------

    with right:

        st.markdown("""
<div class="ai-card">

<h2>🤖 Today's AI Recommendation</h2>

<h4>💻 Practice Coding</h4>

<p>
Your recent learning activity suggests that practicing coding
will improve your overall performance.
</p>

<hr>

<b>Today's Plan</b>

<ul>

<li>✅ Solve 3 Coding Questions</li>

<li>📘 Revise DBMS Notes</li>

<li>🎯 Complete Pending Task</li>

</ul>

</div>
""", unsafe_allow_html=True)

        st.write("")

        st.info("🔥 Current Learning Streak : 5 Days")

    # ---------------- Student Profile ----------------

    st.divider()

    st.subheader("👤 Student Profile")

    p1, p2, p3 = st.columns(3)

    with p1:
        st.metric("Student", user["name"])

    with p2:
        st.metric("Status", "Active ✅")

    with p3:
        st.metric("Learning Level", "Intermediate")

    st.write(f"📧 **Email :** {user['email']}")

    # ---------------- Weekly Progress ----------------

    st.divider()

    st.subheader("📈 Weekly Progress")

    st.progress(70)

    st.write("**70% Weekly Goal Completed**")

    st.divider()

    # ---------------- Quick Actions ----------------

    st.subheader("⚡ Quick Actions")

    a1, a2, a3 = st.columns(3)

    with a1:
        if st.button("➕ Add Task", use_container_width=True):
            st.switch_page("pages/4_Tasks.py")

    with a2:
        if st.button("📝 Notes", use_container_width=True):
            st.switch_page("pages/5_Notes.py")

    with a3:
        if st.button("🤖 AI Recommendation", use_container_width=True):
            st.switch_page("pages/7_AI_Chat.py")

    st.divider()

    # ---------------- Quote ----------------

    st.markdown("""
<div class="feature-card">

<h3>💡 Quote of the Day</h3>

<p style="font-size:18px;">
Success is the sum of small efforts repeated every day.
</p>

</div>
""", unsafe_allow_html=True)

    st.divider()

    # ---------------- Footer ----------------

    st.markdown("""
<div class="footer">

<hr>

<h4>🧠 Student Digital Brain v1.0</h4>

<p>
Built with ❤️ using FastAPI • PostgreSQL • Streamlit • Machine Learning
</p>

</div>
""", unsafe_allow_html=True)

else:

    st.error("Unable to load dashboard data.")