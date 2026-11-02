from tkinter import Canvas
from UI.buttons import MyButton
from UI.myLabels import MyLabel

class MyCanvas:
    def __init__(self, root, width, height):
        self.canvas = Canvas(root, width=width, height=height, bg='white')
        self.canvas.pack(anchor='center', expand=True)

        self.populate_canvas()

    def create_button(self, label, command):
        button = MyButton(self.canvas, label, command)

    def create_label(self, text):
        label = MyLabel(self.canvas, text)

    def populate_canvas(self):
        self.create_label("Welcome to the Calculator!")
        self.create_button("Click Me", lambda: print("Button clicked!"))
    