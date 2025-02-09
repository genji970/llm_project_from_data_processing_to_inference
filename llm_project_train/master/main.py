"""

penai api key env에 설정

os.environ["GOOGLE_API_KEY"] = "your-google-api-key"
os.environ["GOOGLE_CSE_ID"] = "your-custom-search-engine-id"

"""

import os
import argparse
import torch
from llm_project_train.master.arg_add import *
from llm_project_train.master.config import *

# 명령줄 파싱
args = parser.parse_args()
fine_tuning = args.fine_tuning

from llm_project_train.Data_generating.Data_from_web_paper.data_process import data_main
from llm_project_train.Data_generating.Data_from_web_paper.Data_parsing import parsing_2
from llm_project_train.Data_generating.data_to_token import data_to_token_main

from llm_project_train.model_build.model_build_main import *

# ✅ 저장할 폴더 경로 설정
save_directory = "./saved_model"
os.makedirs(save_directory, exist_ok=True)

# ✅ 모델과 토크나이저 저장 경로 지정
model_save_path = os.path.join(save_directory, "full_llm_model.pth")  # 모델 전체 저장 (구조 + 가중치)
tokenizer_save_path = save_directory  # 토크나이저 저장 (디렉토리 단위)

try:
    # ✅ 모델 전체 저장 (구조 + 가중치 포함)
    torch.save(llm_model, model_save_path)

    # ✅ 토크나이저 저장
    llm_model.base_model.tokenizer = tokenizer
    llm_model.tokenizer.save_pretrained(tokenizer_save_path)

    # ✅ 저장된 파일 확인
    saved_files = os.listdir(save_directory)
    required_files = ["full_llm_model.pth", "tokenizer_config.json", "vocab.json", "merges.txt"]

    missing_files = [file for file in required_files if file not in saved_files]

    if not missing_files:
        print("✅ 모델 & 토크나이저 저장 성공!")
        print(f"📁 저장된 파일 목록: {saved_files}")
    else:
        print(f"❌ 오류: 일부 저장 파일이 누락됨: {missing_files}")

except Exception as e:
    print(f"❌ 오류 발생: {e}")



