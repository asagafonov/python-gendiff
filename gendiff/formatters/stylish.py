from gendiff.utils.flatten import flatten
from gendiff.utils.stringify import stringify_stylish as stringify


def expand(val):
    if not isinstance(val, dict):
        return stringify(val)
    keys = list(val.keys())
    result = []
    for key in keys:
        if not isinstance(val[key], dict):
            result.append({
                'name': key,
                'status': 'unknown',
                'children': val[key]
            })
        else:
            result.append({
                'name': key,
                'status': 'unknown',
                'children': expand(val[key])
            })
    return result


def add_stylish_formatting(diff): # noqa C901
    def iter(data, depth):
        space = ' '
        initial_indent1 = space * 4
        initial_indent2 = space * 2
        indent1 = initial_indent1 + (space * (depth * 4))
        indent2 = initial_indent2 + (space * (depth * 4))

        def choose_indent(m):
            if not isinstance(m, list):
                return m
            next_lvl = iter(m, depth + 1)
            formatted = '{\n' + '\n'.join(next_lvl) + '\n' + indent1 + '}'
            return formatted

        def format_value(val):
            return choose_indent(expand(val))

        result = []

        for item in data:
            if item['status'] == 'added':
                result.append('{}+ {}: {}'.format(
                    indent2,
                    item['name'],
                    format_value(item['value'])
                ))
            elif item['status'] == 'deleted':
                result.append('{}- {}: {}'.format(
                    indent2,
                    item['name'],
                    format_value(item['value'])
                ))
            elif item['status'] == 'unknown':
                result.append('{}{}: {}'.format(
                    indent1,
                    item['name'],
                    choose_indent(item['children'])
                ))
            elif item['status'] == 'unmodified':
                result.append('{}{}: {}'.format(
                    indent1,
                    item['name'],
                    format_value(item['value'])
                ))
            elif item['status'] == 'modified':
                result.append([
                    '{}- {}: {}'.format(
                        indent2,
                        item['name'],
                        format_value(item['old_value'])
                    ),
                    '{}+ {}: {}'.format(
                        indent2,
                        item['name'],
                        format_value(item['new_value'])
                    ),
                ])
            else:
                raise Exception('Unknown status: {}'.format(item['status']))

        return flatten(result)

    return '{\n' + '\n'.join(iter(diff, 0)) + '\n}'
