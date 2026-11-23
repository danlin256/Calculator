from UI.myText import MyText
from tkinter import Frame
from UI.buttons import MyButton
from UI.myLabels import MyLabel

class MyFrame(Frame):
    def __init__(self, root, height, width):
        super().__init__(root, height=height, width=width)

        self.pack(fill="both", expand=True)

        self.create_grid(7, 4)  # Creates a grid with 7 rows and 4 columns

        self.populate_Frame()  # Populates the frame with buttons and labels

    # Creates a grid layout for the frame with specified number of rows and columns
    def create_grid(self, rows, columns):
        for i in range(rows):
            self.rowconfigure(i, weight=1)
        for j in range(columns):
            self.columnconfigure(j, weight=1)

        self.rowconfigure(rows, weight=1)  # Adds an extra row for the text widget

    # Creates button and places in correct space
    # Functionality can be passed in as argument
    def create_button(self, label, command, col, row, width, columnspan=1, rowspan=1):
        but = MyButton(self, label, command, width=width)
        but.grid(row=row, column=col, columnspan=columnspan, rowspan=rowspan, sticky="nsew")  # Spans across the specified number of columns and fills the space

    # Creates label and places in correct space
    def create_label(self, text, col=0, row=0, columnspan=4, rowspan=1):
        label = MyLabel(self, text)
        label.grid(row=row, column=col, columnspan=columnspan, rowspan=rowspan, sticky="nsew")  # Spans across the specified number of columns and fills the space

    # Creates text widget to display input and output
    def create_text(self, col=0, row=0, columnspan=4, rowspan=1):
        text = MyText(self, width = 100, height = 5)
        text.grid(row=row, column=col, columnspan=columnspan, rowspan=rowspan)

    # Populates the frame with buttons and labels
    def populate_Frame(self):

        # Creates Label
        self.create_label(
        """
        Welcome to the Calculator!\n
        Either Reverse Polish Notation or Infix Notation can be used to calculate expressions.\n
        """
        )

        # Creates text widget that displays input and output
        texter = self.create_text(col=0, row=1, 
                                  columnspan=4, rowspan=1)

        
        arr1 = [['C', '/', '*', '-'],
                ['7', '8', '9', '+'],
                ['4', '5', '6', '+'],
                ['1', '2', '3', '='],
                ['0', '0', '.', '=']
                ]

        buttons = []

        for i in range(len(arr1)):
            for j in range(len(arr1[i])):
                match arr1[i][j]:
                    case '+':
                        if i != 2:
                            self.create_button(label=arr1[i][j], 
                                            command=None, 
                                            col=j, row=i+2, 
                                            width=50, 
                                            columnspan=1, rowspan=2)
                            buttons.append(arr1[i][j])
                    case '=':
                        if i != 4:
                            self.create_button(label=arr1[i][j], 
                                               command=None, 
                                               col=j, row=i+2, 
                                               width=50, 
                                               columnspan=1, rowspan=2)
                            buttons.append(arr1[i][j])
                    case '0':
                        if j == 0:
                            self.create_button(label=arr1[i][j], 
                                                command=None, 
                                                col=j, row=i+2, 
                                                width=50, 
                                                columnspan=2, rowspan=1)
                        
                            buttons.append(arr1[i][j])
                    case _:
                        self.create_button(label=arr1[i][j], 
                                            command=None, 
                                            col=j, row=i+2, 
                                            width=50, 
                                            columnspan=1, rowspan=1)
                        buttons.append(arr1[i][j])