import os
import pickle

from kb.generator.kariertes_blatt import get_oben_data_generator, get_seite_data_generator, get_unter_data_generator
from tensorflow.python.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
from kb.models import bce_dice_loss, dice_coeff, get_unet_256

def append_to_filename(filename, append):
    return "{0}_{2}{1}".format(*os.path.splitext(filename) + (append,))

def train_model(train_generator, validation_generator, file_output="models/noname.hdf5", epochs=5):
    # Create callbacks for training
    callbacks = [EarlyStopping(monitor='val_loss',
                               patience=8,
                               verbose=1,
                               min_delta=1e-4),
                 ReduceLROnPlateau(monitor='val_loss',
                                   factor=0.1,
                                   patience=4,
                                   verbose=1,
                                   epsilon=1e-4),
                 ModelCheckpoint(monitor='val_loss',
                                 filepath=file_output,
                                 save_best_only=True
                                 )]

    # Use UNet model. The Input is an image with 256x256 pixel size.
    model = get_unet_256()

    # Training
    history = model.fit(x=train_generator,
              epochs=epochs,
              callbacks=callbacks,
              validation_data=validation_generator,
              )

    with open(append_to_filename(file_output, 'history'), 'wb') as file_pi:
        pickle.dump(history.history, file_pi)

    # Saving
    model.save(file_output)


# Main
root_path = 'data/data_build'
data_generator = [
    get_oben_data_generator,
    get_seite_data_generator,
    get_unter_data_generator
]

data_generator_name = [
    "models/oben.hdf5",
    "models/seite.hdf5",
    "models/unter.hdf5",
]


for get_generator, file_output in zip(data_generator, data_generator_name):
    print("Training {name}...".format(name=file_output))
    validation_generator, train_generator = get_generator(root_path)
    test = next(train_generator)
    train_model(train_generator, validation_generator, file_output=file_output)
