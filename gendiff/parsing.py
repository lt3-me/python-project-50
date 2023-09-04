import json
import yaml


def parse_file(file_path):
    format = file_path.split('.')[-1]
    match format:
        case 'json': open_func = json.load
        case 'yaml' | 'yml': open_func = yaml.safe_load
        case _: raise Exception('Unsupported file format')

    dict_ = open_func(open(file_path))

    return dict_
