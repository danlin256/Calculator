from tkinter import ttk

# This class is a wrapper for the ttk.Button widget, allowing for easier creation of buttons with specified labels and commands.
class MyButton(ttk.Button):
    def __init__(self, parent, label, command, width=50):
        super().__init__(
            parent,
            text=label,
            command=command,
            width=width
        )
