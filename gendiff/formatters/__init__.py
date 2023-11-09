import gendiff.formatters.stylish as stylish
import gendiff.formatters.plain as plain
import gendiff.formatters.json as json_formatter


def get_formatted_diff(diff, str_format):
    match str_format:
        case 'stylish':
            formatted_diff = stylish.format(diff)
        case 'plain':
            formatted_diff = plain.format(diff)
        case 'json':
            formatted_diff = json_formatter.format(diff)
        case _:
            raise Exception('Invalid format')
    return formatted_diff
