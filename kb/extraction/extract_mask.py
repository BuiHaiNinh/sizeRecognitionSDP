import glob
import os

import cv2 as cv
import numpy as np
import argparse


# Extract target mask
def extract_target_mask(imagePath, paperPath, region, threshold, output_root='data_build'):
    print(imagePath)
    image = cv.imread(imagePath, 1)
    paper = cv.imread(paperPath, 1)

    kernel = np.ones((3, 3), np.uint8)
    paper = cv.dilate(paper, kernel, iterations=5)
    paper = cv.erode(paper, kernel, iterations=5)
    target = cv.dilate(image, kernel, iterations=5)
    target = cv.erode(target, kernel, iterations=5)

    mask = cv.subtract(paper, target)
    mask = cv.add(mask, mask)

    # crop von seite camera
    crop = mask[region[0], region[1]]

    grayImage = cv.cvtColor(crop, cv.COLOR_BGR2GRAY)
    grayImage = cv.GaussianBlur(grayImage, (9, 9), 0)

    kernel = np.ones((3, 3), np.uint8)
    grayImage = cv.erode(grayImage, kernel, iterations=3)
    grayImage = cv.dilate(grayImage, kernel, iterations=20)
    grayImage = cv.erode(grayImage, kernel, iterations=20)

    edge, thresh = cv.threshold(grayImage, threshold, 255, cv.THRESH_BINARY)

    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    meta = image.copy()

    contour_sizes = [(cv.contourArea(contour), contour) for contour in contours]
    contour_sizes.sort(key=lambda x: x[0], reverse=True)
    # cv.drawContours(meta, [contour_sizes[0][1]], -1, (255, 0, 0), 3)
    cv.rectangle(meta, (region[1].start, region[0].start), (region[1].stop, region[0].stop), (0, 255, 0), 3)

    output = np.zeros((image.shape[0], image.shape[1]), np.uint8)
    output[region[0], region[1]] = thresh

    # add specific mark to output name xxx_mask.JPG
    outputPath = os.path.splitext(imagePath)[0].replace("original", "data_build")
    os.makedirs(os.path.dirname(outputPath), exist_ok=True)

    # write out result image
    cv.imwrite(outputPath + '_mask.JPG', output)
    print(outputPath)
    # cv.imwrite(outputPath + '_meta.JPG', meta)


def extract_mask(threshold, paperPath, inputPath, outputPath, start, end):
    ignoresFileNames = ["example", "mask", "contour", "meta"]

    # extract mask all photos from one folder
    print("Scan files...")
    images_filter_func = lambda file: not any(ignore in file for ignore in ignoresFileNames)
    images = [file for file in glob.glob(inputPath, recursive=True) if images_filter_func(file)]

    print("Extract segmentations...")
    for image in images:
        extract_target_mask(image, paperPath, (start, end), threshold, output_root=outputPath)
        break