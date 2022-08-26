from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivy.core.window import Window

from kivymd.app import MDApp

# Window.size = (400, 600)

Builder.load_string('''

<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineIconListItem:
                text: "Profile"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"                

                IconLeftWidget:
                    icon: "face-profile"

            OneLineIconListItem:
                text: "list"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"

                IconLeftWidget:
                    icon: "upload"

            OneLineIconListItem:
                text: "Logout"
                IconLeftWidget:
                    icon: "logout" 


<MainWidget@Screen>:

    MDTopAppBar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Crazy App"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                name: "scr 1"

                MDLabel:
                    text: "Screen 1"
                    halign: "center"

            Screen:
                name: "scr 2"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation: 'vertical'
                # padding: dp(15)                                    
                # spacing: dp(50) # Aproxima os campos de cima para baixo  

                RelativeLayout:
                    size_hint_y: None
                    height: "200dp"
                                
                    canvas:
                        Color:
                            rgba: app.theme_cls.primary_color
                        Rectangle:
                            pos: self.pos
                            size: self.size                    
                    
                    BoxLayout:
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.7, 'center_y': .5}
                        spacing: dp(2)

                        canvas:
                            Rectangle:
                                size: self.size
                                source: "celebrate.jpg"

                        FitImage:
                            size_hint: None, None
                            radius: [70, 70, 70, 70]
                            width: dp(150)
                            height: dp(150)
                            source: "dummy_user.jpg"
                            pos_hint: {"top": 0.9}

                        # Foto:
                        #     pos_hint: {"top": 0.9}

                        MDLabel:
                            text: "Ahh  Marcel"
                            font_style: "Subtitle1"
                            #halign: "center"

                            theme_text_color: "Custom"                            
                            text_color: 10, 10, 10, 1

                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "email@doMarcel.com"
                            #halign: "center"

                            theme_text_color: "Custom"                            
                            text_color: 10, 10, 10, 1

                            size_hint_y: None
                            font_style: "Caption"
                            height: self.texture_size[1] 

                ContentNavigationDrawer:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer
''')


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class CrazyApp(MDApp):
    def build(self):
        return Factory.MainWidget()


CrazyApp().run()