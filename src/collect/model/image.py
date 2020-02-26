class Image:
    colors: list

    def __init__(self, colors: list):
        self.colors = colors

    def __str__(self):
        return f"Image(colors={self.colors})"
