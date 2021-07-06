import json


def open_json(filepath):
    return json.load(open(filepath))


def stylish(filepath1, filepath2):
    file1 = open_json(filepath1)
    file2 = open_json(filepath2)

    keys1 = list(file1.keys())
    keys2 = list(file2.keys())
    common_keys = sorted(set(keys1).union(set(keys2)))

    result = ''

    for key in common_keys:
        if (key in keys1 and key in keys2):
            if file1[key] == file2[key]:
                result += '\n    {}: {}'.format(key, file1[key])
            else:
                result += '\n  - {}: {}'.format(key, file1[key])
                result += '\n  + {}: {}'.format(key, file2[key])
        elif (key in keys1 and key not in keys2):
            result += '\n  - {}: {}'.format(key, file1[key])
        elif (key not in keys1 and key in keys2):
            result += '\n  + {}: {}'.format(key, file2[key])

    return '{' + result + '\n}'
