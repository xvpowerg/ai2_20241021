import streamlit as st
import pandas as pd

st.title("CSV Reading")
uploaded_file = st.file_uploader("選一個CSV文件",type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("原始數據")
    st.dataframe(df)
    st.subheader("數據描述")
    st.dataframe(df.describe())
    st.subheader("數據視覺化")
    st.line_chart(df)
    columns = st.selectbox("選擇要顯示的列",df.columns)
    st.dataframe(df[columns])
    