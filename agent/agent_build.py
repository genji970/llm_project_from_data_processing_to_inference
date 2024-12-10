import od
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
from langchain.llms import HuggingFacePipeline
from transformers import pipeline
from langchain.memory import ConversationBufferMemory
from model_build_folder.model_build import llm_model
from agent.prompt_generating import prompt

# 메모리 설정
memory = ConversationBufferMemory()

# PeftModel로부터 파이프라인 생성
model_pipeline = pipeline("text-generation", model='gpt2')

# LangChain에 사용할 수 있는 LLM 객체 생성
llm = HuggingFacePipeline(pipeline=model_pipeline)

# LLMChain 생성
chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

def chat():
    print("챗봇에 오신 것을 환영합니다. 질문을 입력하세요 (종료하려면 '종료' 입력):")
    while True:
        user_input = input("Q: ")
        if user_input.lower() == "종료":
            print("챗봇을 종료합니다.")
            break
        response = chain.run({"question": user_input})
        print(f"A: {response}")