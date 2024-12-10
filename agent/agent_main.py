from agent_build import *
from master.config import config

mode = 0
if config['run_mode'] == 'app_execution':
    mode = 1

def decide_what_to_execute(mode):
    if mode == 1:
        return chain
    else:
        chat()

decide_what_to_execute(mode)

