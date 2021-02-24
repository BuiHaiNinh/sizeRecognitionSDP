import keras
import numpy as np
from skimage.io import imread


class DataGenerator(keras.utils.Sequence):
    def __init__(self, x_set, y_set, batch_size=1, k_image_size=0.5, shuffle=True):
        self.x, self.y = x_set, y_set
        self.batch_size = batch_size
        self.k_image_size = k_image_size
        self.n = 1
        self.shuffle = shuffle
        self.indexes = np.arange(len(self.x))
        self.img_preprocess = lambda x: x

    def __len__(self):
        return int(np.floor(len(self.x) / self.batch_size))

    def __getitem__(self, idx):
        indexes = self.indexes[idx * self.batch_size:(idx + 1) * self.batch_size]

        batch_x = [self.x[index] for index in indexes]
        batch_y = [self.y[index] for index in indexes]

        def normalize(x):
            return np.array(x/256)

        def img_read(path):
            img = imread(path)
            img = normalize(img)
            img = self.img_preprocess(img)
            return img

        return np.array([img_read(file_name) for file_name in batch_x]), \
               np.array([img_read(file_name) for file_name in batch_y])

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
