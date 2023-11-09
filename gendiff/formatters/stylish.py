SHORT_INDENT = 2
LONG_INDENT = 4


def to_str(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return value


def format_single(key, value, prefix, indent):
    formatted_value = to_str(value)
    return f"{' ' * indent}{prefix} {key}: {formatted_value}\n"


def format_nested(parent, dict_, prefix, indent):
    output = ''
    output += (f"{' ' * indent}{prefix} {parent}: {{\n")
    indent += LONG_INDENT
    for key in dict_:
        if isinstance(dict_[key], dict):
            output += format_nested(key, dict_[key], ' ', indent)
        else:
            output += format_single(key, dict_[key], ' ', indent)
    indent -= LONG_INDENT
    output += (f"{' ' * indent}  }}\n")
    return output


def format_key_value(key, value, prefix, indent):
    if isinstance(value, dict):
        return format_nested(key, value, prefix, indent)
    else:
        return format_single(key, value, prefix, indent)


def format(diff):
    output = '{\n' + ''.join(_format(diff, SHORT_INDENT)) + '}'
    return output


def _format(diff, indent):
    strings = []

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
            strings.extend(_format(diff[key].get('children'),
                           indent + LONG_INDENT))
            strings.append(f"{' ' * indent}  }}\n")
    return strings
