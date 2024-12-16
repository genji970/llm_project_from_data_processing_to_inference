import logging

from tokenizer.data_structure_build import data_preprocess
from master.config import config
from model_build_folder.model_build import tokenizer

# Logger 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def replace_padding_with_ignore(labels, padding_value=config['padding_value'], ignore_value=config['ignore_value']):
    return [ignore_value if token == padding_value else token for token in labels]

def tokenizing(data_preprocess, config):
    data , max_data_len , max_label_len = data_preprocess(config)

    max_len = max(max_data_len , max_label_len)

    # input_ids, attention_mask, labels 생성
    tokenized_data = [
        {
            **tokenizer(
                f"{item['prompt']}",
                padding='max_length',
                truncation=True,
                max_length=max_len
            ),
            'labels': replace_padding_with_ignore(
                tokenizer(
                    item['completion'],
                    padding='max_length',
                    truncation=True,
                    max_length=max_len
                )['input_ids']
            )
        }
        for item in data
    ]

    #샘플 검사
    # 필요한 키 목록
    required_keys = ["input_ids", "attention_mask"]

    # 빈 샘플 검사 코드
    for idx, sample in enumerate(tokenized_data):
        missing_keys = [key for key in required_keys if
                        key not in sample or sample[key] is None or len(sample[key]) == 0]
        if missing_keys:
            logger.info(f"Sample at index {idx} is missing required keys or has empty values: {missing_keys}")

    return tokenized_data