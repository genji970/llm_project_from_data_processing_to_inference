import od
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
from langchain.llms import HuggingFacePipeline
from transformers import AutoTokenizer , pipeline
from langchain.memory import ConversationBufferMemory
from model_train.model_main import llm_model
from agent.prompt_generating import prompt
from master.config import config
from agent.post_processing import clean_response
from agent.response_generating import CustomHuggingFacePipeline

# 메모리 설정
memory = ConversationBufferMemory()

base_model_name = config['model_name']
tokenizer = AutoTokenizer.from_pretrained(base_model_name)

# Custom pipeline 생성
custom_pipeline = CustomHuggingFacePipeline(model=llm_model,
                                            tokenizer=tokenizer,
                                            task=config['task'],
                                            )

# LangChain에 사용할 수 있는 LLM 객체 생성
llm = HuggingFacePipeline(pipeline=custom_pipeline)

# LLMChain 생성
chain = LLMChain(llm=llm,
                 prompt=prompt,
                memory=memory
                 )

def chat():
    print("챗봇에 오신 것을 환영합니다. 질문을 입력하세요 (종료하려면 '종료' 입력):")
    while True:
        user_input = input("Q: ")
        if user_input.lower() == "종료":
            print("챗봇을 종료합니다.")
            break
        response = chain.run({"question": user_input})
        response = clean_response(response)

        print(f"{response}")