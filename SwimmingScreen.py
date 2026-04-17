from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from SportSelection import selected


class SwimmingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=40)
        self.input = TextInput(font_size=24, size_hint=(1, 0.2),multiline=False)
        label = Label(text="Enter your longest Swim (Meters)", font_size=24)
        label1 = Label(text="Enter your weekly Average (KM)", font_size=24)
        self.input2 = TextInput(font_size=24, size_hint=(1, 0.2), multiline=False)


        layout.add_widget(label)
        layout.add_widget(self.input)
        layout.add_widget(label1)
        layout.add_widget(self.input2)

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

    def go_next(self):
        SwimmingDistance = float(self.input.text)
        weeklyDistance = float(self.input2.text)
        if 100 <= SwimmingDistance <= 500:
            self.manager.current = "Pace100M"
        elif 500 <= SwimmingDistance <= 1000:
            self.manager.current = "Pace400M"
        elif 1000 <= SwimmingDistance <= 2000:
            self.manager.current = "Pace1000M"


    def go_back(self):
        self.manager.current = "sport"

class Pace1000M(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=40)
        label = Label(text="What is your average pace per 1000 Meters (MM:SS)", font_size=24)
        pace1000M = TextInput(font_size=24, size_hint=(1, 0.2), multiline=False)
        layout.add_widget(label)
        layout.add_widget(pace1000M)

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

    def go_next(self):
        self.manager.current = "Pace400M"

    def go_back(self):
        self.manager.current = "swim"

class Pace400M(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=40)
        label = Label(text="What is your average pace per 400 Meters (MM:SS)", font_size=24)
        pace400M = TextInput(font_size=24, size_hint=(1, 0.2), multiline=False)
        layout.add_widget(label)
        layout.add_widget(pace400M)

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

    def go_next(self):
        self.manager.current = "Pace100M"

    def go_back(self):
        self.manager.current = "swim"

class Pace100M(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=40)
        label = Label(text="What is your average pace per 100 Meters (MM:SS)", font_size=24)
        pace100M = TextInput(font_size=24, size_hint=(1, 0.2), multiline=False)
        layout.add_widget(label)
        layout.add_widget(pace100M)

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

    def go_next(self):
        selected.remove('swim')
        print(selected)
        length = len(selected)
        for i in range(length):
            self.manager.current = selected[i]

        if not selected:
            self.manager.current = "intro"

    def go_back(self):
        self.manager.current = "swim"