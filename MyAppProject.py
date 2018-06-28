from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

kv = Builder.load_string('''
<CustomButton@Button>:
    font_size:30
<CalcLayout>:
    id:Calculator
    display:txtinpt
    rows:5
    spacing:10
    padding:10
    
    BoxLayout:
        TextInput:
            id: txtinpt
            font_size:30
            multiline:False
            readonly:True
    BoxLayout:
        spacing:10
        
        CustomButton:
            text: "7"
            on_press: txtinpt.text += self.text
        CustomButton:
            text: "8"
            on_press: txtinpt.text += self.text
        CustomButton:
            text: "9"
            on_press: txtinpt.text += self.text
        CustomButton:
            text: "/"
            on_press:txtinpt.text += self.text
    BoxLayout:
        spacing:10
        
        CustomButton:
            text: "4"
            on_press: txtinpt.text += self.text
        CustomButton:
            text: "5"
            on_press: txtinpt.text += self.text
        CustomButton:
            text: "6"
            on_press: txtinpt.text += self.text
        CustomButton:
            text: "*"
            on_press: txtinpt.text += self.text
    BoxLayout:
        spacing:10
        
        CustomButton:
            text: "1"
            on_press: txtinpt.text += self.text
        CustomButton:
            text: "2"
            on_press: txtinpt.text += self.text
        CustomButton:
            text: "3"
            on_press: txtinpt.text += self.text
        CustomButton:
            text: "-"
            on_press: txtinpt.text += self.text
    BoxLayout:
        spacing:10
        
        CustomButton:
            text: "Clear"
            on_press: txtinpt.text = ""
        CustomButton:
            text: "0"
            on_press: txtinpt.text += self.text
        CustomButton:
            text: "="
            on_press:Calculator.Calculate(txtinpt.text)
        CustomButton:
            text: "+"
            on_press: txtinpt.text += self.text
        
        
    ''')

class CalcLayout(GridLayout):

    def Calculate(self,parameter):
        if parameter:
            try:
               self.display.text = str(eval(parameter))
               
            except Exception:
                self.display.text = "Wrong Input"

class MyProject(App):
    
    def build(self):
        return CalcLayout()

if __name__ == "__main__":
    MyProject().run()
