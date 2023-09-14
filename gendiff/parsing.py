import json
import yaml


def get_dict_from_file(file_path):
    format = file_path.split('.')[-1]
    dict_ = parse_file(file_path, format)
    return dict_


def parse_file(file, format):
    match format:
        case 'json': open_func = json.load
        case 'yaml' | 'yml': open_func = yaml.safe_load
        case _: raise Exception('Unsupported file format')
    return open_func(open(file))
