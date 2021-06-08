import os
import yaml
with open('config.yaml', 'r', encoding='utf-8') as f:
    yaml_dict = yaml.load(f.read())
    dir_name = 'sample_dir'
    print(yaml_dict)
    os.makedirs("/".join(f"{key}_{val}" for key, val in yaml_dict.items()))
