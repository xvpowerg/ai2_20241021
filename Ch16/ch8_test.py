import streamlit as st
import pandas as pd
import joblib
# 設置標題
st.title('銷售預測應用')
model,scaler = joblib.load(r'C:\Users\xvpow\ai2_20241021\Ch16\scaled_sales_prediction_model.pkl')

# 輸入廣告支出
tv_spend = st.number_input('輸入 TV 廣告支出', min_value=0.0)
radio_spend = st.number_input('輸入 radio 廣告支出', min_value=0.0)
newspaper_spend = st.number_input('輸入 newspaper 廣告支出', min_value=0.0)

if st.button('預測銷售'):
    # 構建輸入數據框
    input_data = {
        'TV': tv_spend,
        'radio': radio_spend,
        'newspaper': newspaper_spend
    }
    
    input_df = pd.DataFrame([input_data])
    
    # 對輸入數據進行縮放
    input_scaled = scaler.transform(input_df)

    # 預測銷售
    prediction = model.predict(input_scaled)[0]

    # 顯示預測結果
    st.subheader('預測結果')
    st.write(f'預測的銷售額為: {prediction}')
