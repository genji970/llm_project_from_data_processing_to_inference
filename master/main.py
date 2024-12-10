from agent.agent_main import *
from app.app_main import *
from Data_parsing.parsing_2 import *
from data_process.data_main import *
from model_build_folder.model_build import *
from model_train.model_main import *
from tokenizer.tokenizer_main import *

import subprocess

"""

openai api key env에 설정

os.environ["GOOGLE_API_KEY"] = "your-google-api-key"
os.environ["GOOGLE_CSE_ID"] = "your-custom-search-engine-id"



"""

sub_py_list = [
    'C:/Users/Administrator/PycharmProjects/project/data_process',
    'C:/Users/Administrator/PycharmProjects/project/Data_parsing',
    'C:/Users/Administrator/PycharmProjects/project/tokenizer',
    'C:/Users/Administrator/PycharmProjects/project/model_build_folder',
    'C:/Users/Administrator/PycharmProjects/project/model_train',
    "C:/Users/Administrator/PycharmProjects/project/agent",
    'C:/Users/Administrator/PycharmProjects/project/app'
]

if __name__ == "__main__":
    subprocess.run([sub_py_list])







