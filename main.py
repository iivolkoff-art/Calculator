from kivy.core.window import Window
from Calculator import CalculatorApp

Window.size = (400, 400)
Window.clearcolor = (28/255, 26/255, 40/255 , 1)

if __name__ == '__main__':
    CalculatorApp().run()