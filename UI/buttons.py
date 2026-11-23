from collections.abc import Callable
from tkinter import ttk

# This class is a wrapper for the ttk.Button widget,
# allowing for easier creation of buttons with specified labels and commands.
# Using type hints for ease of review
class MyButton(ttk.Button):
    def __init__(
            self, 
            parent, 
            label: str, 
            command: Callable[[], None] | None = None, 
            width: int =50
        ) -> None:
            super().__init__(
                parent,
                text=label,
                command=command,
                width=width,
                padding=(0,10)
            )

    # This will be changed and fleshed out later
    def set_command(self, command: Callable[[], None] | None) -> None:
        self['command'] = command
