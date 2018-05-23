import yaml


def get_room_info(dict_element):
    for k, v in dict_element.items():
        if v is None:
            dict_element.pop(k)
            return k, dict_element

    return None


def parse_yaml(path):
    try:
        yaml_file_content = load_yaml(path)
        parsed_yaml_content = [get_room_info(x) for x in yaml_file_content]
    except IOError:
        parsed_yaml_content = None

    return parsed_yaml_content


def load_yaml(path):
    try:
        stream = open(path, 'r')
    except FileNotFoundError:
        raise IOError

    return yaml.load(stream)
