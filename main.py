from os import listdir, makedirs
from os.path import splitext, join
from sys import argv
from PIL import Image


def collect_all_images():

    if len(argv) < 2:
        print("You need to have a specify a folder with images in.\nThe right command is 'python main.py path/to/folder/with/images/in' (without quotes).")

    elif len(argv) == 2:
        images_folder = argv[1]

        all_images = []
        valid_file_formats = [".jpg", ".jpeg", ".gif", ".png", ".tga", ".tiff", ".webp", ]
        for image in listdir(images_folder):
            file_format = splitext(image)[1]
            if file_format.lower() not in valid_file_formats:
                continue
            all_images.append(join(images_folder, image))

        return all_images


def resize_images(all_images):

    if all_images:
        print("\nResizing all the images...\n")

    for image in all_images:
        image_name = splitext(image)[0].split("/")[-1]
        image_file = Image.open(image)
        longest_dimension = max(image_file.size)

        # If longest dimension is less than 500px
        # Make a square of largest side
        if longest_dimension < 500:
            size = (longest_dimension, longest_dimension)

        # Otherwise, crop the square to 500px
        else:
            size = (500, 500)

        image_file.thumbnail(size, Image.ANTIALIAS)
        background = Image.new('RGBA', size, (255, 255, 255, 0))
        background.paste(
            image_file, (int((size[0] - image_file.size[0]) / 2),
                         int((size[1] - image_file.size[1]) / 2))
        )
        makedirs("resized_images", exist_ok=True)
        background.save("resized_images/" + image_name + ".png")

    print("\nFinished. Your images should be in a folder called 'resized_images' now.\n")


if __name__ == "__main__":
    all_images = collect_all_images()
    resize_images(all_images)
