"""

penai api key env에 설정

os.environ["GOOGLE_API_KEY"] = "your-google-api-key"
os.environ["GOOGLE_CSE_ID"] = "your-custom-search-engine-id"

"""
import argparse
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

import multiprocessing

sub_py_list = [
    'C:/Users/Administrator/PycharmProjects/project/data_process',
    'C:/Users/Administrator/PycharmProjects/project/Data_parsing',
    'C:/Users/Administrator/PycharmProjects/project/tokenizer',
    'C:/Users/Administrator/PycharmProjects/project/model_build_folder',
    'C:/Users/Administrator/PycharmProjects/project/model_train',
    "C:/Users/Administrator/PycharmProjects/project/agent",
    'C:/Users/Administrator/PycharmProjects/project/app'
]

sub_py_file_list = [
    'data_main',
    'parsing_2',
    'tokenizer_main',
    'model_build',
    'model_main',
    'agent_main',
    'app_main'
]

if __name__ == "__main__":
    # Manager 객체를 사용해 공유 상태 생성
    with multiprocessing.Manager() as manager:
        shared_state = manager.dict()

        # 프로세스 생성
        if run_mode == 'app_execution':
            process1 = multiprocessing.Process(target=sub_py_file_list[0], args=(shared_state,))
            process2 = multiprocessing.Process(target=sub_py_file_list[1], args=(shared_state,))
            process3 = multiprocessing.Process(target=sub_py_file_list[2], args=(shared_state,))
            process4 = multiprocessing.Process(target=sub_py_file_list[3], args=(shared_state,))
            process5 = multiprocessing.Process(target=sub_py_file_list[4], args=(shared_state,))
            process6 = multiprocessing.Process(target=sub_py_file_list[5], args=(shared_state,))
            process7 = multiprocessing.Process(target=sub_py_file_list[6], args=(shared_state,))

            # 프로세스 실행
            process1.start()
            process1.join()  # Task1이 끝난 후 Task2 실행
            process2.start()
            process2.join()
            process3.start()
            process3.join()
            process4.start()
            process4.join()
            process5.start()
            process5.join()
            process6.start()
            process6.join()
            process7.start()
            process7.join()

            # 최종 상태 확인
            print("Final shared state:", dict(shared_state))

        # 프로세스 생성
        else:
            process1 = multiprocessing.Process(target=sub_py_file_list[0], args=(shared_state,))
            process2 = multiprocessing.Process(target=sub_py_file_list[1], args=(shared_state,))
            process3 = multiprocessing.Process(target=sub_py_file_list[2], args=(shared_state,))
            process4 = multiprocessing.Process(target=sub_py_file_list[3], args=(shared_state,))
            process5 = multiprocessing.Process(target=sub_py_file_list[4], args=(shared_state,))
            process6 = multiprocessing.Process(target=sub_py_file_list[5], args=(shared_state,))

            # 프로세스 실행
            process1.start()
            process1.join()  # Task1이 끝난 후 Task2 실행
            process2.start()
            process2.join()
            process3.start()
            process3.join()
            process4.start()
            process4.join()
            process5.start()
            process5.join()
            process6.start()
            process6.join()

            # 최종 상태 확인
            print("Final shared state:", dict(shared_state))





