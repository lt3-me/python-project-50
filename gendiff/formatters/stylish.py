INDENTATION = 2
NEXT_LAYER_INDENT = 4


def format_value(value):
    value = 'true' if value is True else value
    value = 'false' if value is False else value
    value = 'null' if value is None else value
    return value


def format_single(key, value, prefix, indent):
    formatted_value = format_value(value)
    return f"{' ' * indent}{prefix} {key}: {formatted_value}\n"


def format_nested(parent, dict_, prefix, indent):
    output = ''
    output += (f"{' ' * indent}{prefix} {parent}: {{\n")
    indent += NEXT_LAYER_INDENT
    for key in dict_:
        if isinstance(dict_[key], dict):
            output += format_nested(key, dict_[key], ' ', indent)
        else:
            output += format_single(key, dict_[key], ' ', indent)
    indent -= NEXT_LAYER_INDENT
    output += (f"{' ' * indent}  }}\n")
    return output


def format_key_value(key, value, prefix, indent):
    if isinstance(value, dict):
        return format_nested(key, value, prefix, indent)
    else:
        return format_single(key, value, prefix, indent)


def format(diff):
    strings = []
    output = '{\n' + ''.join(_format(diff, strings, INDENTATION)) + '}'
    return output


def _format(diff, strings, indent):
    for key in diff:
        if diff[key].get('children') is None:
            match diff[key].get('status'):
                case 'added':
                    strings.append(format_key_value(key, diff[key].get('value'),
                                                    '+', indent))
                case 'removed':
                    strings.append(format_key_value(key, diff[key].get('value'),
                                                    '-', indent))
                case 'unchanged':
                    strings.append(format_key_value(key, diff[key].get('value'),
                                                    ' ', indent))
                case 'updated':
                    strings.append(format_key_value(key,
                                                    diff[key].get('old_value'),
                                                    '-', indent))
                    strings.append(format_key_value(key, diff[key].get('value'),
                                                    '+', indent))
                case _:
                    raise Exception('Diff formatting error')
        else:
            strings.append(f"{' ' * indent}  {key}: {{\n")
            _format(diff[key].get('children'),
                    strings,
                    indent + NEXT_LAYER_INDENT)
            strings.append(f"{' ' * indent}  }}\n")
    return strings
