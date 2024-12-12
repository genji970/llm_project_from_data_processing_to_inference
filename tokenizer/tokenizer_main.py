import os
import logging
import ray

from tokenizer.data_structure_build import *
from tokenizer.tokenizing_process import *
from master.config import *


def token_generating():
    """

    :return: tokenized_data
    """
    return tokenizing(data_preprocess , config)