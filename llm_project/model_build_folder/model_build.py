import os
import warnings
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch import device

#custome import
from model_build_folder.lora import lora_config
from model_build_folder.model_get import load_model , model_freeze , model_ready

#Random seed fixed
import random

seed = 40
deterministic = True

random.seed(seed)
np.random.seed(seed)
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
if deterministic:
  torch.backends.cudnn.deterministic = True
  torch.backends.cudnn.benchmark = False
warnings.filterwarnings('ignore')

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#Lora_configuration
lora_config = lora_config

# model_init
base_model , model_name = load_model()

model_freeze(base_model)

llm_model , tokenizer = model_ready(base_model , model_name , device)

