import glob
import os


def delete_files(file_pattern, targets):
    """
    Remove all files, which match pattern.

    :param file_pattern: a string. Example: '../data_objects/**/*.JPG'
    :param targets: an array. Example: ["s500", "s750", "s256"]
    :return:
    """
    if not targets:
        return 0

    def images_filter_func(file):
        return any(target in file for target in targets)

    images = [file for file in glob.glob(file_pattern, recursive=True) if images_filter_func(file)]
    for image in images:
        os.remove(image)

    return images


def files(file_pattern, targets=None):
    """
    Get all image path
    :param file_pattern: a string. Example: '../data_objects/**/*.JPG'
    :param targets: an array. Example: ["s500", "s750", "s256"]
    :return:
    """
    def images_filter_func(file):
        return any(target in file for target in targets)

    if targets:
        images = [file for file in glob.glob(file_pattern, recursive=True) if (images_filter_func(file))]
    else:
        images = [file for file in glob.glob(file_pattern, recursive=True)]

    return images
