from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string("""
<ScreenOne>:
    name: "scr 1"
    MDLabel:
        text: "Enter Number For Transactions"
        halign: "center"
        font_style:'H5'
        adaptive_height:True
        pos_hint:{'center_y':.7}
        
    MDFloatLayout: 
        size_hint: .5, .09
        pos_hint: {'center_x': .5, 'center_y': .5}
        canvas:
            Color:
                rgb: 1, 1, 1, 1
            RoundedRectangle:
                size: self.size
                pos: self.pos 
                radius: [6]
        canvas.before:
            Color:
                rgb: 200/255, 200/255, 200/255
            Line:
                width: 2
                rounded_rectangle: self.x, self.y, self.width, self.height, 6, 6, 6, 6, 100
        
        TextInput:
            id: number
            hint_text: "Number"
            size_hint: 1, None 
            pos_hint: {'center_x': .5, 'center_y': .5}
            height: self.minimum_height
            multiline: False
            font_size: "18sp"
            hint_text_color: 170/255, 170/255, 170/255, 1
            background_color: 1, 1, 1, 0
            padding: 13
            cursor_color: 0, 0, 0, 1
        
    MDRaisedButton:
        text: "Save"
        adaptive_height:True
        pos_hint:{'center_y':.3, 'center_x': .5}
        on_release:
            app.scr_1A()
        
    

""")

class ScreenOne(Screen):
    pass