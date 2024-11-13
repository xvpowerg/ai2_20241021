import streamlit as st

st.write("Hello StreamLit")
name = st.text_input("Enter your name")
st.write(f"Hello {name}")