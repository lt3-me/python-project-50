def format_value(value):
    value = f"'{value}'" if isinstance(value, str) else value
    value = 'true' if value is True else value
    value = 'false' if value is False else value
    value = 'null' if value is None else value
    value = '[complex value]' if isinstance(value, dict) else value
    return value


def format(dict1, dict2, diff):

    def _format(dict1, dict2, diff, path):
        output = ''
        for key in diff:
            match diff[key]:
                case 'unchanged':
                    pass
                case 'added':
                    value = format_value(dict2[key])
                    output += f"\
Property '{path}{key}' was added with value: {value}\n"
                case 'removed':
                    output += f"\
Property '{path}{key}' was removed\n"
                case 'replaced':
                    value = format_value(dict1[key])
                    value_new = format_value(dict2[key])
                    output += \
                        f"\
Property '{path}{key}' was updated. From {value} to {value_new}\n"
                case _:
                    if isinstance(diff[key], dict):
                        output += \
                            _format(dict1[key], dict2[key],
                                    diff[key], f'{path}{key}.')
                    else:
                        raise Exception('Diff formatting error')
        return output

    output = _format(dict1, dict2, diff, '').strip()
    return output
