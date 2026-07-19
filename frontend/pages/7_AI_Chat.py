import streamlit as st
from utils.api import recommend

st.set_page_config(
    page_title="AI Recommendation",
    page_icon="🤖",
    layout="wide"
)

from pathlib import Path

css_path = Path(__file__).parent.parent / "assets" / "style.css"

with open(css_path, encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🤖 AI Learning Recommendation")

st.write("Fill your details to get an AI Recommendation.")

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox("Gender", ["Male", "Female"])

    age = st.number_input("Age", 17, 30, 20)

    college_year = st.selectbox(
        "College Year",
        ["1st Year","2nd Year","3rd Year","4th Year"]
    )

    branch = st.selectbox(
        "Branch",
        ["CSE","AI","IT","ECE","EE","ME"]
    )

    cgpa = st.slider("CGPA",5.0,10.0,8.0)

    attendance = st.slider("Attendance %",50,100,80)

    study_hours = st.slider("Study Hours / Day",0.0,12.0,4.0)

    weekly_hours = st.slider("Weekly Study Hours",0.0,80.0,28.0)

    quiz = st.slider("Quiz Score",0.0,100.0,70.0)

    assignment = st.slider("Assignment Score",0.0,100.0,75.0)

    exam = st.slider("Exam Score",0.0,100.0,72.0)

with col2:

    coding = st.slider("Coding Score",0.0,100.0,65.0)

    problem = st.slider("Problem Solving",0.0,100.0,70.0)

    logical = st.slider("Logical Reasoning",0.0,100.0,72.0)

    communication = st.slider("Communication",0.0,100.0,75.0)

    notes = st.slider("Notes Completion %",0.0,100.0,60.0)

    revision = st.number_input("Revision Sessions",0,20,3)

    completed = st.number_input("Completed Tasks",0,100,10)

    pending = st.number_input("Pending Tasks",0,100,3)

    screen = st.slider("Daily Screen Time",0.0,15.0,5.0)

    social = st.slider("Social Media Hours",0.0,10.0,2.0)

    sleep = st.slider("Sleep Hours",0.0,12.0,7.0)

    stress = st.slider("Stress Level",0.0,10.0,4.0)

    focus = st.slider("Focus Level",0.0,10.0,8.0)

    motivation = st.slider("Motivation Level",0.0,10.0,8.0)

st.divider()

if st.button("✨ Generate Recommendation", use_container_width=True):

    data = {

        "gender": gender,
        "age": age,
        "college_year": college_year,
        "branch": branch,
        "cgpa": cgpa,
        "attendance_percentage": attendance,
        "study_hours_per_day": study_hours,
        "weekly_study_hours": weekly_hours,
        "quiz_score": quiz,
        "assignment_score": assignment,
        "exam_score": exam,
        "coding_score": coding,
        "problem_solving_score": problem,
        "logical_reasoning_score": logical,
        "communication_score": communication,
        "notes_completion_percentage": notes,
        "revision_sessions_per_week": revision,
        "tasks_completed": completed,
        "tasks_pending": pending,
        "daily_screen_time_hours": screen,
        "social_media_hours": social,
        "sleep_hours": sleep,
        "stress_level": stress,
        "focus_level": focus,
        "motivation_level": motivation

    }

    response = recommend(data)

    if response.status_code == 200:

        result = response.json()

        st.success("Recommendation Generated Successfully")

        st.markdown("## 🤖 AI Recommendation")

        st.info(result["recommendation"])

        st.write("### 📌 Reason")

        st.write(result["reason"])

        st.metric(
            "Confidence",
            result["confidence"]
        )

    else:

        st.error("Unable to generate recommendation.")