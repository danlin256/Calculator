from arithOp import add
from UI.window import CalculatorWindow

if __name__ == "__main__":
    print(add(2, 2))
    
    window = CalculatorWindow(600, 800)

    window.window_run()