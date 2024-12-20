# llm_project_from_data_processing_to_inference and ai agent
pipeline building to get pdf files and fine tune pretrained model, lastly use this model. pdf file을 받아서 llm을 파인튜닝하는 파이프라인 구축, model의 활용

in progress

## Update ##
2024.12.15 : now can include multiple papers as part of the training dataset<br>
2024.12.16 : add parsing func,<br> 
1. cutting lines if each line length is less than MIN_WORDS ,<br>
2. Excluding contents after References


## how to run ## 
1) You need to set export OPENAI_API_KEY="your-openai-api-key" in terminal
2) You need to change base_path , input_folder_path , output_folder_path , parsing_output_folder_path in master.config<br>
3) put code `python -m master.main execution mode fine_tuning mode` in terminal<br>
   execution_mode = ['chat_execution' , 'app_execution'] , fine_tuning mode = ['True' , 'False']<br>
   You will see pdf -> chunk -> model train -> chatbot system process /<br> chatbot system process 


## used ##
python==3.10.0 , torch , ray , huggingface , langchain , flask 

## future plans ## 

1) current torch : cpu -> torch : cuda 11.3<br>
2) more pdf files<br>
3) adding rag + adding faiss<br>
4) considering loss func in faiss
5) developing app code
6) chunking
7) inference 

## reference ## 
1) Enhancing Robustness in Large Language Models: Prompting for Mitigating the Impact of Irrelevant Information
Ming Jiang, Tingting Huang, Biao Guo, Yao Lu, Feng Zhang
2) 

