from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string("""
<ScreenFive>:
    name: "scr 5"
    MDLabel:
        text: "About Us"
        halign: "center"
        font_style:'H5'
        adaptive_height:True
        pos_hint:{'center_y':.7}
        
    MDLabel:
        text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit ipsa dolore aspernatur doloremque sequi aperiam itaque nemo? Id reprehenderit ad explicabo tenetur. Quibusdam architecto sapiente rem odio, omnis sit quisquam!"
        halign: "center"
        font_style:'H5'
        adaptive_height:True
        pos_hint:{'center_y':.5}


""")


class ScreenFive(Screen):
    pass