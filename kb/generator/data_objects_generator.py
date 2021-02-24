import keras
import numpy as np
from skimage.io import imread


from kb.generator.extract_class import extract_class


class DataObjectsGenerator(keras.utils.Sequence):
    def __init__(self, x_set, classes, batch_size=12, shuffle=True, extract_class_func=extract_class):
        self.x = x_set
        self.batch_size = batch_size
        self.n = 1
        self.shuffle = shuffle
        self.indexes = np.arange(len(self.x))
        self.classes = classes
        self.extract_class_func = extract_class_func
        self.img_preprocess = lambda x: x

    def __len__(self):
        return int(np.floor(len(self.x) / self.batch_size))

    def __getitem__(self, idx):
        indexes = self.indexes[idx * self.batch_size:(idx + 1) * self.batch_size]

        batch_x = [self.x[index] for index in indexes]

        def img_read(path):
            image = imread(path)
            image = self.img_preprocess(image)
            return image

        def output(file_name):
            index = self.classes.index(self.extract_class_func(file_name))
            out = [0] * len(self.classes)
            out[index] = 1
            return out

        def output2(file_name):
            return self.classes.index(self.extract_class_func(file_name))

        return np.array([img_read(file_name) for file_name in batch_x]), \
               np.array([output2(file_name) for file_name in batch_x])

    def __next__(self):
        if self.n >= len(self):
            self.n = 0
        result = self.__getitem__(self.n)
        self.n += 1
        return result

    def on_epoch(self):
        'Updates after each epoch'
        self.indexes = np.arange(len(self.x))
        if self.shuffle:
            np.random.shuffle(self.indexes)
