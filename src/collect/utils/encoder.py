from json import JSONEncoder

class ImageEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
