# Image Resizer

This takes a folder, finds all the images in that folder, and resizes those images to a square of a) 500px or b) the larger dimension of the image – whichever is greater.

For example, an image of 200px by 700px will turn out as 500px by 500px. And image of 200px by 400px will turn out as 400px by 400px. (Transparent padding is added to retain the original aspect ratio).

Python 3 only

## Usage

1. *Install* dependencies with

    `pip install pillow`

    or clone this repository, open the folder and run `pipenv install`

1. *Run* the script over a folder with
`python main.py path/to/folder/with/images/in`
