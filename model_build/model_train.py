from llm_project_train.master.config import *
from llm_project_train.model_build.model_get import get_model
from transformers import Trainer, TrainingArguments
def train_argument(model, tokenized_data):
    # 훈련 설정
    training_args = TrainingArguments(
        output_dir=config['output_dir'],
        overwrite_output_dir=config['overwrite_output_dir'],
        per_device_train_batch_size=config['per_device_train_batch_size'],
        num_train_epochs=config['num_train_epochs'],
        logging_dir=config['logging_dir'],
        logging_steps=config['logging_steps'],
        fp16=config['fp16'],
        gradient_accumulation_steps=config['gradient_accumulation_steps'],
        learning_rate=config['learning_rate'],
    )

    # Trainer 설정 및 훈련 시작
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_data,
    )
    return trainer