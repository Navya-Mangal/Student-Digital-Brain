import streamlit as st

st.set_page_config(
    page_title="Notes",
    page_icon="📝",
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

# ---------------- Session State ----------------

if "notes" not in st.session_state:
    st.session_state.notes = []

# ---------------- Header ----------------

st.title("📝 Study Notes")

st.caption("Create and organize your personal study notes.")

st.divider()

# ---------------- Input ----------------

title = st.text_input(
    "📌 Note Title",
    placeholder="Enter note title..."
)

note = st.text_area(
    "✍ Write Notes",
    height=220,
    placeholder="Write your notes here..."
)

# ---------------- Buttons ----------------

col1, col2 = st.columns(2)

with col1:

    if st.button("💾 Save Note", use_container_width=True):

        if title.strip() == "" or note.strip() == "":

            st.warning("Please enter both title and note.")

        else:

            st.session_state.notes.append({
                "title": title,
                "content": note
            })

            st.success("✅ Note Saved Successfully")

            st.rerun()

with col2:

    if st.button("🗑 Clear All Notes", use_container_width=True):

        st.session_state.notes.clear()

        st.success("All Notes Deleted")

        st.rerun()

# ---------------- Saved Notes ----------------

st.divider()

st.subheader("📚 My Notes")

if len(st.session_state.notes) == 0:

    st.info("No Notes Added Yet.")

else:

    for i, n in enumerate(st.session_state.notes):

        with st.container():

            st.markdown(f"""
<div class="task-card">

<h3>📌 {n['title']}</h3>

<p>{n['content']}</p>

</div>
""", unsafe_allow_html=True)

            if st.button(
                "🗑 Delete",
                key=f"delete_{i}"
            ):

                st.session_state.notes.pop(i)

                st.success("Note Deleted Successfully")

                st.rerun()

# ---------------- Footer ----------------

st.markdown("---")

st.markdown(
    """
<div style="text-align:center;color:gray;">
🧠 Student Digital Brain • Notes Module
</div>
""",
    unsafe_allow_html=True
) 