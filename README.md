# llm_project_from_data_processing_to_inference and ai agent
pipeline building to get pdf files and fine tune pretrained model, lastly use this model. pdf file을 받아서 llm을 파인튜닝하는 파이프라인 구축, model의 활용, agent 사용까지

not finished

## Update ##
2024.12.15 : now can include multiple papers as part of the training dataset

## how to run ## 
1) You need to set export OPENAI_API_KEY="your-openai-api-key" in terminal
2) You need to change base_path , input_folder_path , output_folder_path , parsing_output_folder_path in master.config -- i will change this later<br>
3) put code `python -m master.main execution mode fine_tuning mode` in terminal<br>
   execution_mode = ['chat_execution' , 'app_execution'] , fine_tuning mode = ['True' , 'False']<br>
   You will see pdf -> chunk -> model train -> chatbot system process


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
It is an experiment to determine whether the design is formally valid. Since making a pipeline is in progress. 

1) model fine tuning experiment first trial.
![train result for experiment](https://github.com/user-attachments/assets/638f5215-4a45-48f9-98d3-664bcc57a978)

2) chatbot sample :  ![example for chatbot system](https://github.com/user-attachments/assets/f862181e-5903-448b-add7-c98e106a5ad7) reuslt seems quite bad. Since it is just for whether pipeline works well or not. pad value is different from a real value and chunking process needs to develop , etc..

## Data parsing ##

## Data process ##

## tokenizing ##

## model build ##

## inference ##

## making agent with langchain ##
especially making agent with papers 
