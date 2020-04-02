#!/usr/bin/python
import sys
import os
import images
import files
import clustering

if len(sys.argv) != 2:
    print("Command requires one argument, the data directory")
    exit(1)

data_directory = sys.argv[1]

imageset_path = os.path.join(data_directory, 'input', 'imageset', 'training')
datafile_path = os.path.join(data_directory, 'output', 'data.json')

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

pokemons = dict(filter(lambda x: x[1].image is not None, pokemons.items()))

# Store data in a JSON file
files.write_data(pokemons, datafile_path)
