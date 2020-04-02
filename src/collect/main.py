import os
import sys
import images
import json
from model.image import Image
from utils.encoder import ImageEncoder

if len(sys.argv) != 2:
    print("Command requires one argument, the data directory")
    exit(1)

data_directory = sys.argv[1]

imageset_path = os.path.join(data_directory, "input", "imageset")
output_path = os.path.join(data_directory, "output", "data.json")

# List images from imageset
image_paths = images.list_images(imageset_path)
image_list = []

# Get image data from the images
for image_filename in image_paths:
    image_name = os.path.splitext(image_filename)[0]
    image_colors = images.get_image_colors(
        os.path.join(imageset_path, image_filename))

    image = Image(image_name, image_colors)
    image_list.append(image)

# Store data in a JSON file
with open(output_path, "w") as datafile:
    json_data = json.dumps(image_list, indent=4, cls=ImageEncoder)
    datafile.write(json_data)
