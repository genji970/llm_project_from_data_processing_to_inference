from llm_project_train.model_build.prompt_format import *
import pandas as pd
import os
from transformers import Trainer
from llm_project_train.model_build.model_get import get_model
from llm_project_train.model_build.model_train import train_argument
from llm_project_train.master.config import *

train_save_path = config['df_train_path']
df_train = pd.read_csv(train_save_path)

train_data_json = data_to_prompt(df_train)

max_data_length = max(len(item["content"]) for item in train_data_json)
max_label_length = max(len(item["labels"]) for item in train_data_json)

max_len = max(max_data_length , max_label_length)

#llm_model , tokenizer
llm_model , tokenizer = get_model()

tokenized_data = prompt_to_token(train_data_json , tokenizer , max_len)

trainer = train_argument(llm_model, tokenized_data)

trainer.train()
llm_model.eval()