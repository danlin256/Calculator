from tkinter import Canvas
from UI.buttons import MyButton
from UI.myLabels import MyLabel

class MyCanvas:
    def __init__(self, root, width, height):
        self.canvas = Canvas(root, width=width, height=height, bg='white')
        self.canvas.pack(fill="both", expand=True)

        self.create_grid(6, 4)  # Creates a grid with 6 rows and 4 columns

        self.populate_canvas()

    def create_grid(self, rows, cols):
        for i in range(rows):
            self.canvas.rowconfigure(i, weight=1)
        for j in range(cols):
            self.canvas.columnconfigure(j, weight=1)
        
    def create_button(self, label, command, col, row):
        but = MyButton(self.canvas, label, command)
        but.grid(row=row, column=col)

    def create_label(self, text):
        label = MyLabel(self.canvas, text)

    def populate_canvas(self):
        #self.create_label("Welcome to the Calculator!")
        for i in range(24):
            self.create_button(f"Button {i+1}", lambda i=i: print(f"Button {i+1} clicked!"), col=i%4, row=i//4)
        #self.create_button("Click Me", lambda: print("Button clicked!"), col=0, row=0)
