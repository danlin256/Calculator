import tkinter as tk
from UI.buttons import MyButton

class CalculatorWindow():
    def __init__(self, width, height):
        self.root = tk.Tk()

        self.root.title("Calculator")
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)

        # Creates a canvas that is centered in the middle of the window
        self.canvas = tk.Canvas(self.root, width=width-50, height=height-50, bg='white').pack(anchor=tk.CENTER, expand = True)
    
    def button_creator(self):
        button1 = MyButton(self.canvas, "click me")

    def window_run(self):
        self.button_creator()
        self.root.mainloop()
        

