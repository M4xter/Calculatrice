from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

class Calculatrice(BoxLayout):

    def calculer(self, expression):
        if expression:
            try:
                self.display.text = str(eval(expression))
            except Exception:    
                self.display.text = 'Erreur'

    def reinitialiser(self, expression):
        if expression:
            self.display.text = ''

class calculatriceApp(App):
    def build(self):
        self.title = 'Calculatrice'    

Config.set('graphics','width','250')
Config.set('graphics','height','415')

calculatriceApp().run()