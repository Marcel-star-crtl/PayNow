from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (500, 650)

LoginPage = """
MDFloatLayout:
    MDLabel:
        text: "Login"
        pos_hint: {"center_y": .85}
        font_style: "H4"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    MDLabel:
        text: "Welcome To The PayNow Mobile App"
        pos_hint: {"center_y": .75}
        font_style: "H5"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    MDTextField:
        id: email
        hint_text: "Enter Your Email"
        icon_right: "account"
        pos_hint: {"center_x": .5, "center_y": .6}
        current_hint_text_color: 0, 0, 0, 1
        color_mode: "custom"
        line_color_focus: 1, 0, 0, 1
        size_hint_x: .8
    MDTextField:
        id: password
        hint_text: "Password"
        icon_right: "eye-off"
        pos_hint: {"center_x": .5, "center_y": .45}
        current_hint_text_color: 0, 0, 0, 1
        size_hint_x: .8
        password: True
        color_mode: "custom"
        line_color_focus: 1, 0, 0, 1
        
    MDRaisedButton:
        text: "Log In"
        pos_hint: {"center_x": .5, "center_y": .3}
        size_hint_x: .5 
        on_release: app.verify(email.text, password.text)
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        
    MDIconButton:
        icon:'youtube'
        pos_hint:{'center_x':.5,'center_y':.1}
        on_release:
            OpenUrl('https://www.youtube.com/channel/UCXoNy5uQuZbwq248_ZKSfbw')
    MDIconButton:
        icon:'facebook'
        pos_hint:{'center_x':.3,'center_y':.1}
        on_release:
            OpenUrl('https://www.facebook.com/aboubakerZ')
    MDIconButton:
        icon:'telegram'
        pos_hint:{'center_x':.7,'center_y':.1}
        on_release:
            OpenUrl('https://t.me/dzTOdz')
        
    """


class Tutorial(MDApp):
    def build(self):
        login_page = Builder.load_string(LoginPage)
        return login_page

    def verify(self, email, password):
        if email == "123@paynow.com" and password == "1234":
            print("You Are Logged In To PayNow")

if __name__ == "__main__":
    Tutorial().run()