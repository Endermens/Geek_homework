import os
import yaml
from yaml.loader import SafeLoader


def isDict(var, path=''):
    if type(var) is dict:
        for f_key, f_value in var.items():
            new_path = (path + "/" + f_key)[1::]
            if not os.path.exists(new_path):
                os.makedirs(new_path)
            isDict(f_value, path + "/" + f_key)
    else:
        if type(var) is list:
            for f_key in var:
                isDict(f_key, path)
        else:
            new_path = (path + "/" + var)[1::]
            if not os.path.exists(new_path):
                open(new_path, "w")
            return path + "/" + var


with open('config.yaml', 'r', encoding='utf-8') as f:
    yaml_dict = yaml.load(f.read(), Loader=SafeLoader)
    isDict(yaml_dict)