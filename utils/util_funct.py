import os

from llm_project_train.master.config import config

def file_name_append_to_file_path(config , file_name):
    return os.path.join(config['base_path'] , "/" , file_name)