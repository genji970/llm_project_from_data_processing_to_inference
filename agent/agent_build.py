import od
from langchain import OpenAI, LLMChain
from langchain.memory import ConversationBufferMemory
from model_build_folder.model_build import llm_model
from prompt_generating import prompt

# LLM 체인 생성
#chain = LLMChain(llm=llm, prompt=prompt)

# 메모리 설정
memory = ConversationBufferMemory()

# LLM 체인에 메모리 추가
chain = LLMChain(llm=llm_model, prompt=prompt, memory=memory)

def chat():
    print("챗봇에 오신 것을 환영합니다. 질문을 입력하세요 (종료하려면 '종료' 입력):")
    while True:
        user_input = input("Q: ")
        if user_input.lower() == "종료":
            print("챗봇을 종료합니다.")
            break
        response = chain.run({"question": user_input})
        print(f"A: {response}")