from fastapi import FastAPI
from pydantic import BaseModel
from api.predict import predict_single  
app = FastAPI()

# 入力データの定義（前処理前の特徴量）
class PredictRequest(BaseModel):
    Podcast_Name: str
    Episode_Title: str
    Episode_Length_minutes: float
    Genre: str
    Host_Popularity_percentage: float
    Publication_Day: str
    Publication_Time: str
    Guest_Popularity_percentage: float
    Number_of_Ads: int
    Episode_Sentiment: str

@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}

@app.post("/predict")
def predict(request: PredictRequest):
    input_dict = request.dict()
    prediction = predict_single(input_dict)
    return {"prediction": prediction}
