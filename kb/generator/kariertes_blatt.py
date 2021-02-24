import glob
import random

from kb.generator.extract_class import extract_class
from kb.generator.data_generator import DataGenerator
from kb.generator.data_objects_generator import DataObjectsGenerator


def __get_data_generator(dataPath1, dataPath2, k_validation=0.2, shuffle=True):
    images1_mask = [file for file in glob.glob(dataPath1, recursive=True)]
    images2_mask = [file for file in glob.glob(dataPath2, recursive=True)]

    images_mask = images1_mask + images2_mask
    if shuffle:
        random.shuffle(images_mask)

    image = [image.replace("_mask", "") for image in images_mask]

    n_validation = int(len(images_mask) * k_validation)

    return DataGenerator(x_set=image[:n_validation], y_set=images_mask[:n_validation]), \
           DataGenerator(x_set=image[n_validation:], y_set=images_mask[n_validation:])


def get_oben_data(data_path):
    oben_data_path1 = data_path + "/Kegelstift/**/oben/**/*.JPG"
    oben_data_path2 = data_path + "/Zylinderstift/**/oben/**/*.JPG"
    images1_mask = [file for file in glob.glob(oben_data_path1, recursive=True)]
    images2_mask = [file for file in glob.glob(oben_data_path2, recursive=True)]
    return images1_mask + images2_mask


def get_oben_data_generator(data_path, k_validation=0.2, shuffle=True):
    oben_data_path1 = data_path + "/Kegelstift/**/oben/**/*_mask_s256.JPG"
    oben_data_path2 = data_path + "/Zylinderstift/**/oben/**/*_mask_s256.JPG"
    return __get_data_generator(oben_data_path1, oben_data_path2, k_validation=k_validation, shuffle=shuffle)


def get_seite_data_generator(data_path, k_validation=0.2, shuffle=True):
    data_path1 = data_path + "/Kegelstift/**/Seite/**/*_mask_s256.JPG"
    data_path2 = data_path + "/Zylinderstift/**/Seite/**/*_mask_s256.JPG"
    return __get_data_generator(data_path1, data_path2, k_validation=k_validation, shuffle=shuffle)


def get_unter_data_generator(data_path, k_validation=0.2, shuffle=True):
    data_path1 = data_path + "/Kegelstift/**/unten/**/*_mask_s256.JPG"
    data_path2 = data_path + "/Zylinderstift/**/unten/**/*_mask_s256.JPG"
    return __get_data_generator(data_path1, data_path2, k_validation=k_validation, shuffle=shuffle)


def get_data_objects_generator(data_path_1, data_path_2, k_validation=0.2, shuffle=True, classes=None,
                               extract_class_func=extract_class):
    images1_mask = [file for file in glob.glob(data_path_1, recursive=True)]
    images2_mask = [file for file in glob.glob(data_path_2, recursive=True)]

    images_mask = images1_mask + images2_mask
    if classes is None:
        classes = list(set([extract_class_func(image) for image in images_mask]))

    if shuffle:
        random.shuffle(images_mask)

    image = [image.replace("_mask", "") for image in images_mask]

    n_validation = int(len(images_mask) * k_validation)

    return (DataObjectsGenerator(x_set=image[:n_validation], classes=classes, extract_class_func=extract_class_func),
            DataObjectsGenerator(x_set=image[n_validation:], classes=classes, extract_class_func=extract_class_func),
            classes)


def get_oben_data_objects_generator(data_path, k_validation=0.2, shuffle=True, classes=None):
    data_path1 = data_path + "/Kegelstift/**/oben/**/*_s256*.JPG"
    data_path2 = data_path + "/Zylinderstift/**/oben/**/*_s256*.JPG"
    return get_data_objects_generator(data_path1, data_path2, k_validation, shuffle, classes)


def get_seite_data_objects_generator(data_path, k_validation=0.2, shuffle=True, classes=None):
    data_path1 = data_path + "/Kegelstift/**/Seite/**/*_s256*.JPG"
    data_path2 = data_path + "/Zylinderstift/**/Seite/**/*_s256*.JPG"
    return get_data_objects_generator(data_path1, data_path2, k_validation, shuffle, classes)


def get_unter_data_objects_generator(data_path, k_validation=0.2, shuffle=True, classes=None):
    data_path1 = data_path + "/Kegelstift/**/unten/**/*_s256*.JPG"
    data_path2 = data_path + "/Zylinderstift/**/unten/**/*_s256*.JPG"
    return get_data_objects_generator(data_path1, data_path2, k_validation, shuffle, classes)
