from peft import LoraConfig, get_peft_model
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from llm_project_train.master.config import *

# LoRA 설정
lora_config = LoraConfig(
    r=config['r'],  # Low-rank 업데이트 행렬 차원
    lora_alpha=config['lora_alpha'],  # 스케일링 팩터
    lora_dropout=config['lora_dropout'],  # 드롭아웃 비율
    target_modules=config['target_module'],  # QLoRA가 적용될 대상 모듈
)

def get_model():
    # 모델 및 토크나이저 로드
    model_name = config['model_name']
    base_model = AutoModelForCausalLM.from_pretrained(model_name,
                                                  device_map=config['device_map'],             # GPU와 CPU를 자동 분배
                                                  torch_dtype=config['torch_dtype'],            # 자동으로 적절한 데이터 타입(FP32, FP16 등) 선택
                                                  offload_folder=config['offload_folder'],    # 메모리가 부족할 경우 CPU로 데이터를 오프로드
                                                  offload_state_dict=config['offload_state_dict'])        # 가중치도 필요 시 CPU로 오프로드

    #기존 model freeze
    for param in base_model.parameters():
        param.requires_grad = False

    model = get_peft_model(base_model, lora_config)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token_id =tokenizer.eos_token_id
    return model , tokenizer