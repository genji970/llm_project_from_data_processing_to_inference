from agent.agent_build import *
from master.config import config
from master.arg_add import *

# 명령줄 파싱
args = parser.parse_args()
run_mode = args.run_mode  # 'app_execution' or 'chat_execution'

mode = 0
if run_mode == 'app_execution':
    mode = 1
else:
    mode = 0

def decide_what_to_execute(mode):
    if mode == 1:
        return chain
    else:
        chat()


