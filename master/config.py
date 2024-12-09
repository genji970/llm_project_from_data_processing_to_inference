config = {
    'r' : 8,
    'lora_alpha' : 16,
    'lora_dropout' : 0.1,
    'target_module' : ["q_proj", "k_proj", "v_proj", "out_proj"],
    'model_name' : 'gpt2',
    'device_map' : 'auto',
    'torch_dtype' : 'auto',
    'offload_folder' : "./offload",
    'offload_state_dict' : True,
    'prompt_key1' : 'generated_text',
    'prompt_key2' : 'system',
    'parsing_data_path' : 'C:/Users/Administrator/PycharmProjects/project/parsing_output' ,
    'output_path' : 'C:/Users/Administrator/PycharmProjects/project/output',
    'input_path' : 'C:/Users/Administrator/PycharmProjects/project/input',
    'num_cpus' : 8,
    'num_gpus' : 0


}