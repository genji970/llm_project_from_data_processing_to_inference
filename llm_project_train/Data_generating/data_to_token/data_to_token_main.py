import os
import pandas as pd
from llm_project_train.Data_generating.data_to_token.parsing_data_to_df import data_preprocess
from llm_project_train.master.config import *
from datasets import Dataset, DatasetDict

combined_df = data_preprocess(config)

"""

combined_df.columns = ['value']

"""

combined_df['labels'] = combined_df['value']

df = combined_df

train_data_dataset = Dataset.from_pandas(df)

# CSV 파일을 저장할 기본 경로 설정
base_path = config['base_path']  # 실제 저장하고자 하는 경로로 변경하세요.

df_pandas = train_data_dataset.to_pandas()

# 저장할 CSV 파일 경로 설정
csv_file_path = os.path.join(base_path, f"df_train.csv")

# DataFrame을 CSV 파일로 저장
df_pandas.to_csv(csv_file_path, index=False)

print(f"Saved df_train split to {csv_file_path}")

