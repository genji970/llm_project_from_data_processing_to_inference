"""

penai api key env에 설정

os.environ["GOOGLE_API_KEY"] = "your-google-api-key"
os.environ["GOOGLE_CSE_ID"] = "your-custom-search-engine-id"

"""
import os
import argparse
from master.arg_add import *
from master.config import *

# 명령줄 파싱
args = parser.parse_args()
run_mode = args.run_mode  # 'app_execution' or 'chat_execution'

#data_process
from data_process.data_main import *
r

#Data_parsing
from Data_parsing.parsing_2 import *

#tokenizer
from tokenizer.tokenizer_main import *
token_generating()

#model_build_folder
from model_build_folder.model_build import *

#model train
from model_train.model_main import *
trainer.train()
llm_model.eval

from agent.agent_main import *
decide_what_to_execute(mode)


