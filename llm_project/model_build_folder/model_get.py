from peft import LoraConfig, get_peft_model
from transformers import AutoTokenizer, AutoModelForCausalLM
from model_build_folder.lora import lora_config
from master.config import *

def load_model():
    # 모델 및 토크나이저 로드
    model_name = config['model_name']
    base_model = AutoModelForCausalLM.from_pretrained(model_name,
                                                  device_map=config['device_map'],             # GPU와 CPU를 자동 분배
                                                  torch_dtype=config['torch_dtype'],            # 자동으로 적절한 데이터 타입(FP32, FP16 등) 선택
                                                  offload_folder=config['offload_folder'],    # 메모리가 부족할 경우 CPU로 데이터를 오프로드
                                                  offload_state_dict=config['offload_state_dict']
                                                  )        # 가중치도 필요 시 CPU로 오프로드
    return base_model , model_name

def model_freeze(base_model):
    #기존 model freeze
    for param in base_model.parameters():
        param.requires_grad = False


def model_ready(base_model , model_name):
    model = get_peft_model(base_model, lora_config)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})
    model.resize_token_embeddings(len(tokenizer))
    return model , tokenizer