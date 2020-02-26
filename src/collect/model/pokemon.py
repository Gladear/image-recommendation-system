from model.image import Image


class Pokemon:
    name: str
    types: list
    image: Image

    def __init__(self, name: str, types: list, image: Image = None):
        self.name = name
        self.types = types
        self.image = image

    def __str__(self):
        return f"Pokemon(name={self.name},types={self.types},image={self.image})"
