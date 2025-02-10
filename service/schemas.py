from pydantic import BaseModel

class InputData(BaseModel):
    text: str  # ✅ GPT-2는 텍스트 입력이 필요함!

class PredictionResponse(BaseModel):
    prediction: list  # 모델의 예측 결과
    id: str  # MongoDB의 ObjectId
