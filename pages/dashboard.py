import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Dashboard    ", page_icon="🎛️", layout="wide")
st.header("Welcome to the Mission Control Center", text_alignment="center")
st.header("Welcome to the :violet[_Dashboard_] 📡", text_alignment="center", divider="yellow")

lcolumn, mcolumn, rcolumn = st.columns(3)

with lcolumn:
    st.image("images\Screenshot 2026-07-06 153552.png",
             use_container_width=True)
    st.link_button("Click Here to Play! 🎮", "https://2753628.playcode.io/")
    st.write("##")
    st.image("images\Screenshot 2026-07-06 163126.png",
             use_container_width=True)
    st.link_button("Click Here to Play! 🎮", "https://2753651.playcode.io")
with mcolumn:
    st.image("images\Screenshot 2026-07-06 160841.png",
             use_container_width=True)
    st.link_button("Click Here to Play! 🎮", "https://2753647.playcode.io")
    st.image("images\Screenshot 2026-07-06 180938.png",
             use_container_width=True)
    st.link_button("Click Here to Play! 🎮", "https://2753669.playcode.io")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")

    st.image("images/unnamed-removebg-preview.png")
    if st.button(":red[Log out]"):
        st.switch_page("stellarhome.py")
with rcolumn:
    st.image("images\Screenshot 2026-07-06 162543.png",
             use_container_width=True)
    st.link_button("Click Here to Play! 🎮", "https://2753649.playcode.io")
    st.image("images\Screenshot 2026-07-06 181234.png",
             use_container_width=True)
    st.link_button("Click Here to Play! 🎮", "https://2753671.playcode.io")
