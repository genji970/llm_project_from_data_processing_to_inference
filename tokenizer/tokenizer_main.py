import os
import logging
import ray

from data_structure_build import *
from tokenizing_process import *
from master.config import *

tokenized_data = tokenizing(data_preprocess(config))