from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

class temporizadorApp(App):
    def build(self):
        tela = (300, 400)
        Window.size = tela
        return tempVisita()

class tempVisita(FloatLayout):
    pass


temporizadorApp().run()

