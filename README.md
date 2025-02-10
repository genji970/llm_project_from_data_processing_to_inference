# Ended making pipeline to collect data -> fine tuning -> rest api -> deploying.

next : opt.

## how to run ##

1) `git clone llm_project_train folder and dockerfile`
2) `pip install -r llm_project_train/master/requirements.txt`
3) `python -m llm_project_train.master.main True/False`
4) `git clone service folder`
5) move saved model from llm_project_train to service folder
6) `pip install -r service/requirements.txt`
7) python -m main
8) api rusn

or just simply

`docker pull ghcr.io/genji970/api:latest`

## used ##
python==3.10.12 , torch , ray , huggingface , langchain(not yet) , docker , csv , fast api, aws ec2, etc.

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

