import argparse
import glob
import os

from PIL import Image

from kb.common.files import files
from kb.extraction.extract_mask import extract_mask

configurations = [
    {
        "name": "Bottom Extraction",
        "paper": "./data/original/empty_paper/empty_paper_unter.jpg",
        "input": "./data/original/Kegelstift/**/unten/**/*.JPG",
        "threshold": 90,
        "x1": 3000,
        "x2": 4300,
        "y1": 1000,
        "y2": 3800
    },
    {
        "name": "Bottom Extraction",
        "paper": "./data/original/empty_paper/empty_paper_unter.jpg",
        "input": "./data/original/Zylinderstift/**/unten/**/*.JPG",
        "threshold": 90,
        "x1": 3000,
        "x2": 4300,
        "y1": 1000,
        "y2": 3800
    },
    {
        "name": "Side Extraction",
        "paper": "./data/original/empty_paper/empty_paper_seite.jpg",
        "input": "./data/original/Kegelstift/**/Seite/**/*.JPG",
        "threshold": 70,
        "x1": 1000,
        "x2": 4000,
        "y1": 1000,
        "y2": 3000
    },
    {
        "name": "Side Extraction",
        "paper": "./data/original/empty_paper/empty_paper_seite.jpg",
        "input": "./data/original/Zylinderstift/**/oben/**/*.JPG",
        "threshold": 90,
        "x1": 1000,
        "x2": 4000,
        "y1": 1000,
        "y2": 3000
    },
    {
        "name": "Top Extraction",
        "paper": "./data/original/empty_paper/empty_paper_oben.jpg",
        "input": "./data/original/Kegelstift/**/Seite/**/*.JPG",
        "threshold": 70,
        "x1": 1000,
        "x2": 4000,
        "y1": 1000,
        "y2": 3000
    },
    {
        "name": "Top Extraction",
        "paper": "./data/original/empty_paper/empty_paper_oben.jpg",
        "input": "./data/original/Zylinderstift/**/oben/**/*.JPG",
        "threshold": 90,
        "x1": 1000,
        "x2": 4000,
        "y1": 1000,
        "y2": 3000
    }
]

target_size = (256, 256)

for configuration in configurations:
    extract_mask(threshold=configuration["threshold"],
                 paperPath=configuration["paper"],
                 inputPath=configuration["input"],
                 outputPath="./data/data_build",
                 start=slice(configuration["x1"], configuration["x2"], 1),
                 end=slice(configuration["y1"], configuration["y2"], 1),
                 )

original_files = files("./data/original/**/*.JPG")
for file in original_files:
    image = Image.open(file).resize(target_size)
    outputPath = os.path.splitext(file)[0].replace('original', 'data_build')
    os.makedirs(os.path.dirname(outputPath), exist_ok=True)

    if 'exif' in image.info:
        exif = image.info['exif']
        image.save(outputPath + '_s256.JPG', 'JPEG', exif=exif)
    else:
        image.save(outputPath + '_s256.JPG', 'JPEG')


mask_files = files("./data/data_build/**/*.JPG", targets=["mask"])
for file in mask_files:
    image = Image.open(file).resize(target_size)
    outputPath = os.path.splitext(file)[0]
    os.makedirs(os.path.dirname(outputPath), exist_ok=True)

    if 'exif' in image.info:
        exif = image.info['exif']
        image.save(outputPath + '_s256.JPG', 'JPEG', exif=exif)
    else:
        image.save(outputPath + '_s256.JPG', 'JPEG')
