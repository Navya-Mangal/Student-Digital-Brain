import streamlit as st
from utils.api import (
    add_task,
    get_tasks,
    complete_task,
    delete_task
)

st.set_page_config(
    page_title="Tasks",
    page_icon="📚",
    layout="wide"
)

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ---------------- Login Check ----------------

if "logged_in" not in st.session_state:
    st.warning("Please Login First")
    st.switch_page("pages/2_Login.py")

# ---------------- Sidebar ----------------

user = st.session_state["user"]

st.sidebar.title("🧠 Student Digital Brain")
st.sidebar.success("Task Management")

st.sidebar.markdown("---")
st.sidebar.write(f"👤 {user['name']}")
st.sidebar.write(user["email"])

st.sidebar.markdown("---")

if st.sidebar.button("🚪 Logout"):
    st.session_state.clear()
    st.switch_page("pages/2_Login.py")

# ---------------- Title ----------------

st.title("📚 Study Tasks")

st.caption("Manage your daily learning tasks.")

st.divider()

# ---------------- Add Task ----------------

st.subheader("➕ Add New Task")

col1, col2 = st.columns(2)

with col1:

    title = st.text_input("Task Title")

    subject = st.selectbox(
        "Subject",
        [
            "DSA",
            "DBMS",
            "OS",
            "CN",
            "Python",
            "AI",
            "ML",
            "Other"
        ]
    )

with col2:

    priority = st.selectbox(
        "Priority",
        [
            "High",
            "Medium",
            "Low"
        ]
    )

    deadline = st.text_input("Deadline")

if st.button("➕ Add Task"):

    response = add_task({

        "title": title,
        "subject": subject,
        "priority": priority,
        "deadline": deadline

    })

    if response.status_code == 200:

        st.success("Task Added Successfully")

        st.rerun()

st.divider()

# ---------------- Show Tasks ----------------

st.subheader("📋 Your Tasks")

response = get_tasks()

if response.status_code == 200:

    tasks = response.json()["tasks"]

    if len(tasks)==0:

        st.info("No Tasks Added Yet")

    else:

        for task in tasks:

            priority_color = {

                "High":"🔴",

                "Medium":"🟡",

                "Low":"🟢"

            }

            with st.container():

                st.markdown(f"""
<div class="task-card">

### 📘 {task['title']}

**Subject :** {task['subject']}

**Priority :** {priority_color[task['priority']]} {task['priority']}

**Deadline :** {task['deadline']}

**Status :** {task['status']}

</div>

""",unsafe_allow_html=True)

                col1,col2,col3=st.columns([5,1,1])

                with col2:

                    if st.button(
                        "✅",
                        key=f"complete{task['id']}"
                    ):

                        complete_task(task["id"])

                        st.rerun()

                with col3:

                    if st.button(
                        "🗑",
                        key=f"delete{task['id']}"
                    ):

                        delete_task(task["id"])

                        st.rerun()

else:

    st.error("Unable to fetch tasks.")