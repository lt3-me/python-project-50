def format_value(value):
    value = f"'{value}'" if isinstance(value, str) else value
    value = 'true' if value is True else value
    value = 'false' if value is False else value
    value = 'null' if value is None else value
    value = '[complex value]' if isinstance(value, dict) else value
    return value


def format(diff):
    output = ''.join(_format(diff, '')).strip()
    return output


def _format(diff, path):
    strings = []

    for key in diff:
        if diff[key].get('children') is None:
            match diff[key].get('status'):
                case 'unchanged':
                    pass
                case 'added':
                    value = format_value(diff[key].get('value'))
                    strings.append(f"\
Property '{path}{key}' was added with value: {value}\n")
                case 'removed':
                    strings.append(f"\
Property '{path}{key}' was removed\n")
                case 'updated':
                    value = format_value(diff[key].get('old_value'))
                    value_new = format_value(diff[key].get('value'))
                    strings.append(f"\
Property '{path}{key}' was updated. From {value} to {value_new}\n")
                case _:
                    raise Exception('Diff formatting error')
        else:
            strings.extend(
                _format(diff[key].get('children'), f'{path}{key}.'))
    return strings
