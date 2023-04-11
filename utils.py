
def commands(cmd: str, value: str, data: list[str]) -> list[str]:
    """
     :param cmd: the query command
     :param value: second subsidiary argument
     :param file_data: the name of file, that will be used
     :return: the list with the right answer
     """
    if cmd == 'filter':
        return list(filter(lambda x: value in x, data))
    elif cmd == 'map':
        return list(map(lambda x: x.split()[int(value)], data))
    elif cmd == 'unique':
        return list(set(data))
    elif cmd == 'sort':
        if value == 'desc':
            return sorted(data, reverse=True)
        elif value == 'asc':
            return sorted(data, reverse=False)
    elif cmd == 'limit':
        return data[:int(value)]





