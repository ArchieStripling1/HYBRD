from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen



class SportSelectionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        self.selected=[]

        layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=40
        )

        title = Label(
            text="What are you interested in?",
            font_size=32,
            size_hint=(1, 0.2)
        )

        run_btn = Button(
            text="Running",
            font_size=24,
            size_hint=(1, 0.2)
        )

        cycle_btn = Button(
            text="Cycling",
            font_size=24,
            size_hint=(1, 0.2)
        )

        swim_btn = Button(
            text="Swimming",
            font_size=24,
            size_hint=(1, 0.2)
        )

        next_btn = Button(
            text="Next",
            font_size=24,
            size_hint=(1, 0.2)
        )

        run_btn.bind(on_press=self.select_running)
        cycle_btn.bind(on_press=self.select_cycle)
        swim_btn.bind(on_press=self.select_swim)

        next_btn.bind(on_press=self.go_next)

        layout.add_widget(title)
        layout.add_widget(run_btn)
        layout.add_widget(cycle_btn)
        layout.add_widget(swim_btn)
        layout.add_widget(next_btn)

        self.add_widget(layout)

    def select_running(self, instance):
        if "running" not in self.selected:
            self.selected.append("running")
            print("Selected:", self.selected)
        else:
            self.selected.remove("running")
            print("Selected:", self.selected)

    def select_cycle(self, instance):
        if "cycle" not in self.selected:
            self.selected.append("cycle")
            print("Selected:", self.selected)
        else:
            self.selected.remove("cycle")
            print("Selected:", self.selected)

    def select_swim(self, instance):
        if "swim" not in self.selected:
            self.selected.append("swim")
            print("Selected:", self.selected)
        else:
            self.selected.remove("swim")
            print("Selected:", self.selected)

    def go_next(self, instance):
        if self.selected is not None: #this does not work and even doing it by length doesnt work.
            self.manager.current = self.selected[0]

