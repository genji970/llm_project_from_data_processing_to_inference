config = {
    'r' : 2,
    'lora_alpha' : 16,
    'lora_dropout' : 0.1,
    'target_module' : ['attn.c_attn', 'attn.c_proj'],
    'model_name' : 'gpt2',
    'device_map' : 'auto',
    'torch_dtype' : 'auto',
    'offload_folder' : "./offload",
    'offload_state_dict' : True,
    'prompt_key1' : 'generated_text',
    'prompt_key2' : 'system',
    'parsing_data_path' : 'C:/Users/home/PycharmProjects/project/parsing_output' ,
    'output_path' : 'C:/Users/home/PycharmProjects/project/output',
    'input_path' : 'C:/Users/home/PycharmProjects/project/input',
    'base_path' : 'C:/Users/home/PycharmProjects/project',
    'df_train_path' : 'C:/Users/home/PycharmProjects/project/df_train.csv',
    'num_cpus' : 8,
    'num_gpus' : 0,
    'output_dir':"./results",
    'overwrite_output_dir' : True,
    'per_device_train_batch_size' : 1,
    'num_train_epochs' : 0.01,
    'logging_dir' : './logs',
    'logging_steps' : 10,
    'fp16' : True,
    'gradient_accumulation_steps' : 1,
    'learning_rate' : 1e-5,
    'padding_value' : 50256,
    'ignore_value' : 0,
    'task':"text-generation",

    'prompt_input_columns':['value'],
    'prompt_label_columns':['labels']
}

"""
if url is more than one, look at util.funct.py

"""
