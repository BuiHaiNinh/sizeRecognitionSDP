import os
from PIL import Image, ImageOps

from kb.common.files import files, delete_files

directory = "./data/data_objects/**/*.JPG"
# Clear workspace
delete_files(directory, ["s500", "s375", "s750", "s256", "s150"])

# Processing images
images = files(directory)


def save_image(image, outputPath, exif=None):
    if exif:
        image.save(outputPath, 'JPEG', exif=exif)
    else:
        image.save(outputPath, 'JPEG')


for index, image in enumerate(images):
    print(f"{index + 1} in {len(images)}...")

    im = Image.open(image)
    im = im.resize((256, 256))

    outputPath = os.path.splitext(image)[0]

    if 'exif' in im.info:
        exif = im.info['exif']
        save_image(im, outputPath + '_s256.JPG', exif)
        save_image(ImageOps.flip(im), outputPath + '_s256_flip.JPG', exif)
        save_image(ImageOps.mirror(im), outputPath + '_s256_mirror.JPG', exif)
        for angle in range(20, 340, 20):
            save_image(im.rotate(angle), outputPath + '_s256_rotation' + str(angle) + '.JPG', exif)
    else:
        save_image(im, outputPath + '_s256.JPG')
        save_image(ImageOps.flip(im), outputPath + '_s256_flip.JPG')
        save_image(ImageOps.mirror(im), outputPath + '_s256_mirror.JPG')
        for angle in range(20, 360, 20):
            save_image(im.rotate(angle), outputPath + '_s256_rotation' + str(angle) + '.JPG')