def stringify_plain(val):
    if val is None:
        return 'null'
    if isinstance(val, dict):
        return '[complex value]'
    if isinstance(val, bool):
        return str(val).lower()
    return '\'{}\''.format(val)


def stringify_stylish(val):
    if val is None:
        return 'null'
    if isinstance(val, dict):
        pass
    if isinstance(val, bool):
        return str(val).lower()
    return '\'{}\''.format(val)
