import torch
import os
from transformers import AutoTokenizer

MODEL_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(MODEL_DIR, "saved_model", "full_llm_model.pth")
TOKENIZER_PATH = os.path.join(MODEL_DIR, "saved_model")

# ✅ 올바르게 토크나이저 로드
tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH, trust_remote_code=True)

class Model:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # ✅ 모델 로드
        self.model = self.load_model()

    def load_model(self):
        """ 모델 전체 (구조 + 가중치) 로드 """
        model = torch.load(MODEL_PATH, map_location=self.device)  # 모델 로드
        model.to(self.device)  # GPU/CPU 설정
        return model

    def predict(self, text):
        """ 입력 텍스트를 토큰화하고 모델에 입력하여 예측 수행 """
        with torch.no_grad():
            inputs = tokenizer(text, return_tensors="pt").to(self.device)

            # ✅ 모델 예측
            outputs = self.model.generate(
                **inputs,
                max_length=300,  # 최대 길이 설정 (필요 시 조정)
                no_repeat_ngram_size=2,  # 2-그램 반복 방지
                repetition_penalty=1.2,  # 반복 패널티 적용
                early_stopping=True,  # 조기 종료 활성화
                pad_token_id=tokenizer.eos_token_id  # 패딩 토큰 설정
            )
        generated_ids = outputs[0]
        prompt_length = inputs['input_ids'].shape[1]

        # 프롬프트를 제외한 생성된 부분 추출
        generated_ids_without_prompt = generated_ids[prompt_length:]
        generated_text = tokenizer.decode(generated_ids_without_prompt, skip_special_tokens=True)

        return generated_text

# ✅ 모델 인스턴스 생성
model_instance = Model()
