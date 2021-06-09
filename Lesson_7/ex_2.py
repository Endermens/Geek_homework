import os
import yaml
import ast
with open('config.yaml', 'r', encoding='utf-8') as f:
    yaml_dict = yaml.load(f.read())
    my_dict = ast.literal_eval(yaml_dict)
    for key, value in my_dict.items():
        if not os.path.exists(key):
            for item in value:
                for k in item.keys():
                    os.makedirs(os.path.join(key, k))
                    
    # dir_name = 'sample_dir'
    # print(yaml_dict)
    # os.makedirs("/".join(f"{key}_{val}" for key, val in yaml_dict.items()))
