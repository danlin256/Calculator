from tkinter import Text

class MyText(Text):
    def __init__(self, root, width=20, height=2):
        super().__init__(
            master=root,
            width=width,
            height=height
        )

        self['state'] = "disabled"  # Disables editing of the text widget