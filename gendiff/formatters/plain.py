def to_str(value):
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    return value


def format(diff):
    output = ''.join(_format(diff, '')).strip()
    return output


def _format(diff, path):
    lines = []

    for key in diff:
        if diff[key].get('children') is None:
            match diff[key].get('status'):
                case 'unchanged':
                    pass
                case 'added':
                    value = to_str(diff[key].get('value'))
                    lines.append(f"\
Property '{path}{key}' was added with value: {value}\n")
                case 'removed':
                    lines.append(f"\
Property '{path}{key}' was removed\n")
                case 'updated':
                    value = to_str(diff[key].get('old_value'))
                    value_new = to_str(diff[key].get('value'))
                    lines.append(f"\
Property '{path}{key}' was updated. From {value} to {value_new}\n")
                case _:
                    raise Exception('Diff formatting error')
        else:
            lines.extend(
                _format(diff[key].get('children'), f'{path}{key}.'))
    return lines
