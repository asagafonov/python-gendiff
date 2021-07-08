import pathlib
from gendiff.parser import parse
from gendiff.formatters.diff import format_diff


def prepare_diff(obj1, obj2):
    keys1 = set(obj1.keys())
    keys2 = set(obj2.keys())
    common_keys = sorted(keys1.union(keys2))

    result = []

    for key in common_keys:
        if key not in obj1:
            result.append({
                'name': key,
                'status': 'added',
                'value': obj2[key]
            })
        elif key not in obj2:
            result.append({
                'name': key,
                'status': 'deleted',
                'value': obj1[key]
            })
        elif type(obj1[key]) == 'object' and type(obj2[key]) == 'object':
            result.append({
                'name': key,
                'status': 'unknown',
                'children': prepare_diff(obj1[key], obj2[key])
            })
        elif obj1[key] == obj2[key]:
            result.append({
                'name': key,
                'status': 'unmodified',
                'value': obj1[key]
            })
        else:
            result.append({
                'name': key,
                'status': 'modified',
                'old_value': obj1[key],
                'new_value': obj2[key]
            })

    return result


def gendiff(filepath1, filepath2, format):
    full_path1 = pathlib.Path(filepath1).resolve()
    full_path2 = pathlib.Path(filepath2).resolve()

    def get_extension(filepath):
        return pathlib.Path(filepath).suffix

    file1_ext = get_extension(filepath1)
    file2_ext = get_extension(filepath2)

    file1 = parse(full_path1, file1_ext)
    file2 = parse(full_path2, file2_ext)

    diff = prepare_diff(file1, file2)
    output = format_diff(diff)

    return output
