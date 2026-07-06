import streamlit as st

st.set_page_config(page_title="Communication",page_icon="📩",layout="wide")

st.header("📫 Send Us Recommendations")

contact_form = """
<form action="https://formsubmit.thevkushalv@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
lcolumn, rcolumn = st.columns(2)
with lcolumn:
    st.markdown(contact_form,unsafe_allow_html=True)
with rcolumn:
    st.empty()