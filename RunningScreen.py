
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
        self.input = TextInput(font_size=24, size_hint=(1, 0.2), multiline=False)
        label = Label(text="Enter your longest run (km)", font_size=24)



        layout.add_widget(label)
        layout.add_widget(self.input)


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
        longestDistance = float(self.input.text)
        if longestDistance >= 5 and longestDistance < 10:
            self.manager.current = "RunningTime5k"
        elif longestDistance >= 10 and longestDistance < 21:
            self.manager.current = "RunningTime10k"
        elif (longestDistance >= 21and longestDistance < 42):
            self.manager.current = "RunningTimeHalf"
        elif longestDistance >= 42:
            self.manager.current = "RunningTimeMarathon"

    def go_back(self, instance):
        self.manager.current = "sport"


class RunningTimeMarathon(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=40)
        label = Label(text="What is your fastest Marathon time (HH:MM:SS)", font_size=24)
        MarathonTime = TextInput(font_size=24, size_hint=(1, 0.2), multiline=False)
        layout.add_widget(label)
        layout.add_widget(MarathonTime)


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
        self.manager.current = "RunningTimeHalf"

    def go_back(self, instance):
        self.manager.current = "running"

class RunningTimeHalf(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=40)
        label = Label(text="What is your fastest Half Marathon time (HH:MM:SS)", font_size=24)
        HalfMarathonTime = TextInput(font_size=24, size_hint=(1, 0.2), multiline=False)
        layout.add_widget(label)
        layout.add_widget(HalfMarathonTime)


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
        self.manager.current = "RunningTime10k"

    def go_back(self, instance):
        self.manager.current = "running"

class RunningTime10k(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=40)
        label = Label(text="What is your fastest 10KM time (HH:MM:SS)", font_size=24)
        KM10Time = TextInput(font_size=24, size_hint=(1, 0.2), multiline=False)
        layout.add_widget(label)
        layout.add_widget(KM10Time)


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
        self.manager.current = "RunningTime5k"

    def go_back(self, instance):
        self.manager.current = "running"

class RunningTime5k(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=40)
        label = Label(text="What is your fastest 5KM time (HH:MM:SS)", font_size=24)
        KM5Time = TextInput(font_size=24, size_hint=(1, 0.2), multiline=False)
        layout.add_widget(label)
        layout.add_widget(KM5Time)

        print(self.input)


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
        self.manager.current = "RunningScreen"

    def go_back(self, instance):
        self.manager.current = "running"