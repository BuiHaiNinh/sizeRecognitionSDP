# Main
import glob
import os
import sys

import keras

from kb.extraction.extract_data_objects import extract_object
from kb.models import bce_dice_loss, dice_coeff

root_path = './data/original'
images_pattern = [
    root_path + "/Kegelstift/**/oben/**/*.JPG",
    root_path + "/Zylinderstift/**/oben/**/*.JPG",

    root_path + "/Kegelstift/**/Seite/**/*.JPG",
    root_path + "/Zylinderstift/**/Seite/**/*.JPG",

    root_path + "/Kegelstift/**/unten/**/*.JPG",
    root_path + "/Zylinderstift/**/unten/**/*.JPG"
]

models_path = [
    "models/oben.hdf5",
    "models/oben.hdf5",

    "models/seite.hdf5",
    "models/seite.hdf5",

    "models/unter.hdf5",
    "models/unter.hdf5"
]

error = []
for image_pattern, model_path in zip(images_pattern, models_path):
    ignoresFileNames = ["example", "mask", "contour", "meta"]
    images_filter_func = lambda file: not any(ignore in file for ignore in ignoresFileNames)
    images = [file for file in glob.glob(image_pattern, recursive=True) if images_filter_func(file)]
    model = keras.models.load_model(model_path,
                                    custom_objects={'bce_dice_loss': bce_dice_loss, 'dice_coeff': dice_coeff})

    for image in images:
        print(image)
        image_output = image.replace("original", "data_objects")
        os.makedirs(os.path.dirname(image_output), exist_ok=True)

        try:
            extract_object(model, image, image_output, output_size=(1500, 1500))
        except:
            error.append(sys.exc_info()[0])
            print("Error!")

with open('../logs/objects_extraction.txt', 'w') as f:
    for item in error:
        f.write("%s" % item)
