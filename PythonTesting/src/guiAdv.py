from kivy.app import App
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, BooleanProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.actionbar import ActionBar, ActionBarException, ActionButton, ActionItem, ActionView
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.metrics import dp

#Define different Screens
class HomeScreen(Screen):
    pass

class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100,100,400,400), width=2)
            Color(0,0,1)
            Line(circle=(300,300,80), width=4)
            Line(rectangle=(200,200,80,100), width=2)
            self.rect = Rectangle(pos=(500,300),size=(50,100))
    def on_button_press(self):
        #self.rect.pos = (500,50)
        x,y = self.rect.pos
        x += dp(5)
        self.rect.pos = (x,y)
            


class guiAdvKv(App):
    pass

guiAdvKv().run()