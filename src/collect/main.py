#!/usr/bin/python
import sys
import os
import images
import files
import clustering

if len(sys.argv) != 3:
    print("Command requires two arguments: the paths of the imageset and output datafile")
    exit(1)

imageset_path = sys.argv[1]
datafile_path = sys.argv[2]

# List images from imageset
image_paths = images.list_images(imageset_path)

# Retrieve pokemon data
pokemons = files.read_pokemons_data(f"{imageset_path}/pokemon.csv")

# Get image data from the images

for image_filename in image_paths:
    pokemon_name = os.path.splitext(image_filename)[0]
    pokemon = pokemons[pokemon_name]

    image_data = clustering.get_image_data(
        os.path.join(imageset_path, image_filename))
    pokemon.image = image_data

# Store data in a JSON file
files.write_data(pokemons, datafile_path)
