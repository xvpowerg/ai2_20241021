import streamlit as st
import pandas as pd
from datetime import datetime
st.title("選擇元素")
option_selectbox = st.selectbox(
    "你喜歡甚麼顏色:",
     ["紅色","藍色","綠色"]
)
st.write("你選了:",option_selectbox)
option_mult = st.multiselect("請選您喜歡的水果",["蘋果","香蕉","橘子","西瓜"])
st.write("你選了:",option_mult)

option_radio = st.radio("你喜歡的季節?",["春","夏","秋","冬"])
st.write("你選了:",option_radio)

arre_chackbox = st.checkbox("我同意以下條款")
if arre_chackbox:
    st.write("謝謝你同意我們的條款")
else:
    st.write("請同意我們的條款")        

option_selec_slider = st.select_slider(
    "選一個範圍",
    options=[1,2,3,4,5,6,7,8,9,10],
    value=(3,6)
)
st.write("你選了:",option_selec_slider)
for i in range(option_selec_slider[0],option_selec_slider[1]+1):
    st.write(i)

data_input = st.date_input("選一個日期:",datetime.today().date())
st.write("你選了:",data_input)

value =   st.slider("請選範圍:",0.0,100.0,(25.0,75.0))
st.write("你選了:",value)