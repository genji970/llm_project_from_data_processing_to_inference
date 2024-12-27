import os
import logging
from llm_project_train.Data_generating.Data_from_web_paper.Data_parsing.parsing_1 import *
from llm_project_train.master.config import *

import nltk

# `punkt` 데이터 다시 다운로드
nltk.download('punkt_tab')

# 병렬 실행
folder_name2 = config['output_path']  # 입력 디렉토리
folder_name3 = config['parsing_data_path']  # 출력 디렉토리
os.makedirs(folder_name3, exist_ok=True)

if os.path.exists(folder_name3):
    logging.info(f"Output directory exists: {folder_name3}")
else:
    logging.error(f"Failed to create output directory: {folder_name3}")

# DataParsing Actor 생성
data_parsing = DataParsing.remote(folder_name2, folder_name3)

try:
    # TXT 파일 검색 및 개수 확인
    txt_files = ray.get(data_parsing.txt_search.remote())
    file_num = len(txt_files)
    if file_num == 0:
        raise ValueError("No TXT files available for processing.")

    # 병렬 작업 수 결정
    task_count = min(file_num, 4)  # 최대 4개의 병렬 작업
    tasks = [data_parsing.txt_parsing.remote() for _ in range(task_count)]

    # 결과 가져오기
    results = ray.get(tasks)
    print("Processing completed. Files saved:")
    for result in results:
        if result:  # 결과가 비어 있지 않은 경우만 출력
            for file_path in result:
                print(file_path)

except ValueError as e:
    logging.error(f"Error during processing: {e}")
except Exception as e:
    logging.error(f"Unexpected error: {e}")




