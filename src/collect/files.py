import csv
import json
from model.pokemon import Pokemon
from utils.encoder import PokemonEncoder


def read_pokemons_data(filepath: str) -> dict:
    pokemons = {}

    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            name = row[0]
            types = row[1:]

            pokemons[name] = Pokemon(name, types)

    return pokemons


def write_data(pokemons: Pokemon, filepath: str):
    with open(filepath, "w") as datafile:
        json_data = json.dumps(pokemons, indent=4, cls=PokemonEncoder)
        datafile.write(json_data)
