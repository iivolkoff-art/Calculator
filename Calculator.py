from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class CalculatorApp(App):
    def build(self):
        self.formula = '0'
        bl = BoxLayout(orientation='vertical', spacing=2)
        gl = GridLayout(cols=3, rows = 6, size_hint=(1, .6), spacing=5, padding=5)

        self.lbl = Label(text='0', font_size = 50, size_hint = (1, .4), halign = 'right', valign = 'bottom', text_size = (400 - 50, 400 * .4 - 50))
        bl.add_widget(self.lbl)

        for i in range(9):
            gl.add_widget(Button(text=str(i + 1), background_color=(28/255, 26/255, 43/255, 1), background_normal='', font_size = 25, on_press = self.add_number))
        gl.add_widget(Button(text='*', background_color=(28 / 255, 26 / 255, 43 / 255, 1), background_normal='', font_size = 25, on_press = self.add_operation))
        gl.add_widget(Button(text='0', background_color=(28 / 255, 26 / 255, 43 / 255, 1), background_normal='', font_size = 25, on_press = self.add_number))
        gl.add_widget(Button(text='/', background_color=(28 / 255, 26 / 255, 43 / 255, 1), background_normal='', font_size = 25, on_press = self.add_operation))
        gl.add_widget(Button(text='+', background_color=(28 / 255, 26 / 255, 43 / 255, 1), background_normal='', font_size = 25, on_press = self.add_operation))
        gl.add_widget(Button(text='.', background_color=(28 / 255, 26 / 255, 43 / 255, 1), background_normal='', font_size=25,on_press=self.add_operation))
        gl.add_widget(Button(text='-', background_color=(28 / 255, 26 / 255, 43 / 255, 1), background_normal='', font_size = 25, on_press = self.add_operation))
        gl.add_widget(Button(text='AC', background_color=(28 / 255, 26 / 255, 43 / 255, 1), background_normal='', font_size=25,on_press=self.clear))
        gl.add_widget(Button(text='<<', background_color=(28 / 255, 26 / 255, 43 / 255, 1), background_normal='', font_size = 25, on_press = self.clear_one))
        gl.add_widget(Button(text='=', background_color=(28 / 255, 26 / 255, 90 / 255, 1), background_normal='', font_size = 25, on_press = self.result))

        bl.add_widget(gl)
        return bl

    def add_number(self, instance):
        if(self.formula[:] == '0'):
            self.formula = ''
        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        self.formula += str(instance.text)
        self.update_label()

    def update_label(self):
        self.lbl.text = self.formula

    def result(self, instance):
        try:
            self.lbl.text = str(eval(self.lbl.text))
        except:
            self.lbl.text = 'Error'
            self.formula = '0'

    def clear(self, instance):
        self.formula = '0'
        self.update_label()

    def clear_one(self, instance):
        self.formula = self.formula[:-1] or '0'
        self.update_label()
