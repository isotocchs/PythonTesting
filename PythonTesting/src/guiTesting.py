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

class ScrollViewEx(ScrollView):
    pass

class StackLayoutEx(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        b=Button(text="A", size_hint=(.2,.2))
        self.add_widget(b)
        # for i in range(0,10):
        #     b2=Button(text=str(i+1), size_hint=(.2,.2))
        #     self.add_widget(b2)
        # for i in range(0,10):
        #     b2=Button(text=str(i+1), size_hint=(None,None), size=(dp(100),dp(100)))
        #     self.add_widget(b2)
        # for i in range(0,10):
        #     size = dp(100)+i*10
        #     b2=Button(text=str(i+1), size_hint=(None,None), size=(size,size))
        #     self.add_widget(b2)
        # for i in range(0,100):
        #     b2=Button(text=str(i+1), size_hint=(None,None), size=(dp(100),dp(100)))
        #     self.add_widget(b2)

class GridLayoutEx(GridLayout):
    pass

class BoxLayoutEx(BoxLayout):
    # pass
    #create constructor, need **kwargs for kivy - allows you to use keywords and arguments
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     # create button for layout (Default to horizontal layout)
    #     #self.orientation = "vertical"
    #     b1 = Button(text="CodeButton")
    #     b2 = Button(text="CodeButton 2")
    #     b3 = Button(text="CodeButton 3")
    #     #order of add_widgets is the order that the buttons are displayed
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)
    pass    

class AnchorLayoutEx(AnchorLayout):
    pass

class NotMainWidget(Widget):
    pass
# dp for density independent pixels. Always the same size no matter the device.
# color is in R, G, B, Alpha(visibility) - 1 = 100%, 0.5=50%, 

class GuiStuff(App):
    pass



GuiStuff().run()



























