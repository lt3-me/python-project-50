import json
import yaml
import os


def get_dict_from_file(file_path):
    format = os.path.split('.')[-1]
    dict_ = parse_content(open(file_path), format)
    return dict_


def parse_content(content, format):
    match format:
        case 'json': content = json.load(content)
        case 'yaml' | 'yml': content = yaml.safe_load(content)
        case _: raise Exception('Unsupported file format')
    return content
