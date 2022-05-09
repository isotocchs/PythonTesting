from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line


class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    
    number_of_vertical_lines = 7
    vertical_line_spacing = .1 #percentage in screen width
    verical_lines_array = []

    def __init__(self, **kwargs):
        super(MainWidget,self).__init__(**kwargs)
        self.init_vertical_lines()
    
    
    def on_size(self,*args):
        print("Width: "+str(self.width)+" Height: "+str(self.height))
        self.perspective_point_x = self.width/2
        self.perspective_point_y = self.height*0.75
        self.update_vertical_lines()
    
    def on_perspective_point_x(self,widget,value):
        print("Pers X: "+str(value))
    def on_perspective_point_y(self,widget,value):
        print("Pers Y: "+str(value))
        
    def init_vertical_lines(self):
        with self.canvas:
            Color(1,1,1)
            #create my vertical lines in loop
            for i in range(0,self.number_of_vertical_lines):
                self.verical_lines_array.append(Line())
            
            
    def update_vertical_lines(self):
        center_x = int(self.width/2)
        spacing = self.vertical_line_spacing*self.width
        offset_for_lines = -int(self.number_of_vertical_lines/2)
        for i in range(0,self.number_of_vertical_lines):
                line_x = int(center_x+offset_for_lines*spacing)
                
                x1,y1 = self.transform(line_x, 0)
                x2,y2 = self.transform(line_x,self.height)
                
                self.verical_lines_array[i].points = (x1,y1,x2,y2)
                offset_for_lines+=1
    
    
    
    def transform(self,x,y):
        #return self.transform_2D(x,y)
        return self.transform_perspective(x,y)
    
    def transform_2D(self,x,y):
        return int(x),int(y)
    
    def transform_perspective(self,x,y):
        transformed_y = y*self.perspective_point_y/self.height
        if transformed_y > self.perspective_point_y:
            transformed_y = self.perspective_point_y
        
        diff_x = x - self.perspective_point_x
        diff_y = self.perspective_point_y - transformed_y
        proportion_y = diff_y/self.perspective_point_y  
        transformed_x = self.perspective_point_x+diff_x*proportion_y
        
        return int(transformed_x),int(transformed_y)
        
class GameApp(App):
    pass

GameApp().run()