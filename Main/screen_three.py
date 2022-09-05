from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string("""
<ScreenThree>:
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


""")


class ScreenThree(Screen):
    pass