# encoding: utf-8

import os
import cv2
import numpy as np

# constant
IMAGE_TYPES = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")

# get classes
classes_rows = open("./caffe/synset_words.txt").read().strip().split("\n")
CLASSES = [row[row.find(" ") + 1:].split(",")[0] for row in classes_rows]  # get the class of picture


def list_files(base_path, validExts=None, contains=None):
    for (root_dir, dir_name, filenames) in os.walk(base_path):  # Directory tree generator.
        for filename in filenames:
            if contains is not None and filename.find(contains) == -1:  # Return -1 on failure find.
                continue

            ext = filename[filename.rfind("."):].lower()  # get file extension

            if validExts is None or ext.endswith(validExts):
                # construct the path to the image and yield it
                image_path = os.path.join(root_dir, filename)
                yield image_path


def list_images(base_path, contains=None):
    return list_files(base_path, validExts=IMAGE_TYPES, contains=contains)


# read caffe
net = cv2.dnn.readNetFromCaffe("./caffe/bvlc_googlenet.prototxt", "./caffe/bvlc_googlenet.caffemodel")

# get all images path
images_path = sorted(list(list_images("images/")))

######################################### Single ########################################

image = cv2.imread(images_path[0])  # read
resize_image = cv2.resize(image, (224, 224))  # resize of the bvlc_googlenet.prototxt: input_dim

# image, scalefactor=None, size=None, mean=None, swapRB=None, crop=None, ddepth=None
# mean: (mean-R, mean-G, mean-B), is use all image mean
blob = cv2.dnn.blobFromImage(resize_image, 1, (224, 244), (104, 117, 123))  # Creates 4-dimensional blob from image.
print("blob shape is: {}".format(blob.shape))

# input and get prediction result
net.setInput(blob)
prediction = net.forward()

# get classes index and text
index = np.argsort(prediction[0])[::-1][0]
text = "Label: {}, {:.2f}% ".format(CLASSES[index], prediction[0][index] * 100)
cv2.putText(image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

# show
cv2.imshow("iamge", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

######################################### Batch ########################################
images = []
for p in images_path[1:]:
    img = cv2.imread(p)
    img = cv2.resize(img, (244, 244))
    images.append(img)

# use images
batch_blob = cv2.dnn.blobFromImages(images, 1, (244, 244), (184, 117, 123))
print("batch blob shape is: {} ".format(batch_blob.shape))

# get result
net.setInput(batch_blob)
predictions = net.forward()

# show text and result
for (i, p) in enumerate(images_path[1:]):
    img = cv2.imread(p)
    idx = np.argsort(predictions[i])[::-1][0]
    text = "Label: {}, {:.2f}% ".format(CLASSES[idx], predictions[i][idx] * 100)
    cv2.putText(img, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




