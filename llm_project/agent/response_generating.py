# 텍스트 생성 래퍼 함수
class CustomHuggingFacePipeline:
    def __init__(self, model, tokenizer , task):
        self.model = model
        self.tokenizer = tokenizer
        self.task = task  # task 속성 추가

    def __call__(self, prompt, max_length=100, temperature=0.7):
        # 입력 토큰화
        inputs = self.tokenizer(prompt, return_tensors="pt")

        # 모델에서 텍스트 생성
        outputs = self.model.generate(
            **inputs,
            max_length=max_length,
            temperature=temperature,
            num_return_sequences=1,
            #eos_token_id=self.tokenizer.eos_token_id,  # 종료 조건: eos 토큰
            no_repeat_ngram_size=3,  # 반복 방지
        )

        # 출력 디코딩 및 반환 형식 수정
        # 생성된 텍스트 디코딩
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return [{"generated_text": generated_text}]  # 리스트 내 딕셔너리로 반환