import os
import pandas as pd

def data_preprocess(config):
    train_data_path = config['parsing_data_path']
    file_list = os.listdir(train_data_path)

    # 데이터프레임 리스트 초기화
    dataframes = []

    # 줄별로 읽어서 데이터프레임 생성
    for file_name in file_list:
        file_path = os.path.join(train_data_path , file_name)
        if os.path.isfile(file_path):#(폴더 제외)
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                # 각 줄을 데이터프레임의 행으로 변환
                df = pd.DataFrame(lines, columns=["value"])
                # 줄 끝의 공백 제거
                df["value"] = df["value"].str.strip()
                dataframes.append(df)

    # 하나의 데이터프레임으로 합치기 (옵션)
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df