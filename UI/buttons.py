from tkinter import ttk

class MyButton:
    def __init__(self, root, label):

        self.button = ttk.Button(
            root, 
            text = label,
            command = lambda: print("Button clicked!")
        )

        self.button.pack(
            ipadx = 5,
            ipady = 5,
            expand = True
        )