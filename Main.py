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

    def select_cycle(self, instance):
        if "cycle" not in self.selected:
            self.selected.append("cycle")
            print("Selected:", self.selected)
    def select_swim(self, instance):
        if "swim" not in self.selected:
            self.selected.append("swim")
            print("Selected:", self.selected)

    def go_next(self, instance):
        if self.selected is not None:
            self.manager.current = self.selected[0]


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





class CyclingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=40)

        label = Label(text="Enter your longest Cycle (km)", font_size=24)

        layout.add_widget(label)

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
        if "swim" in self.selected:
            self.manager.current = self.selected["swim"]
    def go_back(self, instance):
        self.manager.current = "home"



class SwimmingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=40)

        label = Label(text="Enter your longest Swim (km)", font_size=24)

        layout.add_widget(label)

        self.add_widget(layout)

class MainApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(SportSelectionScreen(name="home"))
        sm.add_widget(RunningScreen(name="running"))
        sm.add_widget(CyclingScreen(name="cycle"))
        sm.add_widget(SwimmingScreen(name="swim"))

        return sm


if __name__ == "__main__":
    MainApp().run()