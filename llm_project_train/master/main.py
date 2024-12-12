"""

penai api key env에 설정

os.environ["GOOGLE_API_KEY"] = "your-google-api-key"
os.environ["GOOGLE_CSE_ID"] = "your-custom-search-engine-id"

"""
import os
import argparse
import subprocess
from master.arg_add import *

# 명령줄 파싱
args = parser.parse_args()
run_mode = args.run_mode  # 'app_execution' or 'chat_execution'

if run_mode == 'app_execution':
    from app.app_main import *

from agent.agent_main import *
from Data_parsing.parsing_2 import *
from data_process.data_main import *
from model_build_folder.model_build import *
from model_train.model_main import *
from tokenizer.tokenizer_main import *

sub_py_list = [
    config['base_path'] + '/' + 'data_process',
    config['base_path'] + '/' + 'Data_parsing',
    config['base_path'] + '/' + 'tokenizer',
    config['base_path'] + '/' + 'model_build_folder',
    config['base_path'] + '/' + 'model_train',
    config['base_path'] + '/' + 'agent'
]

sub_py_file_list = [
    'data_main.py',
    'parsing_2.py',
    'tokenizer_main.py',
    'model_build.py',
    'model_main.py',
    'agent_main.py'
]

# app_main.py 추가 여부
if run_mode == 'app_execution':
    sub_py_list.append(config['base_path'] + '/' + 'app')
    sub_py_file_list.append('app_main.py')

# 각 파일 실행
for path, file in zip(sub_py_list, sub_py_file_list):
    script_path = f"{path}/{file}"
    print(f"Executing: {script_path}")

    try:
        # 스크립트 실행
        result = subprocess.run(["python", script_path], capture_output=True, text=True, check=True)
        print(f"STDOUT:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_path}:\n{e.stderr}")
    except FileNotFoundError:
        print(f"File not found: {script_path}")
