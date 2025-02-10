import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from model import model_instance, tokenizer
from database import collection
from bson import ObjectId

router = APIRouter()

# ✅ 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ 입력 데이터 스키마 정의
class InputData(BaseModel):
    text: str  # 🔥 text는 반드시 문자열이어야 함

# ✅ 응답 데이터 스키마 정의
class PredictionResponse(BaseModel):
    prediction: str
    id: str

@router.post("/predict", response_model=PredictionResponse)
def predict(data: InputData):
    # ✅ text_input을 정리하여 tokenizer()에 전달
    text_input = data.text.strip()

    # ✅ 토크나이저 실행
    try:
        inputs = tokenizer(text_input, return_tensors="pt")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Tokenizer failed: {e}")

    # ✅ 모델 예측 수행 (**inputs로 언패킹하여 전달)
    try:
        prediction = model_instance.model.generate(
            **inputs,
            max_length=300,  # 최대 길이 설정 (필요 시 조정)
            no_repeat_ngram_size=2,  # 2-그램 반복 방지
            repetition_penalty=1.2,  # 반복 패널티 적용
            early_stopping=True,  # 조기 종료 활성화
            pad_token_id=tokenizer.eos_token_id  # 패딩 토큰 설정
        )
        prediction_text = tokenizer.decode(prediction[0], skip_special_tokens=True)  # 🔥 결과 디코딩
        print(f"✅ Model Prediction Output: {prediction_text}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model prediction failed: {e}")

    # ✅ 예측 결과를 MongoDB에 저장하고 id 반환
    try:
        result = collection.insert_one({"text": text_input, "prediction": prediction_text})
        response = {
            "prediction": prediction_text,
            "id": str(result.inserted_id)  # 🔥 id 필드 추가
        }
        print(f"✅ Response: {response}")
        logger.info(f"✅ Response: {response}")
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")

@router.get("/prediction/{prediction_id}", response_model=PredictionResponse)
def get_prediction(prediction_id: str):
    """ 저장된 예측 결과 조회 """
    document = collection.find_one({"_id": ObjectId(prediction_id)})

    if document:
        return {"prediction": document["prediction"], "id": str(document["_id"])}
    raise HTTPException(status_code=404, detail="Prediction not found")

@router.get("/")
def home():
    """ 기본 홈 엔드포인트 """
    return {"message": "Welcome to FastAPI Prediction API"}