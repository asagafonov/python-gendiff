from gendiff.diff_generators import stylish, plain, json


def format_diff(diff, format):
    if format == 'stylish':
        return stylish.add_stylish_formatting(diff)
    elif format == 'plain':
        return plain.add_plain_formatting(diff)
    elif format == 'json':
        return json.add_json_formatting(diff)
    else:
        raise Exception('{} format is not supported'.format(format))
