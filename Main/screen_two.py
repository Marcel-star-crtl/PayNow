from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string("""
<ScreenTwo>:
    name: "scr 2"
    MDLabel:
        text:'Person'
        halign: 'center'
        font_style: 'H2'
        pos_hint:{'center_y':0.7}
    MDTextField:
        id : task_text
        size_hint:(0.7,0.1)
        pos_hint:{'center_x':0.5,'center_y':0.45}
        hint_text:'Enter Person Number'
        
    MDTextField:
        id : task_text
        size_hint:(0.7,0.1)
        pos_hint:{'center_x':0.5,'center_y':0.55}
        hint_text:'Enter Person Name'
        
    MDRaisedButton:
        text:'Add Person'
        pos_hint: {'center_x':0.5,'center_y':0.35}
        on_press:
            app.person()


""")


class ScreenTwo(Screen):
    pass