# llm_project_from_data_processing_to_inference and ai agent
pipeline building to get pdf files and fine tune pretrained model, lastly use this model. pdf file을 받아서 llm을 파인튜닝하는 파이프라인 구축, model의 활용, agent 사용까지

## used ##
python==3.10.0 , torch , ray , huggingface , langchain , flask 

## future plans ## 

1) current torch : cpu -> torch : cuda 11.3<br>
2) more pdf files<br>
3) adding rag + adding faiss<br>
4) considering loss func in faiss

## didn't check ##
def replace_padding_with_ignore in tokenizer folder tokenizing_process.py
: padding_value=128001 -> might be something starts 5 , ignore_value= -100 for gpt2 not other llm

## how to run ## 

## Data parsing ##

## Data process ##

## tokenizing ##

## model build ##

## inference ##

## making agent with langchain ##
especially making agent with papers 
