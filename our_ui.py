import time
from pymata4 import pymata4
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

num_steps = 600
pins = [8, 9, 10, 11]
board = pymata4.Pymata4()

board.set_pin_mode_stepper(num_steps, pins)


class MyGridLayout(Widget):
    
    #degree_input = ObjectProperty(None)
    
    global degree_value
    
    degree_value = 0
    
    def slide_it(self, *args):
        #print(args[1])
        global degree_value
        degree_value = int(args[1])
        self.slide_text.text = str(degree_value)
        
    def press(self):
        # variable = self.name_of_variable.text
        #self.add_widget(Label(text="initiating..."))
        
        steps = round(degree_value * (5.556))
        board.stepper_write(20, steps)
        time.sleep(1)
        
        
    
class MyApp(App):
    def build(self):
        return MyGridLayout()
    

if __name__ == '__main__':
    MyApp().run()