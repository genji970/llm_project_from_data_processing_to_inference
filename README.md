# llm_project_from_data_processing_to_inference 
pipeline building to get pdf files and fine tune pretrained model, lastly use this model. pdf file을 받아서 llm을 파인튜닝하는 파이프라인 구축, model의 활용

# in progress not end

## Update ##
1. 2024.12.26 docker image build
2. no path problem occurs. changed : "C:/.." -> os.path.dirname(__file__). code will automatically change paths 


## how to run ## 
1) You need to set export OPENAI_API_KEY="your-openai-api-key" in terminal 
2) `git clone this repo and put : python -m master.main True` or use `docker_image run code`<br>
   fine_tuning mode = ['True' , 'False']<br>
   You will see pdf -> chunk -> model train -> inference

4) sample docker image package code `docker pull ghcr.io/genji970/llm_data_collecting-processing_inference:latest`


## used ##
python==3.10.12 , torch , ray , huggingface , langchain(not yet) , docker , csv , ..

## future plans ## 

1) current torch : cpu -> torch : cuda 11.3(after finishing process)<br>
2) more pdf files<br>
3) loss decline
4) inference , lang add
5) model opt. i) data aug ii) considering mismatch iii) alignment by RLHF<br>

5) using reference paper , paper's dataset 

6) eval metrics : F1 , BLEU, if RAG is added then adding Recall@k , Precision@k

## reference ## 

