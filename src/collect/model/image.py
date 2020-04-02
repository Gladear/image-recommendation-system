class Image:
    name: str
    colors: list

    def __init__(self, name: str, colors: list):
        self.name = name
        self.colors = colors

    def __str__(self):
        return f"Image(name={self.name}, colors={self.colors})"
