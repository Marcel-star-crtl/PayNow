from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string("""
<ScreenEight>:
    name: "scr 2A"
    MDLabel:
        id: task_label
        halign: 'center'
        markup: True
        text: '[size=20][b]Click the button at the bottom of the screen to enter start a list[/b][/size]'
        pos_hint: {'y': .35}

    ScrollView:
        pos_hint:{'center_y':.5, 'center_x':.5}
        size_hint: .9, .8

        MDList:
            id: container

    MDFloatingActionButton:
        icon: 'plus-thick'
        on_release: app.show_task_dialog()
        elevation_normal: 20
        pos_hint: {'x': .45, 'y':.05}


<DialogContent>:
    orientation: 'vertical'
    spacing: '10dp'
    size_hint: 1, None
    height: '150dp'

    GridLayout:
        rows: 1
        MDTextField:
            id: task_text
            hind_text: 'Add Task..'
            hint_text : 'Enter Name'
            pos_hint: {'center_y': .5}
            max_text_length: 50
            
        MDTextField:
            id: task_text
            hind_text: 'Add Task..'
            hint_text : 'Enter Number'
            pos_hint: {'center_y': .5}
            max_text_length: 50

        MDIconButton:
            icon: 'calendar'
            on_release: root.show_date_picker()
            padding: '10dp'

    MDLabel:
        spacing: '10dp'
        id: date_text

    BoxLayout:
        orientation: 'horizontal'

        MDRaisedButton:
            text: 'SAVE'
            on_release: (app.add_task(task_text, date_text.text), app.close_dialog())

        MDFlatButton:
            text: 'CANCEL'
            on_release: app.close_dialog()


<ListItemWithCheckbox>:
    id: the_list_item
    markup:True

    LeftCheckbox:
        id: check
        on_release: root.mark(check, the_list_item)

    IconRightWidget:
        icon: 'trash-can-outline'
        theme_text_color: 'Custom'
        text_color: 1, 0, 0, 1
        on_release: root.delete_item(the_list_item)
        
""")


class ScreenEight(Screen):
    pass