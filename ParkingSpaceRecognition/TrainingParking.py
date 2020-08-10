# -*- coding:utf-8 -*-
# This is a Training parking code
# Warning: This code running can cover origin car-default.h5
# origin `TrainResult/car-default.h5` file is a empty file.

import os
from keras import applications
from keras import optimizers
from keras.layers.core import Flatten
from keras.layers.core import Dense

from keras.models import Model
from keras.callbacks import ModelCheckpoint
from keras.callbacks import EarlyStopping

from keras.preprocessing.image import ImageDataGenerator

# get all train or test files
files_train = 0
files_test = 0

cwd = os.getcwd()
training_train_folder = "TrainData/train"

for sub_folder in os.listdir(training_train_folder):
    path, dirs, files = next(os.walk(os.path.join(training_train_folder, sub_folder)))
    files_train += len(files)

training_test_folder = "TrainData/test"
for sub_folder in os.listdir(training_test_folder):
    path, dirs, files = next(os.walk(os.path.join(training_test_folder, sub_folder)))
    files_test += len(files)

# key point: Some parameters
img_width, img_height = 48, 48
training_data_train_dir = "TrainData/train"
training_data_test_dir = "TrainData/test"
number_train = files_train
number_test = files_test
number_classes = 2
batch_size = 32
epochs = 1

# use VGG16 architecture. can use others.
model = applications.VGG16(include_top=False, weights='imagenet', input_shape=(img_width, img_height, 3))

for layer in model.layers[:10]:
    layer.trainable = False

x = model.output
x = Flatten()(x)

predictions = Dense(number_classes, activation="softmax")(x)

# create model
model_final = Model(input=model.input, output=predictions)

model_final.compile(loss="categorical_crossentropy", optimizer=optimizers.SGD(lr=0.0001, momentum=0.9),
                    metrics=["accuracy"])

# create train or test generator
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    horizontal_flip=True,
    fill_mode="nearest",
    zoom_range=0.1,
    width_shift_range=0.1,
    height_shift_range=0.1,
    rotation_range=5)
test_datagen = ImageDataGenerator(
    rescale=1. / 255,
    horizontal_flip=True,
    fill_mode="nearest",
    zoom_range=0.1,
    width_shift_range=0.1,
    height_shift_range=0.1,
    rotation_range=5)
train_generator = train_datagen.flow_from_directory(
    training_data_train_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode="categorical")
test_generator = test_datagen.flow_from_directory(
    training_data_test_dir,
    target_size=(img_height, img_width),
    class_mode="categorical")

# start trains the model, rewrite to the car-default.h5 file.
# But this checkpoint save method is not available
checkpoint = ModelCheckpoint(filepath="TrainResult/car.h5",
                             monitor="val_acc",
                             verbose=1,
                             save_best_only=True,
                             save_weights_only=False,
                             mode="auto",
                             period=1)

early = EarlyStopping(monitor="val_acc", min_delta=0, patience=10, verbose=1, mode="auto")

history_object = model_final.fit_generator(
    train_generator,
    samples_per_epoch=number_train,
    epochs=epochs,

    validation_data=test_generator,
    nb_val_samples=number_test,
    callbacks=[checkpoint, early]
)

# save model
model_final.save("TrainResult/car-default.h5")
