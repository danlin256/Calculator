import tkinter as tk
from UI.buttons import MyButton
from UI.myCanvas import MyCanvas

class CalculatorWindow():
    def __init__(self, width, height):
        self.root = tk.Tk()

        self.root.title("Calculator")
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)

        # Creates a canvas that is centered in the middle of the window
        self.canvas = MyCanvas(self.root, width=width-50, height=height-50)

    def window_run(self):
        self.root.mainloop()
        

