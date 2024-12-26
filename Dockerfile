FROM python:3.10.12

#work directory

WORKDIR /master

COPY master/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY master/ .
COPY Data_generating/ .
COPY inference / .
COPY model_build / .
COPY utils / .

CMD ["python" , "main.py"]
