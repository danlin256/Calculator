import tkinter as tk

class CalculatorWindow():
    def __init__(self, width, height):
        self.root = tk.Tk()

        self.root.title("Calculator")
        self.root.geometry(f"{width}x{height}")


    def window_run(self):
        self.root.mainloop()