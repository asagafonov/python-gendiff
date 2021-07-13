def flatten(collection):
    result = []
    for el in collection:
        if isinstance(el, list):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result
