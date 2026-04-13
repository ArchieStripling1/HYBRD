from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen



class RunningScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=40)

        label = Label(text="Enter your longest run (km)", font_size=24)

        layout.add_widget(label)


        back_btn = Button(
            text="Previous",
            font_size=24,
            size_hint=(1, 0.2)
        )
        next_btn = Button(
            text="Next",
            font_size=24,
            size_hint=(1, 0.2)
        )

        next_btn.bind(on_press=self.go_next)
        back_btn.bind(on_press=self.go_back)

        layout.add_widget(back_btn)
        layout.add_widget(next_btn)

        self.add_widget(layout)


    def go_next(self, instance):
        if self.selected[1] is not None:
            self.manager.current = self.selected[1]

    def go_back(self, instance):
        self.manager.current = ("home")