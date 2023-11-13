import json
import yaml
import os


def get_dict_from_file(file_path):
    format = os.path.splitext(file_path)[-1]
    with open(file_path, "r") as f:
        return parse_content(f, format)


def parse_content(content, format):
    match format:
        case '.json': content = json.load(content)
        case '.yaml' | '.yml': content = yaml.safe_load(content)
        case _: raise Exception('Unsupported file format')
    return content
