import streamlit as st
from utils.api import signup

st.set_page_config(page_title="Signup", page_icon="📝")

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📝 Student Signup")

name = st.text_input("Full Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Create Account"):

    if name == "" or email == "" or password == "":
        st.warning("Please fill all fields.")
    else:

        response = signup({
            "name": name,
            "email": email,
            "password": password
        })

        if response.status_code == 200:
            st.success("🎉 Account Created Successfully")
            st.json(response.json())
        else:
            st.error("Signup Failed")
            st.json(response.json())