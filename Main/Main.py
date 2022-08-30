from kivy.config import Config
Config.set('kivy', 'exit_on_escape', '0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.list import OneLineListItem
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from kivymd.app import MDApp

Window.size = (500, 650)

Builder.load_string('''

<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineIconListItem:
                text: "Start"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"                

                IconLeftWidget:
                    icon: "restart"

            OneLineIconListItem:
                text: "list"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"

                IconLeftWidget:
                    icon: "view-list"

            OneLineIconListItem:
                text: "Contact Us"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 3"                

                IconLeftWidget:
                    icon: "contacts"
                    
            OneLineIconListItem:
                text: "History"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 4"                

                IconLeftWidget:
                    icon: "history"
                    
            OneLineIconListItem:
                text: "About Us"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 5"                

                IconLeftWidget:
                    icon: "account-group"

            OneLineIconListItem:
                text: "Logout"
                IconLeftWidget:
                    icon: "logout" 
 
 
<MainWidget@Screen>:
    MDTopAppBar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "PayNow"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        
        FitImage:
            size_hint: None, None
            width: dp(25)
            height: dp(25)
            source: "images/notification.png"
            pos_hint: {"center_x": .91, "center_y": .09}
        
    IconLeftWidget:
        icon: "arrow-up-drop-circle-outline"
        on_release: app.show_example_grid_bottom_sheet()
        pos_hint: {"center_x": .5, "center_y": .1}
        adaptive_height:True

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
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
                    
                    

            Screen:
                name: "scr 2"

                MDLabel:
                    text:'Person'
                    halign: 'center'
                    font_style: 'H2'
                    pos_hint:{'center_y':0.8}
                MDTextField:
                    id : task_text
                    size_hint:(0.7,0.1)
                    pos_hint:{'center_x':0.5,'center_y':0.55}
                    hint_text:'Enter Person Details'
                MDRaisedButton:
                    text:'Add Person'
                    pos_hint: {'center_x':0.5,'center_y':0.35}
                    on_press:
                        app.Person()
                    
                    
            Screen:
                name: "scr 3"

                MDLabel:
                    text: "Contact Us"
                    pos_hint: {'center_X': .5, 'center_y': .8}
                    halign: "center"
                    font_style:'H5'
                    font_size: "26sp"
                    
                MDFloatLayout: 
                    size_hint: .9, .09
                    pos_hint: {'center_x': .5, 'center_y': .7}
                    canvas:
                        Color:
                            rgb: 1, 1, 1, 1
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos 
                            radius: [6]
                    canvas.before:
                        Color:
                            rgb: 230/255, 230/255, 230/255
                        Line:
                            width: 2
                            rounded_rectangle: self.x, self.y, self.width, self.height, 6, 6, 6, 6, 100
                            
                    TextInput:
                        id: name
                        hint_text: "Name"
                        size_hint: 1, None 
                        pos_hint: {'center_x': .5, 'center_y': .7}
                        height: self.minimum_height
                        multiline: False
                        font_size: "18sp"
                        hint_text_color: 170/255, 170/255, 170/255, 1
                        background_color: 1, 1, 1, 0
                        padding: 13
                        cursor_color: 0, 0, 0, 1
                
                MDFloatLayout: 
                    size_hint: .9, .09
                    pos_hint: {'center_x': .5, 'center_y': .6}
                    canvas:
                        Color:
                            rgb: 1, 1, 1, 1
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos 
                            radius: [6]
                    canvas.before:
                        Color:
                            rgb: 230/255, 230/255, 230/255
                        Line:
                            width: 2
                            rounded_rectangle: self.x, self.y, self.width, self.height, 6, 6, 6, 6, 100
                            
                    TextInput:
                        id: email
                        hint_text: "Email"
                        size_hint: 1, None 
                        pos_hint: {'center_x': .5, 'center_y': .6}
                        height: self.minimum_height
                        multiline: False
                        font_size: "18sp"
                        hint_text_color: 170/255, 170/255, 170/255, 1
                        background_color: 1, 1, 1, 0
                        padding: 13
                        cursor_color: 0, 0, 0, 1
                    
                MDFloatLayout: 
                    size_hint: .9, None
                    height: 160
                    pos_hint: {'center_x': .5, 'center_y': .41}
                    canvas:
                        Color:
                            rgb: 1, 1, 1, 1
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos 
                            radius: [6]
                    canvas.before:
                        Color:
                            rgb: 230/255, 230/255, 230/255
                        Line:
                            width: 2
                            rounded_rectangle: self.x, self.y, self.width, self.height, 6, 6, 6, 6, 100
                            
                    TextInput:
                        id: message
                        hint_text: "Message"
                        size_hint: 1, None 
                        pos_hint: {'center_x': .5, 'center_y': .41}
                        height: 160
                        font_size: "18sp"
                        hint_text_color: 170/255, 170/255, 170/255, 1
                        background_color: 1, 1, 1, 0
                        padding: 13
                        cursor_color: 0, 0, 0, 1
                        
                    Button: 
                        text: "send"
                        size_hint: .9, .2
                        pos_hint: {'center_x': .5, 'center_y': .000001}
                        back_color: 1, 1, 1, 0
                        color: 1, 1, 1, 1
                        on_release: app.send_emails(name, message)
                        canvas.before:
                            Color:
                                rgb: 71/255, 104/255, 237/255, 1
                            RoundedRectangle:
                                size: self.size
                                pos: self.pos
                                radius: [6]
                        
            Screen:
                name: "scr 4"

                MDLabel:
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
                
            Screen:
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
            Screen:
                name: "scr 6"

                ScrollView:
                    MDList:
                        id:person_details
            
                MDRaisedButton:
                    text: 'Back'
                    pos_hint: {'center_x':0.3,'center_y':0.2}
                    on_press:
                        root.manager.current = "scr 2"

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


class PayNow(MDApp):
    def build(self):
        Window.bind(on_request_close=self.on_request_close)
        return Factory.MainWidget()

    def on_request_close(self, *args):
        self.textpopup(title='Exit', text='Are you sure?')
        return True

    def textpopup(self, title='', text=''):
        """Open the pop-up with the name.

        :param title: title of the pop-up to open
        :type title: str
        :param text: main text of the pop-up to open
        :type text: str
        :rtype: None
        """
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text=text))
        mybutton = Button(text='OK', size_hint=(1, 0.25))
        box.add_widget(mybutton)
        popup = Popup(title=title, content=box, size_hint=(None, None), size=(400, 300))
        mybutton.bind(on_release=self.stop)
        popup.open()

    def send_emails(self, name, email, message):
        print(name.text, email.text, message)

    def callback_for_menu_items(self, *args):
        toast(args[0])

    def show_example_grid_bottom_sheet(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Facebook": "facebook",
            "YouTube": "youtube",
            "Twitter": "twitter",
            "Da Cloud": "cloud-upload",
            "Camera": "camera",

        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()

    def Person(self):
        self.task_text = self.strng.get_screen('src 2').ids.task_text.text
        if self.task_text.split() != []:
            self.strng.get_screen('src 6').manager.current = 'src 6'
            self.strng.get_screen('src 6').ids.task_items.add_widget(
                OneLineListItem(text = self.task_text)
            )
        else:
            Snackbar(text = 'Task is Empty').show()

if __name__ == '__main__':
    PayNow().run()