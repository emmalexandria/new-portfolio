#!/usr/bin/python

import os
import filetype

from PIL import Image

from typing import NamedTuple


class Settings(NamedTuple):
    img_extensions: tuple
    ignore_root: bool
    compression: int
    asset_dir: str

def main():
    settings = Settings(('.png', '.jpg', '.jpeg'),
                True, 80, "./static")

    files = walk_dir(settings.asset_dir, settings.ignore_root, settings.img_extensions)

    for file in files:
        image = Image.open(file)

        resize_path = add_subdir_to_path(file, "processed")
        basename = os.path.basename(file)

        for i in range(0, 4):
            resize_name = "{0}_{2}{1}".format(*os.path.splitext(basename) + (str(i+1)+"x",))
            fullpath = resize_path+"/"+resize_name

            if os.path.isfile(fullpath): continue 

            compression_ratio = (i+1)*0.25

            webp_save(file, fullpath, settings.compression, image.width*compression_ratio)
            print(f"\033[32m [✓] {file} resized and saved as WebP \033[0m (comp: {settings.compression}, size:{i+1}x)") 

def is_webp(filepath):
    kind = filetype.guess(filepath)
    if kind.MIME == "image/webp":
        return True
    else:
        return False

# idk if theres a built in python function with equal functionality to cwebp, but im fine with using it for now
def webp_save(input, output, compression, width):
    os.system(f'cwebp -q {compression} "{input}" -o "{output}" -quiet -resize {width} 0')


# Return the original path with a subdir placed before the file
def add_subdir_to_path(path, subdir):
    basename = os.path.basename(path)
    dirname = os.path.dirname(path)

    newdir = dirname+"/"+subdir

    if not os.path.exists(newdir):
        os.makedirs(newdir)

    return newdir
    
def walk_dir(directory, ignore_root, extensions):
    valid_files = []

    for subdir, dirs, files in os.walk(directory):
        if (subdir==directory and ignore_root):
            continue

        for file in files:
            if file.lower().endswith(extensions):
                fullpath = subdir+"/"+file
                if is_webp(fullpath) != True:
                    valid_files.append(fullpath)

    return valid_files
                

def resize_to_ratio(image, ratio):
    aspect_ratio = image.width/image.height

    height = round(image.height*ratio)
    width = round(height*aspect_ratio)
    
    return image.resize((width, height), Image.Resampling.LANCZOS)


main()
