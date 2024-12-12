import os
import pandas as pd

from master.config import *

def data_preprocess(config):
    train_data_path = config['parsing_data_file_path']

    # 줄별로 읽어서 데이터프레임 생성
    with open(train_data_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 각 줄을 데이터프레임의 행으로 변환
    df = pd.DataFrame(lines, columns=["Text"])

    # 줄 끝의 공백 제거
    df["Text"] = df["Text"].str.strip()

    # train_data 생성
    train_data = [
        {
            "prompt" : f"{row}",
            "completion" : f"{row}"
        }
        for _ , row in df.iterrows()
    ]

    #특수부호 제거
    train_data = [
        {key: value.replace("\n", "").replace("\\", "") if isinstance(value, str) else value
        for key, value in item.items()}
        for item in train_data
    ]

    max_data_length = max(len(item["prompt"]) for item in train_data)
    max_label_length = max(len(item["completion"]) for item in train_data)

    return train_data , max_data_length , max_label_length