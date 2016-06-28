from PIL import Image


class ImageManager:

    def __init__(self):
        self.image = None
        self.raster = None

    def loadimage(self, path):
        self.image = Image.open(path)
        self.raster = self.image.load()

