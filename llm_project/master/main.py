"""

penai api key env에 설정

os.environ["GOOGLE_API_KEY"] = "your-google-api-key"
os.environ["GOOGLE_CSE_ID"] = "your-custom-search-engine-id"

"""
import os
import argparse
import torch
from master.arg_add import *
from master.config import *

# 명령줄 파싱
args = parser.parse_args()
run_mode = args.run_mode  # 'app_execution' or 'chat_execution'
fine_tuning = args.fine_tuning

#data_process
if fine_tuning == "True":
    from data_process.data_main import *

#Data_parsing
if fine_tuning == "True":
    from Data_parsing.parsing_2 import *

#tokenizer
if fine_tuning == "True":
    from tokenizer.tokenizer_main import *
    token_generating()

#model_build_folder
from model_build_folder.model_build import *

#model train
if fine_tuning == "True":
    from model_train.model_main import *

from agent.agent_main import *
decide_what_to_execute(mode)


