from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.togglebutton import ToggleButton

selected = []

class SportSelectionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=40
        )

        # Header
        title = Label(
            text="What are you interested in?",
            font_size=32,
            size_hint=(1, 0.2)
        )

        # Buttons
        run_btn = ToggleButton(
            text="Running",
            font_size=24,
            size_hint=(1, 0.2)
        )

        cycle_btn = ToggleButton(
            text="Cycling",
            font_size=24,
            size_hint=(1, 0.2)
        )

        swim_btn = ToggleButton(
            text="Swimming",
            font_size=24,
            size_hint=(1, 0.2)
        )

        next_btn = ToggleButton(
            text="Next",
            font_size=24,
            size_hint=(1, 0.2)
        )

        # Bind Buttons
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

    # If running is not in selected add it to selected, if it is in selected remove it.
    @staticmethod
    def select_running(instance):
        if "running" not in selected:
            selected.append("running")
            print("Selected:", selected)
        else:
            selected.remove("running")
            print("Selected:", selected)

    # If cycle is not in selected add it to selected, if it is in selected remove it.
    @staticmethod
    def select_cycle(instance):
        if "cycle" not in selected:
            selected.append("cycle")
            print("Selected:", selected)
        else:
            selected.remove("cycle")
            print("Selected:", selected)

    # If swim is not in selected add it to selected, if it is in selected remove it.
    @staticmethod
    def select_swim(instance):
        if "swim" not in selected:
            selected.append("swim")
            print("Selected:", selected)
        else:
            selected.remove("swim")
            print("Selected:", selected)

    def go_next(self, instance):
        self.manager.current = "race"

