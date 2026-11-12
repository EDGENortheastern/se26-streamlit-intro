from pathlib import Path
import streamlit as st

# Load our custom styles. Passing a .css file to st.html injects it as a <style> tag.
st.html(Path("style.css"))

st.title("Hello Name App")

user_name = st.text_input("What is your name?")

if user_name:
    # The key gives this container a CSS class of "st-key-greeting",
    # which style.css uses to style the greeting card.
    with st.container(key="greeting"):
        st.write(f"Hello, { user_name }!")
