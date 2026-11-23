import tkinter as tk
from UI.myFrame import MyFrame

class CalculatorWindow:
    def __init__(self, width, height):
        self.root = tk.Tk()

        self.root.title("Calculator")               # Sets the title of the window
        self.root.geometry(f"{width}x{height}")     # Sets the size of the window
        self.root.resizable(False, False)           # Makes the window non-resizable

        # Creates a frame that is centered in the middle of the window
        self.frame = MyFrame(self.root, height=height-50, width=width-50)

    # Runs the main loop of the window
    def window_run(self):
        self.root.mainloop()
        

