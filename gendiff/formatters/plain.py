from gendiff.utils.flatten import flatten
from gendiff.utils.stringify import stringify_plain as stringify


def add_plain_formatting(diff): # noqa C901
    def iter(data, path):
        result = []
        for item in data:
            new_path = '{}.{}'.format(path, item['name'])

            if item['status'] == 'added':
                result.append(
                    'Property \'{}\' was added with value: {}'.format(
                        new_path[1:],
                        stringify(item['value'])
                    ))
            elif item['status'] == 'deleted':
                result.append(
                    'Property \'{}\' was removed'.format(new_path[1:])
                )
            elif item['status'] == 'unknown':
                result.append(iter(item['children'], new_path))
            elif item['status'] == 'unmodified':
                pass
            elif item['status'] == 'modified':
                result.append(
                    'Property \'{}\' was updated from {} to {}'.format(
                        new_path[1:],
                        stringify(item['old_value']),
                        stringify(item['new_value'])
                    ))
            else:
                raise Exception('Unknown status: {}'.format(item['status']))

        return flatten(result)

    return '\n'.join(iter(diff, ''))
