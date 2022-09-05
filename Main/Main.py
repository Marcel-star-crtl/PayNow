from kivy.config import Config

Config.set('kivy', 'exit_on_escape', '0')

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.toast.kivytoast import toast
from database import person, Database
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd import images_path
from database import person, Database
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime
from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
import pkgutil
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
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

Window.size = (500, 650)

from kivymd.app import MDApp

import screen_one
import screen_two
import screen_three
import screen_four
import screen_five
import screen_six
import screen_seven
import screen_eight

Buil_strng = '''
#: import t kivymd.toast.kivytoast
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


MDScreen:
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
                name : 'login'
                FloatLayout:
                    canvas:
                        Color:
                            rgba: rgba('#0e1574ff')
                        Triangle:
                            points: (0, self.size[1] - (0.4*self.size[1]), 0, self.size[1], self.size[0], self.size[1])
                        Color:
                            rgba: rgba('#0e1574c8')
                        Triangle:
                            points: (self.size[0], self.size[1] - (0.4*self.size[1]), self.size[0]//2, self.size[1] - (0.2*self.size[1]), self.size[0], self.size[1])
                    MDIcon:
                        pos_hint: {'center_x': 0.5, 'center_y' : 0.6}
                        size_hint: (None, None)
                        icon : 'AVATAR/icons8-user-100.png'
                    MDLabel:
                        text : 'LOGIN'
                        pos_hint : {'x' : 0.415, 'center_y' : 0.85}
                        theme_text_color : 'Custom'
                        text_color : (1, 1, 1, 1)
                        text_size: (0.3, 0.2)
                    MDTextField:
                        id : email
                        hint_text : 'Email'
                        icon_right: "email"
                        size_hint: (0.8, None)
                        pos_hint : {'center_x' : 0.5, 'center_y' : 0.45}
                    MDTextField:
                        id : password
                        hint_text : 'Password'
                        icon_right: "eye-off"
                        password : True
                        size_hint: (0.8, None)
                        pos_hint : {'center_x' : 0.5, 'center_y' : 0.34}
                    MDTextButton:
                        text : f"[u]Sign up![/u]"
                        markup: True
                        pos_hint: {'x': 0.1, 'y' : 0.26}
                        font_size: '13sp'
                        on_press:
                            app.change_screen()
                    MDTextButton:
                        text : f'[u]forgot password?[/u]'
                        markup: True
                        pos_hint : {'x' : 0.6, 'y' : 0.26}
                        font_size: '13sp'
                        on_press:
                            t.toast('Sorry we can"t do anything, you are solely responsible for that !!')
                    MDFillRoundFlatButton:
                        text : 'Login'
                        md_bg_color : rgba('#0e1574ff')
                        text_color : 1, 1, 1, 1
                        size_hint: (0.4, None)
                        pos_hint : {'center_x' : 0.5, 'center_y' : 0.17}
                        on_press:
                            app.validate()
            
                    MDIconButton:
                        icon:'youtube'
                        pos_hint:{'center_x':.5,'center_y':.04}
                        on_release:
                            OpenUrl('https://www.youtube.com/channel/UCXoNy5uQuZbwq248_ZKSfbw')
                    MDIconButton:
                        icon:'facebook'
                        pos_hint:{'center_x':.3,'center_y':.04}
                        on_release:
                            OpenUrl('https://www.facebook.com/aboubakerZ')
                    MDIconButton:
                        icon:'google'
                        pos_hint:{'center_x':.7,'center_y':.04}
                        on_release:
                            OpenUrl('https://t.me/dzTOdz')
            
            Screen:
                name : 'signup'
                FloatLayout:
                    canvas:
                        Color:
                            rgba: rgba('#0e1574ff')
                        Triangle:
                            points: (0, self.size[1] - (0.4*self.size[1]), 0, self.size[1], self.size[0], self.size[1])
                        Color:
                            rgba: rgba('#0e1574c8')
                        Triangle:
                            points: (self.size[0], self.size[1] - (0.4*self.size[1]), self.size[0]//2, self.size[1] - (0.2*self.size[1]), self.size[0], self.size[1])
                    MDIconButton:
                        icon : 'keyboard-backspace'
                        pos_hint: {'center_x': 0.1, 'center_y' : 0.94}
                        theme_text_color : 'Custom'
                        text_color : (1, 1, 1, 1)
                        on_press:
                            app.change_screen('back')
                    MDLabel:
                        text : 'SIGNUP'
                        pos_hint : {'x' : 0.415, 'center_y' : 0.85}
                        theme_text_color : 'Custom'
                        text_color : (1, 1, 1, 1)
                        text_size: (0.3, 0.2)
                    MDIcon:
                        pos_hint: {'center_x': 0.5, 'center_y' : 0.6}
                        size_hint: (None, None)
                        icon : 'AVATAR/icons8-user-100.png'
                    MDTextField:
                        id : email_signup
                        hint_text : 'Email'
                        icon_right: "email"
                        size_hint: (0.8, None)
                        pos_hint : {'center_x' : 0.5, 'center_y' : 0.45}
                    MDTextField:
                        id : password_signup
                        hint_text : 'Password'
                        icon_right: "eye-off"
                        password : True
                        size_hint: (0.8, None)
                        pos_hint : {'center_x' : 0.5, 'center_y' : 0.34}
                    MDFillRoundFlatButton:
                        text : 'signup'
                        md_bg_color : rgba('#0e1574ff')
                        text_color : 1, 1, 1, 1
                        size_hint: (0.4, None)
                        pos_hint : {'center_x' : 0.5, 'center_y' : 0.17}
                        on_press:
                            app.signup()
            
                    MDIconButton:
                        icon:'youtube'
                        pos_hint:{'center_x':.5,'center_y':.04}
                        on_release:
                            OpenUrl('https://www.youtube.com/channel/UCXoNy5uQuZbwq248_ZKSfbw')
                    MDIconButton:
                        icon:'facebook'
                        pos_hint:{'center_x':.3,'center_y':.04}
                        on_release:
                            OpenUrl('https://www.facebook.com/aboubakerZ')
                    MDIconButton:
                        icon:'google'
                        pos_hint:{'center_x':.7,'center_y':.04}
                        on_release:
                            OpenUrl('https://t.me/dzTOdz')

            ScreenOne:
            ScreenTwo:  
            ScreenThree:
            ScreenFour:
            ScreenFive:
            ScreenSix:
            ScreenSeven:
            ScreenEight:

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
'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Content(MDBoxLayout):
	'''Custom content.'''

class ListItemWithCheckbox(TwoLineAvatarIconListItem):

    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        self.pk = pkgutil

    def mark(self, check, the_list_item):
        if check.active == True:
            the_list_item.text = '[s]' + the_list_item.text + '[/s]'
        else:
            pass

    def delete_item(self, the_list_item):
        self.parent.remove_widget(the_list_item)


class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
	pass


class DialogContent(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text = str(datetime.now().strftime('%A %d %B %Y'))

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        date = value.strftime('%A %d %B %Y')
        self.ids.date_text.text = str(date)

class PayNow(MDApp):
    dialog = None
    task_list_dialog = None
    def build(self):
        Window.bind(on_request_close=self.on_request_close)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.strng = Builder.load_string(Buil_strng)
        return self.strng

    def on_start(self):
        Window.bind(on_request_close=self.on_request_close)
        self.p_obj = person()
        self.data = Database()

    def scr_1A(self, *args):
        self.root.ids.screen_manager.current = 'scr 1A'

    def scr_2(self, *args):
        self.root.ids.screen_manager.current = 'scr 2A'

    def scr_2A(self, *args):
        self.root.ids.screen_manager.current = 'scr 2'

    def signup(self):
        email = self.root.ids.email_signup.text
        password = self.root.ids.password_signup.text
        if not email and not password:
            return toast('email and password are not provided.')
        elif not email:
            return toast('email is not valid')
        elif not password:
            return toast('password is not valid')
        val = self.data.select_by_email(email=email)
        if val is None:
            self.p_obj.add_email(email)
            self.p_obj.add_password(password)
            self.data.add_entry(self.p_obj)
        else:
            return toast('already exists !!')
        return toast('registered successfully !!')

    def change_screen(self, direct=None):
        if direct is not None:
            self.root.ids.screen_manager.current = 'login'
            self.root.ids.screen_manager.transition.direction = 'right'
            self.root.ids.email.text = ''
            self.root.ids.password.text = ''
        else:
            self.root.ids.screen_manager.current = 'signup'
            self.root.ids.screen_manager.transition.direction = 'left'
            self.root.ids.email_signup.text = ''
            self.root.ids.password_signup.text = ''

    def validate(self):
        email = self.root.ids.email.text
        password = self.root.ids.password.text
        if not email and not password:
            return toast('email and password are not provided.')
        elif not email:
            return toast('email is not valid')
        elif not password:
            return toast('password is not valid')
        val = self.data.select_by_email(email=email)
        real_email, real_pass = [val, ('', '')][val is None]
        if real_email != email:
            toast('You are not registered !!')
        elif real_pass != password:
            toast('Incorrect Password !!')
        else:
            toast('login successfull !!')
            self.root.ids.screen_manager.current = 'scr 1'

    def show_task_dialog(self):
        if not self.task_list_dialog:
            self.task_list_dialog = MDDialog(
                title='Create Task',
                type='custom',
                content_cls=DialogContent(),
            )
        self.task_list_dialog.open()

    def close_dialog(self, *args):
        self.task_list_dialog.dismiss()

    def add_task(self, task, task_date):
        print(task.text, task_date)

        self.root.ids['container'].add_widget(
            ListItemWithCheckbox(text='[b]' + task.text + '[/b]', secondary_text=task_date))
        task.text = ''

    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Address:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color
                    ),
                ],
            )
        self.dialog.open()

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

    def person(self):
        self.task_text = self.strng.ids.screen_manager.get_screen('src 2').ids.task_text.text
        if self.task_text.split() != []:
            self.strng.get_screen('src 6').manager.current = 'src 6'
            self.strng.get_screen('src 6').ids.task_items.add_widget(
                OneLineListItem(text=self.task_text)
            )
        else:
            Snackbar(text='No person added yet').show()


if __name__ == '__main__':
    PayNow().run()