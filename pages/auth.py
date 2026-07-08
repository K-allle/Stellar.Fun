import streamlit as st
import requests
from streamlit_lottie import st_lottie

def load_img(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title="Sign Up", page_icon=":notebook:", layout="wide")
unlock_img = load_img("https://lottie.host/64065949-f517-43f6-aa2e-310d277100a0/2jPwoyOhtY.json")
st.title("Sign up to :blue[Stellar.Fun]!")

email = st.text_input('Email Address')
password = st.text_input('Password', type='password')

if st.button(":blue[Get Started!]"):
    if email and password:
        st.session_state["registered_email"] = email
        st.session_state["registered_password"] = password
        st.switch_page("pages/dashboard.py")
    else:
        st.error("Please provide both an email and password.")
st.header("Founded by people who feel your :violet[limitless] curiosity.", text_alignment="center")
st_lottie(unlock_img,height=300)