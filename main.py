from sys import argv, exit
from pathlib import Path
from PIL import Image


def resize_images(target_width=500, target_height=500, output_format=".png"):

    if len(argv) != 2:
        print("\nYou need to have a specify a folder with images in.\nThe right command is 'python main.py folder/containing/images/' (without quotes).\n")
        exit(1)

    elif len(argv) == 2:
        images_directory = argv[1]

    counter = 0
    img_files = []

    p = Path(images_directory)

    valid_file_formats = [".jpg", ".jpeg", ".gif",
                          ".png", ".tga", ".tiff", ".webp", ]

    for img_file in p.glob('*.*'):
        if img_file.is_file() and img_file.suffix in valid_file_formats:
            img_files.append(img_file.name)

    if len(img_files) == 0:
        print("\nNo images found\n")
        exit(1)

    print("Resizing images...")
    for img_file in img_files:
        counter += 1
        print(str(counter) + " / " + str(len(img_files)))

        # Opening image file
        img = Image.open(images_directory + img_file)

        # Determining longest side of file
        longest_dimension = max(img.size)

        # If longest dimension is less than target width (default 500px)
        # Make a square of largest side
        if longest_dimension < max(target_width, target_height):
            size = (longest_dimension, longest_dimension)

        # Otherwise, crop the square to target size
        else:
            size = (target_width, target_height)

        # Makes a transparent background and pastes game image over the centre
        img.thumbnail(size, Image.ANTIALIAS)
        background = Image.new('RGBA', size, (255, 255, 255, 0))
        background.paste(
            img, (int((size[0] - img.size[0]) / 2),
                  int((size[1] - img.size[1]) / 2))
        )

        img_file = Path(img_file)
        if img_file.suffix != output_format:
            background.save(images_directory + img_file.stem + output_format)
        else:
            background.save(images_directory + str(img_file))

    print("Finished")


resize_images()
