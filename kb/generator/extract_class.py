def extract_class(path):
    classification = path[path.find('/'):]

    for i in range(0, 2):
        classification = classification[classification.find('/') + 1:]

    for i in range(0, 2):
        classification = removeLast(classification)

    return classification


def extract_type(path):
    classification = path[path.find('/'):]

    for i in range(0, 2):
        classification = classification[classification.find('/') + 1:]

    for i in range(0, 4):
        classification = removeLast(classification)

    return classification

def extract_din(path):
    classification = path[path.find('/'):]

    for i in range(0, 2):
        classification = classification[classification.find('/') + 1:]

    for i in range(0, 4):
        classification = removeLast(classification)

    return classification


def removeLast(path):
    return path[:path.rfind('/')]


def removeFirst(path):
    classification = path[path.find('/') + 1:]