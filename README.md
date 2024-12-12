# llm_project_from_data_processing_to_inference and ai agent
pipeline building to get pdf files and fine tune pretrained model, lastly use this model. pdf file을 받아서 llm을 파인튜닝하는 파이프라인 구축, model의 활용, agent 사용까지

not finished

## how to run ## 
1) You need to set export OPENAI_API_KEY="your-openai-api-key" in terminal

## used ##
python==3.10.0 , torch , ray , huggingface , langchain , flask 

## future plans ## 

1) current torch : cpu -> torch : cuda 11.3<br>
2) more pdf files<br>
3) adding rag + adding faiss<br>
4) considering loss func in faiss
5) developing app code 

## didn't check yet ##
1) def replace_padding_with_ignore in tokenizer folder tokenizing_process.py
: padding_value=128001 -> might be something starts 5 , ignore_value= -100 for gpt2 not other llm<br>

2) Did masked attention work?

## experiment ##

1) model fine tuning experiment first trial.
 ![llm_lora_fine_tuning_result_for_2_epochs](https://github.com/user-attachments/assets/e119c665-c6b9-4aa2-88ae-b10c8416dc98)

2) chatbot sample :  ![chatbot result sample](https://github.com/user-attachments/assets/66bf394b-ef27-4c43-a0bf-6e678b820110)

## Data parsing ##

## Data process ##

## tokenizing ##

## model build ##

## inference ##

## making agent with langchain ##
especially making agent with papers 
