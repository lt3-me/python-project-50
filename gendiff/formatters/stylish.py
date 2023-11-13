SHORT_INDENT = 2
LONG_INDENT = 4


def to_str(key, value, prefix, indent):
    if isinstance(value, dict):
        output = ''
        output += (f"{' ' * indent}{prefix} {key}: {{\n")
        indent += LONG_INDENT
        for key in value:
            output += to_str(key, value[key], ' ', indent)
        indent -= LONG_INDENT
        output += (f"{' ' * indent}  }}\n")
        return output
    if isinstance(value, bool):
        value = 'true' if value else 'false'
    if value is None:
        value = 'null'
    return f"{' ' * indent}{prefix} {key}: {value}\n"


def format(diff):
    output = '{\n' + ''.join(_format(diff, SHORT_INDENT)) + '}'
    return output


def _format(diff, indent):
    lines = []

    for key in diff:
        if diff[key].get('children') is None:
            match diff[key].get('status'):
                case 'added':
                    lines.append(to_str(key, diff[key].get('value'),
                                        '+', indent))
                case 'removed':
                    lines.append(to_str(key, diff[key].get('value'),
                                        '-', indent))
                case 'unchanged':
                    lines.append(to_str(key, diff[key].get('value'),
                                        ' ', indent))
                case 'updated':
                    lines.append(to_str(key, diff[key].get('old_value'),
                                        '-', indent))
                    lines.append(to_str(key, diff[key].get('value'),
                                        '+', indent))
                case _:
                    raise Exception('Diff formatting error')
        else:
            lines.append(f"{' ' * indent}  {key}: {{\n")
            lines.extend(_format(diff[key].get('children'),
                         indent + LONG_INDENT))
            lines.append(f"{' ' * indent}  }}\n")
    return lines
