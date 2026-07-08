import streamlit as st
import auth
st.set_page_config(page_title="Log In", page_icon="📖", layout="wide")
lcolumn, rcolumn = st.columns(2)
with lcolumn:
    st.title("Log in to :red[Stellar.FUN]")
    st.image(r"C:\Users\allek\Downloads\unnamed-removebg-preview.png", width=300)

with rcolumn:
    email_log = st.text_input('Email Address')
    password_log = st.text_input('Password', type='password')
    if st.button(":violet[Log In!]"):

        if "registered_email" not in st.session_state or "registered_password" not in st.session_state:
            st.error("No registered account found. Please sign up first!")

        elif email_log == st.session_state["registered_email"] and password_log == st.session_state["registered_password"]:
            st.switch_page("pages/dashboard.py")

        else:
            st.write(":red[You have typed one of the following inputs incorrectly]")