import os
import pickle

from keras import Model
from keras.applications.vgg16 import VGG16
from keras.layers import Flatten, Dense, Dropout
from keras.optimizers import RMSprop
import kb.generator.kariertes_blatt as kb


def create_model(object_classes):
    pretrained_model = VGG16(include_top=False, input_shape=(256, 256, 3), weights='imagenet')
    for layer in pretrained_model.layers:
        layer.trainable = False

    last_layer = pretrained_model.get_layer('block5_pool')
    print('last layer of vgg : output shape: ', last_layer.output_shape)
    last_output = last_layer.output

    x = Flatten()(last_output)
    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.2)(x)
    x = Dense(len(object_classes), activation='softmax')(x)

    model = Model(pretrained_model.input, x)
    model.compile(optimizer=RMSprop(lr=0.0001),
                  loss='sparse_categorical_crossentropy',
                  metrics=['acc'])

    return model


def append_to_filename(filename, append):
    return "{0}_{2}{1}".format(*os.path.splitext(filename) + (append,))


def train_model(train_generator, validation_generator, classes, file_output, epochs=8):
    model = create_model(classes)
    history = model.fit(x=train_generator,
                        epochs=epochs,
                        validation_data=validation_generator,
                        verbose=1
                        )

    with open(append_to_filename(file_output, 'labels'), 'w') as f:
        for item in classes:
            f.write("%s\n" % item)
    model.save(file_output)
    with open(append_to_filename(file_output, 'history'), 'wb') as file_pi:
        pickle.dump(history.history, file_pi)
