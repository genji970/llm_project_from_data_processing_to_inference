# Ended making pipeline to collect data -> fine tuning -> rest api -> deploying.

next : opt.

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

