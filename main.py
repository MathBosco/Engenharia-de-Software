from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.card import MDCard
import finder 

class ResultadosCard(MDCard):
    ...

class Inicial(MDFloatLayout):
    ...


class TelaLogin(MDFloatLayout):
    def abrir_main(self):
        # self.add_widget(Inicial())
        ...

# Construção principal do app
class Myapp(MDApp):
    def build(self):
        return Builder.load_file('interface.kv')
    
# Inicia o aplicativo
Myapp().run()