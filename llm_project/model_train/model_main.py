import argparse
from master.arg_add import *

from model_train.model_argument import *
from model_build_folder.model_build import llm_model

# 명령줄 파싱
args = parser.parse_args()
fine_tuning_mode = args.fine_tuning

if fine_tuning_mode == 'True':
    trainer.train()
    llm_model.eval
else:
    llm_model.eval


