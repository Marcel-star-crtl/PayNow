from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string("""
<ScreenFour>:
    name: "scr 4"
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "280dp", "180dp"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDLabel:
            text: "Title"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: self.texture_size[1]

        MDSeparator:
            height: "1dp"

        MDLabel:
            text: "Body"


""")


class ScreenFour(Screen):
    pass