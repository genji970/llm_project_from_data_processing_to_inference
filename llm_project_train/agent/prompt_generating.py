from langchain import PromptTemplate

#프롬프트 템플릿 정의
prompt = PromptTemplate(
    input_variables=["question"],
    template="Q: {question}\nA:",
)