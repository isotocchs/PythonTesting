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


class WidgetExample(GridLayout):
    count = 0
    countEnabled = BooleanProperty(False)
    myText = StringProperty("Hello")
    sliderValueText = StringProperty("Value")
    def onButtonClick(self):
        print("Button Clicked")
        if self.countEnabled:
            self.count +=1
            self.myText = "You Clicked the button."
            self.myText = str(self.count)
            
    def onToggleButton(self, toggleSelf):
        print("The State of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.countEnabled = False
        else:
            toggleSelf.text = "ON"
            self.countEnabled = True
            
    def switchOnOff(self, switchSelf):
        print("The state of the switch: "+str(switchSelf.active))
    def sliderValue(self, sliderSelf):
        print("Slider Value: "+str(int(sliderSelf.value)))
        self.sliderValueText = str(int(sliderSelf.value))
        
class ScrollViewEx(ScrollView):
    pass

class StackLayoutEx(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        # eijurgb=Button(text="A", size_hint=(.2,.2))
        # self.add_widget(eijurgb)
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
        for i in range(0,100):
            b2=Button(text=str(i+1), size_hint=(None,None), size=(dp(100),dp(100)))
            self.add_widget(b2)
    #pass


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



























