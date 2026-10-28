import tkinter as tk

class CalculatorWindow():
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # Concatenates the x and y so it fits the geometry field.
        # self.dimensions = str(x)+"x"+str(y)
        self.dimensions = f"{x}x{y}"        # More pythonic

        # This means that it can be accessed from anywhere in class
        self.root = tk.Tk()

    def create_canvas(self):
        self.root.title("Calculator")
        self.root.geometry(self.dimensions)

        self.root.mainloop()