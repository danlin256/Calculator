from tkinter import Label

class MyLabel:
    def __init__(self, root, text):
        self.label = Label(root, text=text)
        self.label.pack(pady=10)