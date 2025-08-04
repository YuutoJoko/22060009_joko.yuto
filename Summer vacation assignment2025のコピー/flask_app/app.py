import streamlit as st
from logic import get_weather

st.set_page_config(page_title="日本の天気", page_icon="🌤", layout="centered")

st.markdown("""
    <style>
    .weather-card {
        background: linear-gradient(145deg, #ffffff, #e6e6e6);
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1), -5px -5px 15px rgba(255,255,255,0.7);
        border-radius: 20px;
        padding: 30px;
        margin-top: 20px;
        text-align: center;
        font-family: 'Segoe UI', sans-serif;
    }
    .city-title {
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .weather-desc {
        font-size: 24px;
        margin-bottom: 10px;
    }
    .temp {
        font-size: 20px;
        color: #555;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>⛅ 日本の天気アプリ</h1>", unsafe_allow_html=True)

city = st.selectbox("📍 都市を選択してください：", ["東京", "大阪", "名古屋", "福岡", "札幌", "仙台", "広島", "那覇"])

if st.button("🌦 天気を確認"):
    with st.spinner("天気情報を取得中..."):
        weather_info = get_weather(city)

    st.markdown(f"""
        <div class='weather-card'>
            <div class='city-title'>{city}</div>
            <div class='weather-desc'>{weather_info}</div>
        </div>
    """, unsafe_allow_html=True)
