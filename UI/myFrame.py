from tkinter import Frame
from UI.buttons import MyButton
from UI.myLabels import MyLabel

class MyFrame(Frame):
    def __init__(self, root, height, width):
        self.frame = Frame(root, height=height, width=width)
        self.frame.pack(fill="both", expand=True)

        self.create_grid(6, 4)  # Creates a grid with 6 rows and 4 columns

        self.populate_Frame()  # Populates the frame with buttons and labels

    # Creates a grid layout for the frame with specified number of rows and columns
    def create_grid(self, rows, columns):
        for i in range(rows):
            self.frame.rowconfigure(i, weight=1)
        for j in range(columns):
            self.frame.columnconfigure(j, weight=1)

    # Creates button and places in correct space
    # Functionality can be passed in as argument
    def create_button(self, label, command, col, row):
        but = MyButton(self.frame, label, command)
        but.grid(row=row, column=col)

    # Creates label and places in correct space
    def create_label(self, text, col=0, row=0):
        label = MyLabel(self.frame, text)
        label.grid(row=row, column=col)

    # Populates the frame with buttons and labels
    def populate_Frame(self):
        self.create_label("Welcome to the Calculator!")
        for i in range(24):
            self.create_button(f"Button {i+1}", lambda i=i: print(f"Button {i+1} clicked!"), col=i%4, row=i//4)
        
