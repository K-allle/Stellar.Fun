import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Stellar.Fun",page_icon="💫",layout='wide')

def load_img(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
rocket_img = load_img("https://lottie.host/2b72ea31-2c46-4184-a999-ffbc6d0a6a5f/oz2hcLfjsM.json")
robo_img = load_img("https://lottie.host/21d7219e-4121-4dc5-ae1c-2fe52c19fab6/1soupMA0uN.json")
dev_img = load_img("https://lottie.host/36d218ac-9c76-4290-9c7a-c086cd6c1188/SjzpuVy1Qr.json")
one, two = st.columns(2)
with one:
    st.subheader("Your :violet[Space Exploration] Awaits You!")
    st.header("Have :violet[limitless] fun on :blue[Stellar.Fun] :rocket:", divider='yellow')
with two:
    st.image("images/unnamed-removebg-preview.png", width=200)
    if st.button(":yellow[Already have an account?]"):
        st.switch_page("pages/log.py")

lcolumn, rcolumn = st.columns(2)

with lcolumn:
    st.write("##")

    st.subheader("The universe is :red[absurdly] large. Let's :blue[explore] it.")
    st.write("Welcome to a collection of interactive digital experiments designed to help you visualize the staggering, beautiful, and sometimes terrifying scale of :violet[outer space].")
    st.write("Space isn't just empty room; it's filled with worlds where your age changes completely, stars that could swallow our entire solar system, and distances so vast that human math barely makes sense of them. This is your playground to break down the cosmos into bite-size, interactive fun.")
    st.write("_:yellow[What will you discover today?]_")

    st.write("##")
    st.header("Our :violet[Mission] :telescope:")
    st.write("Our mission is :green[simple:] **To make the universe human-sized.** We take overwhelming scientific data, giant numbers, and complex astrophysics, and turn them into playful, interactive web toys. You don't need a degree in aerospace engineering to understand the cosmos—you just need a curiosity to :red[click], :red[scroll], and :red[explore.]")

    st.write("##")
    st.header("🕹️ :blue[Cosmic] Playground (Featured Games)")
    st.write("Made by professional Developers :green[Kushal] and :blue[Aanya]")
    st.subheader("🪐 1. The Alien Birthday Generator")
    st.write("Time moves differently out here. Plug in your Earth birthday and instantly find out how many years old you would be if you lived on the fast-spinning planet Mercury, or the freezing, incredibly slow Pluto.")
    st.subheader("💰 2. Spend an Astronaut's Budget")
    st.write("You have been handed $100 Billion of space agency funding. Your goal? Spend it all. Buy custom spacesuits, purchase a fleet of Saturn V rockets, or rent out the International Space Station for a weekend. Can you empty the vault?")
    st.subheader("📏 3. The Scale of Space Scroll")
    st.write("Start at the size of a single astronaut and scroll all the way out to the edge of the observable universe. Watch as kilometers turn into light-years and planets turn into tiny specks of dust.")

    st.write("##")
    st.header("👨‍🚀 :yellow[Join] Mission Control")
    st.write("Don't explore the :violet[cosmos] in the dark. Create your free explorer account today to sync your journey across all of our interactive space toys!")
    if st.button("Sign Up Now!🚀"):
        st.switch_page("pages/auth.py")
with rcolumn:
    st_lottie(rocket_img,height=300)
    st.write("##")
    st_lottie(robo_img,height=300)
    st.write("##")
    st_lottie(dev_img)
