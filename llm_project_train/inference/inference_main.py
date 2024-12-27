import torch
from llm_project_train.model_build.model_build_main import llm_model , tokenizer , max_len

print("대화를 시작합니다. 종료하려면 'exit' 또는 'quit'을 입력하세요.\n")

# 대화 내역을 저장할 리스트
conversation_history = []

while True:
    # 사용자 입력 받기
    user_input = input("Q: ")

    # 종료 명령어 확인
    if user_input.lower() in ['exit', 'quit']:
        print("대화를 종료합니다.")
        break

    # 대화 내역에 사용자 입력 추가
    conversation_history.append(f"Q: {user_input}")

    # 대화 내역이 너무 길어지면 최근 10개만 유지
    if len(conversation_history) > 20:
        conversation_history = conversation_history[-20:]

    # 대화 내역을 하나의 문자열로 결합
    prompt = "\n".join(conversation_history) + "\nA:"

    try:
        # 토큰화
        inputs = tokenizer(prompt, return_tensors="pt")

        # 텍스트 생성
        outputs = llm_model.generate(
            **inputs,
            max_length=300,  # 최대 길이 설정 (필요 시 조정)
            no_repeat_ngram_size=2,  # 2-그램 반복 방지
            repetition_penalty=1.2,  # 반복 패널티 적용
            early_stopping=True,  # 조기 종료 활성화
            pad_token_id=tokenizer.eos_token_id  # 패딩 토큰 설정
        )

        # 생성된 토큰들
        generated_ids = outputs[0]

        # 프롬프트의 길이 계산
        prompt_length = inputs['input_ids'].shape[1]

        # 프롬프트를 제외한 생성된 부분 추출
        generated_ids_without_prompt = generated_ids[prompt_length:]

        # 디코딩하여 텍스트로 변환 (프롬프트 제외)
        generated_text = tokenizer.decode(generated_ids_without_prompt, skip_special_tokens=True)

        # 생성된 응답 추가
        conversation_history.append(f"A: {generated_text}")

        # 응답 출력
        print(f"A: {generated_text}\n")

    except Exception as e:
        print(f"오류 발생: {e}")
        continue