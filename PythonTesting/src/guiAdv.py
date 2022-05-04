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
from kivy.graphics.vertex_instructions import Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import Clock

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
            # Line(points=(100,100,400,400), width=2)
            # Color(0,0,1)
            # Line(circle=(300,300,80), width=4)
            # Line(rectangle=(200,200,80,100), width=2)
            #Rectangle(pos=(500,300),size=(50,100))
            self.rect = Rectangle(pos=(500,300),size=(50,100))
    def on_button_press_right(self):
        x,y = self.rect.pos
        width, height = self.rect.size
        increase = dp(20)
        remainingSpace = self.width - (x+width)
        
        if remainingSpace < increase:
            increase = remainingSpace
            
        x += increase
        self.rect.pos = (x,y)
        
        
    def on_button_press_left(self):
        x,y = self.rect.pos
        width, height = self.rect.size
        increase = dp(20)
        remainingSpace = 0+x
        
        if remainingSpace < increase:
            increase = remainingSpace
            
        x -= increase
        self.rect.pos = (x,y)
    def on_button_press_up(self):
        x,y = self.rect.pos
        width, height = self.rect.size
        increase = dp(20)
        remainingSpace = self.height - (y+height)
        
        if remainingSpace < increase:
            increase = remainingSpace
            
        y += increase
        self.rect.pos = (x,y)
    def on_button_press_down(self):
        x,y = self.rect.pos
        width, height = self.rect.size
        increase = dp(20)
        remainingSpace = 0+y
        
        if remainingSpace < increase:
            increase = remainingSpace
            
        y -= increase
        self.rect.pos = (x,y)
            
class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.time_in_seconds = 1/60
        self.ball_speed_x = dp(5)
        self.ball_speed_y = dp(5)
        with self.canvas:
            self.ball = Ellipse(pos=(200,200),size=(self.ball_size,self.ball_size))
        Clock.schedule_interval(self.update_motion, self.time_in_seconds)
         
    def on_size(self,*args):
        self.ball.pos =  (self.center_x-self.ball_size/2,self.center_y-self.ball_size/2)   
        
    def update_motion(self,dt):
        x,y = self.ball.pos
        x += self.ball_speed_x
        y += self.ball_speed_y
        
        
        
        self.ball.pos = (x,y)
        
        
        
        
class guiAdvKv(App):
    pass

guiAdvKv().run()