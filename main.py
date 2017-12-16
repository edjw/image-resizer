from sys import argv, exit
from pathlib import Path
from PIL import Image


def collect_images():

    valid_image_formats = [".jpg", ".jpeg", ".gif",
                           ".png", ".tga", ".tiff", ".webp", ]
    img_files = []
    img_directories = []

    if len(argv) < 2:
        print("\nYou need to specify image files or a folder with images in.\nThe right command is 'python main.py folder/containing/images/' or 'python main.py image.png' (without quotes).\n")
        exit(1)

    elif len(argv) >= 2:
        for arg in argv[1:]:
            arg = Path(arg).resolve()

            if arg.is_dir():
                img_directories.append(arg)
            elif arg.is_file() and arg.suffix in valid_image_formats:
                img_files.append(arg)

    for img_directory in img_directories:
        p = Path(img_directory)

        for img_file in p.glob('*.*'):
            if img_file.is_file() and img_file.suffix in valid_image_formats:
                img_files.append(img_file)

    if len(img_files) == 0:
        print("\nNo images found\n")
        exit(1)

    return img_files


def resize_images(img_files, output_width=500, output_height=500, output_format=".png", **kwargs):

    counter = 0

    print("Resizing images...")
    for img_file in img_files:
        counter += 1
        print(str(counter) + " / " + str(len(img_files)))

        # Opening image file
        img = Image.open(img_file)

        # Determining longest side of file
        longest_dimension = max(img.size)

        # If longest dimension is less than target width (default 500px)
        # Make a square of largest side
        if longest_dimension < max(output_width, output_height):
            size = (longest_dimension, longest_dimension)

        # Otherwise, crop the square to target size
        else:
            size = (output_width, output_height)

        # Makes a transparent background and pastes game image over the centre
        img.thumbnail(size, Image.ANTIALIAS)
        background = Image.new('RGBA', size, (255, 255, 255, 0))
        background.paste(
            img, (int((size[0] - img.size[0]) / 2),
                  int((size[1] - img.size[1]) / 2))
        )

        img_file = Path(img_file)
        current_image_directory = str(img_file.parent)

        # If user doesn't specify an output directory,
        # save new image in same directory as original
        if 'output_directory' not in kwargs:
            output_directory = current_image_directory + "/"

        # If output_directory is specified,
        # save it there
        elif 'output_directory' in kwargs:
            output_directory = kwargs['output_directory']
            output_directory = Path(output_directory).expanduser()
            output_directory = str(output_directory) + "/"

        if img_file.suffix != output_format:
            output_file = output_directory + str(img_file.stem) + output_format
        else:
            output_file = output_directory + str(img_file.name)

        print("Saved image: '{}'".format(output_file))
        background.save(output_file)

    print("Finished")


if __name__ == "__main__":
    img_files = collect_images()
    resize_images(img_files, output_directory="/Users/personal/Documents/")
