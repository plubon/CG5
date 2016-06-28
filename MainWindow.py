import Tkinter as Tk
import tkFileDialog
from ImageManager import ImageManager
from PIL import ImageTk
from Sphere import Sphere


class MainWindow(Tk.Tk):

    WIDTH = 1024;
    HEIGHT = 768;

    def __init__(self):
        Tk.Tk.__init__(self)
        self.currentFileName = None
        self.imageLabel = None
        self.photo = None
        self.toppanel = None
        self.botpanel = None
        self.manager = ImageManager()
        self.canvas = None
        self.raster = None
        self.sphere = None
        self.initialize()

    def initialize(self):
        self.title = "CGP5"
        self.canvas = Tk.Canvas(self.botpanel, width=MainWindow.WIDTH, height=MainWindow.HEIGHT, bg="#F5F1DE")
        self.canvas.pack()
        self.raster = Tk.PhotoImage(width=MainWindow.WIDTH, height=MainWindow.HEIGHT)
        self.canvas.create_image((0, 0), image=self.raster, state="normal", anchor="nw")
        self.toppanel = Tk.Frame(self)
        self.toppanel.pack(side=Tk.TOP)
        self.botpanel = Tk.Frame(self)
        self.botpanel.pack()
        Tk.Button(self.toppanel, text="Choose an image", command=self.fileselecthandler).pack(side=Tk.LEFT)
        self.imageLabel = Tk.Label(self.botpanel)
        self.imageLabel.pack()
        self.sphere = Sphere(300, 10, 10)
        self.mainloop()

    def fileselecthandler(self):
        self.currentFileName = tkFileDialog.askopenfilename(**self.filechooseoptions)
        if self.currentFileName:
            self.loadimage()

    def loadimage(self):
        self.manager.loadimage(self.currentFileName)
        self.photo = ImageTk.PhotoImage(self.manager.image)

    def drawimage(self):
        if self.photo is None and self.imageLabel is None:
            self.photo = ImageTk.PhotoImage(self.manager.image)
            self.imageLabel = Tk.Label(self, image=self.photo).pack()
        else:
            self.photo = ImageTk.PhotoImage(self.manager.image)
            self.imageLabel.configure(image=self.photo)
            self.imageLabel.image = self.photo


if __name__ == "__main__":
    mw = MainWindow()