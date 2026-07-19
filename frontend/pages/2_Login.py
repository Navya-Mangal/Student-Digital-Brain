import streamlit as st
from utils.api import login

st.set_page_config(
    page_title="Student Digital Brain",
    page_icon="🧠",
    layout="wide"
)

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

left, right = st.columns([1.3,1], gap="large")

# ---------------- LEFT ----------------

with left:

    st.markdown("""
    <div style="margin-top:60px">

    <div class="hero-title">

    🧠 Student Digital Brain

    </div>

    <div class="hero-subtitle">

    AI Powered Personalized Learning Platform

    </div>

    <div class="feature">✨ Personalized Dashboard</div>

    <div class="feature">🤖 AI Recommendation System</div>

    <div class="feature">📈 Progress Analytics</div>

    <div class="feature">📅 Daily Learning Planner</div>

    <div class="feature">🏆 Smart Productivity Tracking</div>

    </div>

    """, unsafe_allow_html=True)

# ---------------- RIGHT ----------------

with right:

    st.markdown("""
    <div class="login-box">

    <h2 style="text-align:center;">
    Welcome Back 👋
    </h2>

    <p style="text-align:center;color:gray;">
    Login to continue
    </p>

    </div>
    """,unsafe_allow_html=True)

    email = st.text_input(
        "📧 Email",
        placeholder="Enter Email"
    )

    password = st.text_input(
        "🔒 Password",
        type="password",
        placeholder="Enter Password"
    )

    st.write("")

    if st.button("🚀 Login",use_container_width=True):

        if email=="" or password=="":

            st.warning("Please fill all fields.")

        else:

            response=login({

                "email":email,

                "password":password

            })

            if response.status_code==200:

                data=response.json()

                if data["message"]=="Login Successful":

                    st.session_state["logged_in"]=True
                    st.session_state["user"]=data["user"]

                    st.success("Login Successful 🎉")

                    st.switch_page("pages/3_Dashboard.py")

                else:

                    st.error("Invalid Email or Password")

            else:

                st.error("Server Error")

    st.write("")

    if st.button("📝 Create New Account",use_container_width=True):

        st.switch_page("pages/1_Signup.py")