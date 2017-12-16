# Image Resizer

This takes a folder, finds all the images in that folder, and resizes those images to a square or rectangle of whatever dimensions you want. It applies transparent padding around the original image to retain the original aspect ratio

It is especially useful for resizing images for web.

Python 3.4 and higher only

At some point I'll make this controlable through the command line with [argparse](https://docs.python.org/3/library/argparse.html) or [click](https://dbader.org/blog/python-commandline-tools-with-click) which will remove the need to edit the script to alter the default usage.


## Usage

1. *Install* dependencies with

    `pip install pillow`

    or clone this repository, open the folder and run `pipenv install`

1. *Run* the script, passing it an image, multiple images, a folder, multiple folders, or a mixture of folders and images

    `python main.py folder/containing/images/ another/folder/`

    `python main.py image.jpg another_image.png`

    `python main.py folder/containing/images/ image.jpg`

1. It defaults to producing a 500px by 500px '.png' file in the same folder as original image. To change that, edit the function at the end of the program, for example:

    `resize_images(output_width=600, output_height=400, output_format=".jpg", output_directory="/Users/personal/Documents/"`
