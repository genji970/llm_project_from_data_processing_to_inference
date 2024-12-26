# llm_project_from_data_processing_to_inference 
pipeline building to get pdf files and fine tune pretrained model, lastly use this model. pdf file을 받아서 llm을 파인튜닝하는 파이프라인 구축, model의 활용

# in progress not end

## Update ##
1. 2024.12.26 docker image build


## how to run ## 
1) You need to set export OPENAI_API_KEY="your-openai-api-key" in terminal 
2) You need to change base_path , input_folder_path , output_folder_path , parsing_output_folder_path in master.config<br>
3) put code `python -m master.main fine_tuning mode` in terminal<br>
   fine_tuning mode = ['True' , 'False']<br>
   You will see pdf -> chunk -> model train -> inference

4) first sample docker image package code `docker pull ghcr.io/genji970/llm_data_collecting-processing_inference:latest`


## used ##
python==3.10.12 , torch , ray , huggingface , langchain(not yet) , docker , csv , ..

## future plans ## 

1) current torch : cpu -> torch : cuda 11.3(after finishing process)<br>
2) more pdf files<br>
3) adding rag + adding faiss<br>
4) considering loss func in faiss
5) developing app code
6) chunking
7) inference
8) langchain plus
9) container
10) rag
11) model opt. i) data aug ii) considering mismatch iii) alignment by RLHF<br>

12) eval metrics : F1 , BLEU, if RAG is added then adding Recall@k , Precision@k

## reference ## 
1) Enhancing Robustness in Large Language Models: Prompting for Mitigating the Impact of Irrelevant Information
Ming Jiang, Tingting Huang, Biao Guo, Yao Lu, Feng Zhang
2) 

