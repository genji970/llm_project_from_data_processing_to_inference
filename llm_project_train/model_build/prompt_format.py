from llm_project_train.master.config import *

input_column = config['prompt_input_columns']
label_column = config['prompt_label_columns']

def data_to_prompt(combined_df):
    # train_data 생성
    train_data = [
        {"role": "user",
         "content": ",".join([f"{col} : {row[col]}" for col in combined_df[input_column]]),
         "labels": ",".join([f"labels : {row[col]}" for col in combined_df[label_column]])
         }
        for _, row in combined_df.iterrows()
    ]
    return train_data

def prompt_to_token(train_data , tokenizer , max_len):
    # input_ids, attention_mask, labels 생성
    tokenized_data = [
        {
            **tokenizer(
                f"{item['content']}",
                padding='max_length',
                truncation=True,
                max_length=max_len
            ),
            'labels':
                tokenizer(
                    item['labels'],
                    padding='max_length',
                    truncation=True,
                    max_length=max_len
                )['input_ids']

        }
        for item in train_data
    ]
    return tokenized_data

import torch
from datasets import Dataset

def token_to_batch(data):
    tokenized_data = [
        {
            "input_ids" : (torch.tensor(item["input_ids"])).unsqueeze(0) ,
            "attention_mask" : (torch.tensor(item["attention_mask"])).unsqueeze(0) ,
            "labels" : (torch.tensor(item["completion"])).unsqueeze(0)

        }
        for item in data
    ]
    return Dataset.from_list(tokenized_data)
