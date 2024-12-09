import os
import logging
import ray
import json

from data_concat import Data_Concat
from data_ready import Data_Ready
from data_processing import process_all_pdfs
from master.config import *

#log config setting
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("This is an info message.")

# Ray 초기화
if not ray.is_initialized():
    ray.init(num_cpus = config['num_cpus'] , num_gpus = config['num_gpus'])

url = 'https://arxiv.org/pdf/1706.03762'
#url_list = []
input_folder = config['input_path']
output_folder = config['output_path']

#data_concat
d = Data_Concat(url , input_folder , output_folder)
d.gather_files()

#data_ready
dd = Data_Ready(input_folder)
dd.data_ready

#data_processing
r = process_all_pdfs(input_folder , output_folder)

print(r)


