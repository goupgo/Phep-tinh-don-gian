import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class MyRoot(BoxLayout):
    
    def __init__(self):
        super(MyRoot, self).__init__()

    def add(self):
        x = int(self.num1.text)
        y = int(self.num2.text)
        add = x + y
        self.res.text = str(add)
    
    def sub(self):
        x = int(self.num1.text)
        y = int(self.num2.text)
        sub = x - y
        self.res.text = str(sub)
    
    def mul(self):
        x = int(self.num1.text)
        y = int(self.num2.text)
        mul = x * y
        self.res.text = str(mul)
    
    def div(self):
        x = int(self.num1.text)
        y = int(self.num2.text)
        div = round((x / y), 2)
        self.res.text = str(div)


class NeuralRandom(App):
    
    def build(self):
        return MyRoot()
    
neuralRandom = NeuralRandom()
neuralRandom.run()