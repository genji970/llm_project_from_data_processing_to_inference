## how to run ##

1) `git clone llm_project_train folder and dockerfile`
2) `pip install -r llm_project_train/master/requirements.txt`
3) `python -m llm_project_train.master.main True/False`
4) `git clone service folder`
5) move saved model from llm_project_train to service folder
6) `pip install -r api_for_service/requirements.txt`
7) `python -m main`
8) api run
9) 'ctrl + c' url and add docs. Then, you can test chat system. `http://127.0.0.1:8000/docs`

or just simply

1) `docker pull ghcr.io/genji970/api:latest`
2) `docker run -d -p 8000:8000 --name api_container ghcr.io/genji970/api_image:latest`
3) `http://<EC2_PUBLIC_IP>:8000`

## Detail ##

This repo consist of two parts. llm_project_train folder + Dockerfile. api_for_service folder.(I merged two different project into one.)

Data_generating -> model_build -> master

In Data_generating folder, train_dataset will be made and saved in the format of csv. 

In model_build folder, gpt2 will be loaded from huggingface, gpt2 will be fine tuned.

After fine tuned, weight and whole model structure will be saved as saved model. You have to move this saved model folder into service project consist of service folder. 

if you run service project, rest api will run.

## used ##
python==3.10.12 , torch , ray , huggingface , langchain(not yet) , docker , csv , fast api, aws ec2, etc.
