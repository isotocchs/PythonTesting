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


class WidgetExample(GridLayout):
    count = 0
    countEnabled = BooleanProperty(False)
    myText = StringProperty("Counter")
    typingText = StringProperty("")
    sliderValueText = StringProperty("Value")
    myTextBoxInput = StringProperty("")
    def __init__(self, **kwargs):
        super(WidgetExample, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')
        if self._keyboard.widget:
            # If it exists, this widget is a VKeyboard object which you can use
            # to change the keyboard layout.
            pass
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print('The key', keycode, 'have been pressed')
        print(' - text is %r' % text)
        print(' - modifiers are %r' % modifiers)
        self.typingText = text
    
    def onButtonClick(self):
        print("Button Clicked")
        if self.countEnabled:
            self.count +=1
            #self.myText = "You Clicked the button."
            self.myText = str(self.count)
            
    def onToggleButton(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.countEnabled = False
        else:
            toggleSelf.text = "ON"
            self.countEnabled = True
            
    def switchOnOff(self, switchSelf):
        print("The state of the switch: "+str(switchSelf.active))
    def sliderValue(self, sliderSelf):
        print("Slider Value: "+str(sliderSelf.value))
        self.sliderValueText = str(int(sliderSelf.value))
        
    def onTextValidate(self, textBoxSelf):
        self.myTextBoxInput = textBoxSelf.text
        
class ScrollViewEx(ScrollView):
    pass

class StackLayoutEx(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "rl-tb"
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

class StackLayoutEx2(StackLayout):
    moveEnabled2 = BooleanProperty(False)
    moveEnabled3 = BooleanProperty(False)
    moveEnabled4 = BooleanProperty(False)
    moveEnabled5 = BooleanProperty(False)
    moveEnabled6 = BooleanProperty(False)
    moveEnabled7 = BooleanProperty(False)
    moveEnabled8 = BooleanProperty(False)
    moveEnabled9 = BooleanProperty(False)
    moveEnabled10 = BooleanProperty(False)
    moveEnabled11 = BooleanProperty(False)
    moveEnabled12 = BooleanProperty(False)
    moveEnabled13 = BooleanProperty(False)
    moveEnabled14 = BooleanProperty(False)
    moveEnabled15 = BooleanProperty(False)
    moveEnabled16 = BooleanProperty(False)
    moveEnabled17 = BooleanProperty(False)
    moveEnabled18 = BooleanProperty(False)
    moveEnabled19 = BooleanProperty(False)
    moveEnabled20 = BooleanProperty(False)
    moveEnabled21 = BooleanProperty(False)
    moveEnabled22 = BooleanProperty(False)
    moveEnabled23 = BooleanProperty(False)
    moveEnabled24 = BooleanProperty(False)
    moveEnabled25 = BooleanProperty(False)
    def onToggleButton2(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled2 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled2 = True
    def onToggleButton3(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled3 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled3 = True
    def onToggleButton4(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled4 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled4 = True
    def onToggleButton4L(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "Dead end!"
            self.moveEnabled4L = False
        else:
            toggleSelf.text = "Dead end!"
            self.moveEnabled4L = True
    def onToggleButton5(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled5 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled5 = True
    def onToggleButton5L(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "Dead end!"
            self.moveEnabled5L = False
        else:
            toggleSelf.text = "Dead end!"
            self.moveEnabled5L = True
    def onToggleButton6(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled6 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled6 = True 
    def onToggleButton7(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled7 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled7 = True
    def onToggleButton7L(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "Dead end!"
            self.moveEnabled7L = False
        else:
            toggleSelf.text = "Dead end!"
            self.moveEnabled7L = True
    def onToggleButton8(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled8 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled8 = True 
    def onToggleButton9(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled9 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled9 = True
    def onToggleButton10(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled10 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled10 = True
    def onToggleButton11(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled11 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled11 = True
    def onToggleButton12(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled12 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled12 = True 
    def onToggleButton13(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled13 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled13 = True 
    def onToggleButton14(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled14 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled14 = True 
    def onToggleButton15(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled15 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled15 = True
    def onToggleButton15L(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "Dead end!"
            self.moveEnabled15L = False
        else:
            toggleSelf.text = "Dead end!"
            self.moveEnabled15L = True
    def onToggleButton16(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled16 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled16 = True
    def onToggleButton16L(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "Dead end!"
            self.moveEnabled16L = False
        else:
            toggleSelf.text = "Dead end!"
            self.moveEnabled16L = True
    def onToggleButton17(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled17 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled17 = True 
    def onToggleButton18(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled18 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled18 = True 
    def onToggleButton19(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled19 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled19 = True
    def onToggleButton20(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled20 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled20 = True
    def onToggleButton21(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled21 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled21 = True
    def onToggleButton21L(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "Dead end!"
            self.moveEnabled21L = False
        else:
            toggleSelf.text = "Dead end!"
            self.moveEnabled21L = True
    def onToggleButton22(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled22 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled22 = True 
    def onToggleButton23(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled23 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled23 = True 
    def onToggleButton24(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled24 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled24 = True 
    def onToggleButton25(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled25 = False
        else:
            toggleSelf.text = "ON"
            self.moveEnabled25 = True
    def onToggleButton25W(self, toggleSelf):
        print("The state of the toggle: "+toggleSelf.state)
        if toggleSelf.state == "normal":
            toggleSelf.text = "OFF"
            self.moveEnabled25W = False
        else:
            toggleSelf.text = "You Win!"
            self.moveEnabled25W = True
            
import kivy

from kivy.app import App

from kivy.uix.gridlayout import GridLayout

from kivy.config import Config



class CalculatorGridLayout(GridLayout):

    def calculate(self, calculation):

        if calculation:

            try:

                self.display.text = str(eval(calculation))

            except Exception:

                self.display.text = "Error"

                

class CalculatorApp(App):

    def build(self):

        return CalculatorGridLayout()

    

calculateApp = CalculatorApp()

calculateApp.run()

class GuiStuff(App):
    pass



GuiStuff().run()



























