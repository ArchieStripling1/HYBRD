from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen

from SportSelection import selected


class CyclingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=40)
        self.input = TextInput(font_size=24, size_hint=(1, 0.2), multiline=False)
        label = Label(text="Enter your longest Cycle (km)", font_size=24)
        label2 = Label(text="Enter your weekly distance (km)", font_size=24)
        self.input2 = TextInput(font_size=24, size_hint=(1, 0.2), multiline=False)

        layout.add_widget(label)
        layout.add_widget(self.input)
        layout.add_widget(label2)
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
        CyclingDistance = float(self.input.text)
        WeeklyDistance = float(self.input2.text)
        if 0 <= CyclingDistance < 50:
            self.manager.current = "Cycling10K"
        elif 50 <= CyclingDistance < 100:
            self.manager.current = "Cycling50K"
        elif CyclingDistance >= 100:
            self.manager.current = "Cycling100K"


    def go_back(self):
        self.manager.current = "sport"

class Cycling100K(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=40)
        label = Label(text="What is your average pace per 100KM (KMPH)", font_size=24)
        cycling100k = TextInput(font_size=24, size_hint=(1, 0.2), multiline=False)
        layout.add_widget(label)
        layout.add_widget(cycling100k)

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
        self.manager.current = "Cycling50K"

    def go_back(self):
        self.manager.current = "swim"

class Cycling50K(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=40)
        label = Label(text="What is your average pace per 50KM (KMPH)", font_size=24)
        cycling50k = TextInput(font_size=24, size_hint=(1, 0.2), multiline=False)
        layout.add_widget(label)
        layout.add_widget(cycling50k)

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
        self.manager.current = "Cycling10K"

    def go_back(self):
        self.manager.current = "swim"

class Cycling10K(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=40)
        label = Label(text="What is your average pace per 10KM (KMPH)", font_size=24)
        cycling10k = TextInput(font_size=24, size_hint=(1, 0.2), multiline=False)
        layout.add_widget(label)
        layout.add_widget(cycling10k)

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
        selected.remove('cycle')
        print(selected)
        length = len(selected)
        for i in range(length):
            self.manager.current = selected[i]

        if not selected:
            self.manager.current = "intro"


    def go_back(self):
        self.manager.current = "swim"