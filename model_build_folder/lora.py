from peft import LoraConfig , get_peft_model
from master.config import *

# LoRA 설정
lora_config = LoraConfig(
    r=config['r'],  # Low-rank 업데이트 행렬 차원
    lora_alpha=config['lora_alpha'],  # 스케일링 팩터
    lora_dropout=config['lora_dropout'],  # 드롭아웃 비율
    target_modules=config['arget_modules'],  # QLoRA가 적용될 대상 모듈
)

