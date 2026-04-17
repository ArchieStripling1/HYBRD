from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

selected = []

class SportSelectionScreen(Screen):
    def __init__(self, **kwargs):



        super().__init__(**kwargs) # setup Kivy screen



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

    @staticmethod
    def select_running():
        if "running" not in selected:
            selected.append("running")
            print("Selected:", selected)
        else:
            selected.remove("running")
            print("Selected:", selected)

    @staticmethod
    def select_cycle():
        if "cycle" not in selected:
            selected.append("cycle")
            print("Selected:", selected)
        else:
            selected.remove("cycle")
            print("Selected:", selected)

    @staticmethod
    def select_swim():
        if "swim" not in selected:
            selected.append("swim")
            print("Selected:", selected)
        else:
            selected.remove("swim")
            print("Selected:", selected)

    def go_next(self):
        if selected is not None: #this does not work and even doing it by length doesn't work.
            self.manager.current = selected[0]

