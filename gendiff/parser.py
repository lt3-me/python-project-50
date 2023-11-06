import json
import yaml


def get_dict_from_file(file_path):
    format = file_path.split('.')[-1]
    dict_ = parse_content_from_file(file_path, format)
    return dict_


def parse_content_from_file(file, format):
    match format:
        case 'json': content = json.load(open(file))
        case 'yaml' | 'yml': content = yaml.safe_load(open(file))
        case _: raise Exception('Unsupported file format')
    return content
