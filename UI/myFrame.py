from UI.myText import MyText
from tkinter import Frame
from UI.buttons import MyButton
from tkinter.ttk import Label

class MyFrame(Frame):
    def __init__(
            self, 
            root, 
            height: int, 
            width: int
        ) -> None:
            super().__init__(root, height=height, width=width)

            self.pack(fill="both", expand=True)

            self.configure_grid(6, 4)  # Creates a grid with 6 rows and 4 columns

            self.populate_frame()  # Populates the frame with buttons and labels

    # Creates a grid layout for the frame with specified number of rows and columns
    def configure_grid(self, rows: int, columns: int):
        for i in range(rows):
            self.rowconfigure(i, weight=1)
        for j in range(columns):
            self.columnconfigure(j, weight=1)

        self.rowconfigure(rows, weight=1)  # Adds an extra row for the text widget

    # Creates button and places in correct space
    # Functionality can be passed in as argument
    def create_button(
            self, 
            label: str, 
            command: callable[[], None] | None,
            col: int, 
            row: int, 
            width: int, 
            columnspan: int = 1, 
            rowspan: int = 1
        ) -> None:
        
        button = MyButton(
            self, 
            label, 
            command, 
            width=width)

        button.grid(
            row=row, 
            column=col, 
            columnspan=columnspan, 
            rowspan=rowspan, 
            sticky="nsew")

    def button_grid(self):
        BUTTON_LAYOUT = [
            {"label": "C", "row": 2, "col": 0},
            {"label": "/", "row": 2, "col": 1},
            {"label": "*", "row": 2, "col": 2},
            {"label": "-", "row": 2, "col": 3},

            {"label": "7", "row": 3, "col": 0},
            {"label": "8", "row": 3, "col": 1},
            {"label": "9", "row": 3, "col": 2},
            {"label": "+", "row": 3, "col": 3, "rowspan": 2},

            {"label": "4", "row": 4, "col": 0},
            {"label": "5", "row": 4, "col": 1},
            {"label": "6", "row": 4, "col": 2},

            {"label": "1", "row": 5, "col": 0},
            {"label": "2", "row": 5, "col": 1},
            {"label": "3", "row": 5, "col": 2},
            {"label": "=", "row": 5, "col": 3, "rowspan": 2},

            {"label": "0", "row": 6, "col": 0, "columnspan": 2},
            {"label": ",", "row": 6, "col": 2},
        ]

        for button in BUTTON_LAYOUT:
            self.create_button(
                label=button["label"],
                command=None,  # Placeholder for button functionality
                col=button["col"],
                row=button["row"],
                width=50,
                columnspan=button.get("columnspan", 1),
                rowspan=button.get("rowspan", 1)
            )

    # Creates label and places in correct space
    def create_label(self):
        # Creates Label
        text = """
            Welcome to the Calculator!\n
            Either Reverse Polish Notation or Infix Notation can be used to calculate expressions.\n
        """
        self.label = Label(self, text=text)
        self.label.grid(row=0, column=0, columnspan=4, rowspan=1, sticky="nsew")

    # Creates text widget to display input and output
    def create_text(self, col=0, row=0, columnspan=4, rowspan=1):
        text = MyText(self, width = 100, height = 5)
        text.grid(
            row=row, 
            column=col, 
            columnspan=columnspan, 
            rowspan=rowspan,
            sticky="nsew"
        )

        # Returns text widget
        # This will be used later for the input and output
        return text

    # Populates the frame 
    def populate_frame(self):

        # Creates label to display welcome message and instructions
        self.create_label()

        # Creates text widget that displays input and output
        self.display = self.create_text(col=0, row=1, 
                                  columnspan=4, rowspan=1)

        self.button_grid()
        