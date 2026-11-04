from tkinter import Label

class MyLabel(Label):
    def __init__(self, root, text):
        super().__init__(
            master=root,
            text=text
        )
