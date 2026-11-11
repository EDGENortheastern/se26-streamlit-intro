import streamlit as st
st.title("Hello Name App")

user_name = st.text_input("What is your name?")

if user_name:
    st.write(f"Hello, { user_name }!")