from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string("""
<ScreenSix>:
    name: "scr 6"
    ScrollView:
        MDList:
            id:person_details

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x':0.3,'center_y':0.2}
        on_press:
            root.manager.current = "scr 2"


""")


class ScreenSix(Screen):
    pass