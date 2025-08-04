import requests

city_dict = {
    "福岡": "Fukuoka",
    "東京": "Tokyo",
    "大阪": "Osaka",
    "名古屋": "Nagoya",
    "札幌": "Sapporo",
    "仙台": "Sendai",
    "広島": "Hiroshima",
    "那覇": "Naha",
}

weather_dict = {
    "Sunny": "☀️ 晴れ",
    "Clear": "☀️ 快晴",
    "Partly cloudy": "🌤 少し曇り",
    "Cloudy": "☁️ 曇り",
    "Overcast": "☁️ どんより",
    "Mist": "🌫 もや",
    "Patchy rain possible": "🌦 小雨の可能性",
    "Light rain": "🌧 小雨",
    "Moderate rain": "🌧 雨",
    "Heavy rain": "⛈ 強い雨",
    "Thunderstorm": "⚡ 雷雨",
    "Snow": "❄️ 雪",
    "Fog": "🌫 霧",
}

def get_weather(city):
    city_en = city_dict.get(city, city)
    url = f"https://wttr.in/{city_en}?format=j1"
    try:
        res = requests.get(url)
        if res.status_code != 200:
            return "天気情報を取得できませんでした。"

        data = res.json()
        weather_en = data["current_condition"][0]["weatherDesc"][0]["value"]
        temp = data["current_condition"][0]["temp_C"]
        max_temp = data["weather"][0]["maxtempC"]
        min_temp = data["weather"][0]["mintempC"]

        weather_jp = weather_dict.get(weather_en, weather_en)

        return (
            f"{weather_jp}<br>"
            f"🌡 現在気温：{temp}℃<br>"
            f"📈 最高気温：{max_temp}℃ / 📉 最低気温：{min_temp}℃"
        )
    except Exception as e:
        return f"⚠️ エラー: {e}"
