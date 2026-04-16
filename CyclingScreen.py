from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


class CyclingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=40)
        self.input = TextInput(font_size=24, size_hint=(1, 0.2), multiline=False)
        label = Label(text="Enter your longest Cycle (km)", font_size=24)

        layout.add_widget(label)
        layout.add_widget(self.input)


        next_btn = Button(
            text="Next",
            font_size=24,
            size_hint=(1, 0.2)
        )
        back_btn = Button(
            text="Previous",
            font_size=24,
            size_hint=(1, 0.2)
        )


        layout.add_widget(back_btn)
        layout.add_widget(next_btn)

        back_btn.bind(on_press=self.go_back)
        next_btn.bind(on_press=self.go_next)

        self.add_widget(layout)

    def go_next(self, instance):
        CyclingDistance = float(self.input.text)


    def go_back(self, instance):
        self.manager.current = "sport"