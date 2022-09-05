from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string("""
<ScreenSeven>:
    name: "scr 1A"
    MDRaisedButton:
        text: "Send Now"
        adaptive_height:True
        pos_hint:{'center_y':.6, 'center_x': .5}
        on_release:
            app.scr_2A()


    MDRaisedButton:
        text: "Send Later"
        adaptive_height:True
        pos_hint:{'center_y':.4, 'center_x': .5}
        on_release:
            app.scr_2()



""")


class ScreenSeven(Screen):
    pass