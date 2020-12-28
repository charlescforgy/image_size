# -*- coding: utf-8 -*-
import argparse
import os
import pickle
from os.path import join

import cv2
from tqdm import tqdm

SUPPORTED_IMAGE_TYPES = [
    "bmp",
    "dib",
    "exr",
    "hdr",
    "jp2",
    "jpe",
    "jpeg",
    "jpg",
    "pbm",
    "pfm",
    "pgm",
    "pic",
    "png",
    "pnm",
    "ppm",
    "pxm",
    "ras",
    "sr",
    "tif",
    "tiff",
    "webp",
]

parser = argparse.ArgumentParser(
    description="""
    A program to create a python dictionary with image names as the keys and
    a the image dimensions as the values.

    This program takes two arguments, a file folder with images
    (path given relative to directory in which program is run), and a name of
    an output file in which to place the pickled results.""",
)


parser.add_argument(
    "--image_folder",
    "-i",
    required=True,
    type=str,
    help="The folder containing the images.",
)
parser.add_argument(
    "--dict_name",
    "-d",
    required=True,
    type=str,
    help="The name of the pickle file to create with the program results.",
)
parser.add_argument(
    "--multithread",
    "-m",
    action="store_true",
    help=(
        """Run program on multiple threads.
        Only recommended for large number of images (minimum 1000).
        """
    ),
)
parser.add_argument(
    "--no_verification",
    action="store_true",
    help=(
        """Do not filter image files to ensure that they are of an appropriate
        type. This option is not recommended, but may be necessary if you have
        files with non-standard names.
        """
    ),
)
args = parser.parse_args()

image_dir = join(os.getcwd(), args.image_folder)
if args.no_verification:
    image_names = sorted(img for img in os.listdir(image_dir))
else:
    image_names = sorted(
        img
        for img in os.listdir(image_dir)
        if img.lower().split(".")[-1] in SUPPORTED_IMAGE_TYPES
    )

def main():
    if args.multithread:
    
        from multiprocessing import Pool
    
        def get_image_shape(name):
            return name, cv2.imread(join(image_dir, name)).shape

        if __name__ == "__main__":
            print("Creating dictionary...")
            with Pool(None) as p:
                image_size_list = p.map(get_image_shape, image_names)
            image_size_dict = dict(image_size_list)
            print(f"Parsing complete, dumping results into pickle file: {args.dict_name}.")
            with open(args.dict_name, "wb") as write_file:
            pickle.dump(image_size_dict, write_file)


    else:
        print(f"Parsing images in {image_dir}")
    
        image_size_list = []
        for name in tqdm(image_names):
            # We use cv2.imread as it is the fastest option. If you don't have OpenCV installed,
            # PIL.Image.open is only slightly slower, and can be used instead with minimal slowdown.
            # imageio.imread is substantially slower, and is not recommended.
            image = cv2.imread(join(image_dir, name))
            image_size_list.append(image.shape)
        print("Creating dictionary...")
        image_size_dict = {name: dim for name, dim in zip(image_names, image_size_list)}

        print(f"Parsing complete, dumping results into pickle file: {args.dict_name}.")
        with open(args.dict_name, "wb") as write_file:


            pickle.dump(image_size_dict, write_file)

if __name__ == '__main__':
    main()
