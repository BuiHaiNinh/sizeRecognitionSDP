def extract_class(path):
    classification = path[path.find('/'):]

    for i in range(0, 2):
        classification = classification[classification.find('/') + 1:]

    for i in range(0, 2):
        classification = remove_last(classification)

    return classification


def extract_class_muenze_group(path):
    classification = path[path.find('/'):]

    for i in range(0, 3):
        classification = classification[classification.find('/') + 1:]

    for i in range(0, 1):
        classification = remove_last(classification)

    return "data_objects/"+classification


def extract_type(path):
    classification = path[path.find('/'):]

    for i in range(0, 2):
        classification = classification[classification.find('/') + 1:]

    for i in range(0, 4):
        classification = remove_last(classification)

    return classification


def extract_din(path):
    classification = path[path.find('/'):]

    for i in range(0, 2):
        classification = classification[classification.find('/') + 1:]

    for i in range(0, 4):
        classification = remove_last(classification)

    return classification


def remove_last(path):
    return path[:path.rfind('/')]


def remove_first(path):
    return path[path.find('/') + 1:]