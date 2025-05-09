import streamlit as st
import requests

st.title("ポッドキャスト再生時間予測")

st.markdown("以下の情報を入力してください：")

# 入力フォーム
Podcast_Name = st.text_input("Podcast Name", "AI Weekly")
Episode_Title = st.text_input("Episode Title", "Understanding GPT")
Episode_Length_minutes = st.number_input("Episode Length (minutes)", min_value=0.0)
Genre = st.text_input("Genre", "Technology")
Host_Popularity_percentage = st.number_input("Host Popularity (%)", min_value=0.0, max_value=100.0)
Publication_Day = st.selectbox("Publication Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
Publication_Time = st.text_input("Publication Time (HH:MM)", "14:00")
Guest_Popularity_percentage = st.number_input("Guest Popularity (%)", min_value=0.0, max_value=100.0)
Number_of_Ads = st.number_input("Number of Ads", min_value=0, step=1)
Episode_Sentiment = st.selectbox("Episode Sentiment", ["Positive", "Neutral", "Negative"])

# JSONにまとめる
input_data = {
    "Podcast_Name": Podcast_Name,
    "Episode_Title": Episode_Title,
    "Episode_Length_minutes": Episode_Length_minutes,
    "Genre": Genre,
    "Host_Popularity_percentage": Host_Popularity_percentage,
    "Publication_Day": Publication_Day,
    "Publication_Time": Publication_Time,
    "Guest_Popularity_percentage": Guest_Popularity_percentage,
    "Number_of_Ads": Number_of_Ads,
    "Episode_Sentiment": Episode_Sentiment
}

if st.button("予測する"):
    try:
        response = requests.post("http://localhost:8000/predict", json=input_data)
        if response.status_code == 200:
            prediction = response.json()["prediction"]
            st.success(f"予測再生時間: {prediction:.2f} 分")
        else:
            st.error(f"予測に失敗しました（ステータスコード: {response.status_code}）")
    except Exception as e:
        st.error(f"接続エラー: {e}")
