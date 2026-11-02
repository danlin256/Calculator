from tkinter import ttk

class MyButton:
    def __init__(self, root, label, command):

        self.button = ttk.Button(
            root, 
            text = label,
            command = command
        )

        self.button.pack(
            ipadx = 5,
            ipady = 5,
            expand = False
        )