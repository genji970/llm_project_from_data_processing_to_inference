FROM python:3.10.12

#work directory

WORKDIR /llm_project_train/master

COPY llm_project_train/master/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY llm_project_train/master/ .
COPY llm_project_train/Data_generating/ .
COPY llm_project_train/inference / .
COPY llm_project_train/model_build / .
COPY llm_project_train/utils / .

ENTRYPOINT ["python" , "main.py"]
