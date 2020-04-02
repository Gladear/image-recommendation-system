from json import JSONEncoder

class PokemonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
