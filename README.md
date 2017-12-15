# Image Resizer

This takes a folder, finds all the images in that folder, and resizes those images to a square or rectangle of whatever dimensions you want. It applies transparent padding around the original image to retain the original aspect ratio

Python 3.4 and higher only

## Usage

1. *Install* dependencies with

    `pip install pillow`

    or clone this repository, open the folder and run `pipenv install`

1. *Run* the script over a folder containg folders

    `python main.py folder/containing/images`


1. It defaults to producing a 500px by 500px '.png' file. To change that, edit the function at the end of the program, for example:

    `resize_images(target_width=600, target_height=400, output_format=".jpg"`

    At some point I'll make this controlable through the command line with [argparse](https://docs.python.org/3/library/argparse.html) or [click](https://dbader.org/blog/python-commandline-tools-with-click).