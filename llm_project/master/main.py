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
fine_tuning = args.fine_tuning

from Data_generating.data_process import data_main
from Data_generating.Data_parsing import parsing_2
from Data_generating.data_to_token import data_to_token_main

from model_build.model_build_main import *
from inference.inference_main import *


