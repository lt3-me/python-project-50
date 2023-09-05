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


def format(dict1, dict2, diff):

    def _format(dict1, dict2, diff, indent):
        output = ''
        for key in diff:
            match diff[key]:
                case 'added':
                    output += format_key_value(key, dict2[key], '+', indent)
                case 'removed':
                    output += format_key_value(key, dict1[key], '-', indent)
                case 'unchanged':
                    output += format_key_value(key, dict1[key], ' ', indent)
                case 'replaced':
                    output += format_key_value(key, dict1[key], '-', indent)
                    output += format_key_value(key, dict2[key], '+', indent)
                case _:
                    if isinstance(diff[key], dict):
                        output += (f"{' ' * indent}  {key}: {{\n")
                        output += \
                            _format(dict1[key], dict2[key],
                                    diff[key], indent + NEXT_LAYER_INDENT)
                        output += (f"{' ' * indent}  }}\n")
                    else:
                        raise Exception('Diff formatting error')
        return output

    output = '{\n' + _format(dict1, dict2, diff, INDENTATION) + '}'
    print(output)
    return output
