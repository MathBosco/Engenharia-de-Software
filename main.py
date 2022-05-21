from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import finder 

# Classes com as telas
class Resultados(Screen):
    ...

class Inicial(Screen):
    def busca(self):
        comida = self.ids.mealType.text
        local = self.ids.location.text

        resposta = finder.findARestaurant(comida, local)

class TelaLogin(Screen):
    ...

# Screen manager
sm = ScreenManager()
sm.add_widget(TelaLogin(name='tela_login'))
sm.add_widget(Inicial(name='inicial'))
sm.add_widget(Resultados(name='resultados'))

# Construção principal do app
class Myapp(MDApp):
    def build(self):
        return Builder.load_file('interface.kv')
    
# Inicia o aplicativo
Myapp().run()