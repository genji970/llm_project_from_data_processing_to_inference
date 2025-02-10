# llm_project_from_data_processing_to_inference 
pipeline building to get pdf files and fine tune pretrained model, lastly use this model. pdf file을 받아서 llm을 파인튜닝하는 파이프라인 구축, model의 활용

# in progress not end

## Update ##
link : https://github.com/genji970/llm-service-deployment-for-fine-tuned-gpt2-pipeline-using-rest-api<br>
llm model service is deployed in aws 

## used ##
python==3.10.12 , torch , ray , huggingface , langchain(not yet) , docker , csv , ..

## future plans ## 

1) current torch : cpu -> torch : cuda 11.3(after finishing process)<br>
2) more pdf files<br>
3) loss decline
4) inference , lang add
5) model opt. i) data aug ii) considering mismatch iii) alignment by RLHF<br>

6) using reference paper , paper's dataset
7) container env build 

7) eval metrics : F1 , BLEU, if RAG is added then adding Recall@k , Precision@k

## reference ## 

