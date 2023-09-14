import gendiff.formatters.stylish as stylish
import gendiff.formatters.plain as plain
import gendiff.formatters.json as json_formatter


def get_format_function_from_str(str_format):
    match str_format:
        case 'stylish':
            format_func = stylish.format
        case 'plain':
            format_func = plain.format
        case 'json':
            format_func = json_formatter.format
        case _:
            raise Exception('Invalid format')
    return format_func
