from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from SportSelection import selected


class RunningScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=30, spacing=30)

        title = Label(
            text="Running Profile",
            font_size=34,
            size_hint=(1, 0.15),
            bold=True
        )
        layout.add_widget(title)

        # Longest Run
        longest_box = BoxLayout(orientation='vertical', spacing=10)
        longest_label = Label(text="Longest Run (km)", font_size=20)

        self.longest_value = Label(text="0 km", font_size=26)

        self.longest_slider = Slider(min=1, max=60, value=0)
        self.longest_slider.bind(value=self.update_longest)

        longest_box.add_widget(longest_label)
        longest_box.add_widget(self.longest_value)
        longest_box.add_widget(self.longest_slider)

        layout.add_widget(longest_box)

        # Weekly Distance
        weekly_box = BoxLayout(orientation='vertical', spacing=10)

        weekly_label = Label(text="Weekly Distance (km)", font_size=20)

        self.weekly_value = Label(text="0 km", font_size=26)

        self.weekly_slider = Slider(min=0, max=150, value=0)
        self.weekly_slider.bind(value=self.update_weekly)

        weekly_box.add_widget(weekly_label)
        weekly_box.add_widget(self.weekly_value)
        weekly_box.add_widget(self.weekly_slider)

        layout.add_widget(weekly_box)

        # Buttons
        btn_box = BoxLayout(size_hint=(1, 0.2), spacing=20)

        back_btn = Button(text="Previous", font_size=20)
        next_btn = Button(text="Next", font_size=20)

        back_btn.bind(on_press=self.go_back)
        next_btn.bind(on_press=self.go_next)

        btn_box.add_widget(back_btn)
        btn_box.add_widget(next_btn)

        layout.add_widget(btn_box)

        self.add_widget(layout)

    def update_longest(self, instance, value):
        self.longest_value.text = f"{int(value)} km"

    def update_weekly(self, instance, value):
        self.weekly_value.text = f"{int(value)} km"

    def go_next(self, instance):
        longestDistance = int(self.longest_slider.value)

        if 5 <= longestDistance < 10:
            self.manager.current = "RunningTime5k"
        elif 10 <= longestDistance < 21:
            self.manager.current = "RunningTime10k"
        elif 21 <= longestDistance < 42:
            self.manager.current = "RunningTimeHalf"
        elif longestDistance >= 42:
            self.manager.current = "RunningTimeMarathon"

    def go_back(self, instance):
        self.manager.current = "sport"


class RunningTimeScreen(Screen):
    def __init__(self, distance, **kwargs):
        super().__init__(**kwargs)


        layout = BoxLayout(orientation='vertical', padding=30, spacing=30)

        title = Label(
            text=f"Enter your {distance} time",
            font_size=30
        )

        self.input = TextInput(
            hint_text="HH:MM:SS",
            font_size=24,
            size_hint=(1, 0.2)
        )

        btn_box = BoxLayout(size_hint=(1, 0.2), spacing=20)

        back_btn = Button(text="Previous")
        next_btn = Button(text="Next")

        back_btn.bind(on_press=self.go_back)
        next_btn.bind(on_press=self.go_next)

        btn_box.add_widget(back_btn)
        btn_box.add_widget(next_btn)

        layout.add_widget(title)
        layout.add_widget(self.input)
        layout.add_widget(btn_box)

        self.add_widget(layout)

    def go_next(self, instance):
        selected.remove('running')
        print(selected)
        length = len(selected)
        for i in range(length):
            self.manager.current = selected[i]

        if not selected:
            self.manager.current = "intro"

    def go_back(self, instance):
        self.manager.current = "race"
