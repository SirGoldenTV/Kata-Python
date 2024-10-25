def filter_list(l):
    new_list = []
    for element in l:
        if isinstance(element, int):
            new_list.append(element)
    return new_list