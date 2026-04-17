from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

class IntroScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=40
        )

        title = Label(
            text="HYBRD",
            font_size=32,
            size_hint=(1, 0.2)
        )

        next_btn = Button(
            text="Next",
            font_size=24,
            size_hint=(1, 0.2)
        )

        next_btn.bind(on_press=self.go_next)

        layout.add_widget(title)
        layout.add_widget(next_btn)

        self.add_widget(layout)

    def go_next(self):
        self.manager.current = "sport"