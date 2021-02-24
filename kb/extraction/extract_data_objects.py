import numpy as np
import cv2 as cv
from skimage.io import imread
from skimage.transform import resize


def calculate_input_image(image):
    return np.array([(resize(image, (256, 256)) * 256).astype(np.uint8)])


def extract_size(largest_contour):
    boxes = []
    for c in largest_contour:
        (x, y, w, h) = cv.boundingRect(c)
        boxes.append([x, y, x + w, y + h])

    boxes = np.asarray(boxes)
    left, top = np.min(boxes, axis=0)[:2]
    right, bottom = np.max(boxes, axis=0)[2:]

    width = right - left
    height = bottom - top

    a = max(width, height)

    left = int((right + left - a) / 2)
    right = int(left + a)
    top = int((top + bottom - a) / 2)
    bottom = int(top + a)

    return left, right, top, bottom


def extract_object_from_image(model, image, output_size=(1500, 1500)):
    transformed_image = calculate_input_image(image)
    predicted_mask = model.predict(transformed_image)[0]

    # Threshold
    predicted_mask[predicted_mask >= 0.9] = 1
    predicted_mask[predicted_mask < 0.8] = 0

    # Resize to original size
    predicted_mask = cv.resize(predicted_mask, (image.shape[1], image.shape[0]))
    u8 = predicted_mask.astype(np.uint8)

    # Get largest contour for frame detection
    contours, hierarchy = cv.findContours(u8, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    largest_contours = sorted(contours, key=cv.contourArea)[-1:]
    left, right, top, bottom = extract_size(largest_contours[0])

    crop = image[top:bottom, left:right]
    crop = cv.resize(crop, output_size)
    return crop


def extract_object(model, image_path, output_path, output_size=(1500, 1500)):
    image = imread(image_path)
    result = extract_object_from_image(model, image, output_size)
    cv.imwrite(output_path, result)
