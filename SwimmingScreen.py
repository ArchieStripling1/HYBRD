from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from SportSelection import selected


class SwimmingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=30, spacing=30)

        # Header

        title = Label(
            text="Swimming Profile",
            font_size=24,
            size_hint=(1, 0.15),
            bold=True
        )
        layout.add_widget(title)

        # Longest Swim
        longest_box = BoxLayout(orientation='vertical', spacing=10)
        longest_label = Label(text="Longest Swim (Meters)", font_size=24)

        self.longest_value = Label(text="0 m", font_size=26)

        # Slider
        self.longest_slider = Slider(min=1, max=6000, value=0)
        self.longest_slider.bind(value=self.update_longest)

        longest_box.add_widget(longest_label)
        longest_box.add_widget(self.longest_value)
        longest_box.add_widget(self.longest_slider)

        layout.add_widget(longest_box)

        # Weekly Distance
        weekly_box = BoxLayout(orientation='vertical', spacing=10)

        weekly_label = Label(text="Weekly Distance (Meters)", font_size=20)

        self.weekly_value = Label(text="0 m", font_size=26)

        # Slider
        self.weekly_slider = Slider(min=0, max=12000, value=0)
        self.weekly_slider.bind(value=self.update_weekly)

        weekly_box.add_widget(weekly_label)
        weekly_box.add_widget(self.weekly_value)
        weekly_box.add_widget(self.weekly_slider)

        layout.add_widget(weekly_box)

        # Buttons
        btn_box = BoxLayout(size_hint=(1, 0.2), spacing=20)

        back_btn = Button(text="Previous", font_size=20)
        next_btn = Button(text="Next", font_size=20)

        # Bind Buttons
        back_btn.bind(on_press=self.go_back)
        next_btn.bind(on_press=self.go_next)

        btn_box.add_widget(back_btn)
        btn_box.add_widget(next_btn)

        layout.add_widget(btn_box)

        self.add_widget(layout)

    # Update Slider Value
    def update_longest(self, instance, value):
        self.longest_value.text = f"{int(value)} meters"

    # Update Slider Value

    def update_weekly(self, instance, value):
        self.weekly_value.text = f"{int(value)} meters"

    def go_next(self, instance):
        SwimmingDistance = int(self.longest_slider.value)

        if 100 <= SwimmingDistance <= 500:
            self.manager.current = "Pace100M"
        elif 500 <= SwimmingDistance <= 1000:
            self.manager.current = "Pace400M"
        elif 1000 <= SwimmingDistance:
            self.manager.current = "Pace1000M"


    def go_back(self, instance):
        self.manager.current = "sport"

class SwimmingPace(Screen):
    def __init__(self, distance, **kwargs):
        super().__init__(**kwargs)  # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=30, spacing=30)

        #Enter Longest Distance Time
        title = Label(
            text=f"Enter your {distance} time",
            font_size=30
        )

        self.input = TextInput(
            hint_text="HH:MM:SS",
            font_size=24,
            size_hint=(1, 0.2)
        )

        #Buttons
        btn_box = BoxLayout(size_hint=(1, 0.2), spacing=20)

        back_btn = Button(text="Previous")
        next_btn = Button(text="Next")

        # Bind Buttons
        back_btn.bind(on_press=self.go_back)
        next_btn.bind(on_press=self.go_next)

        btn_box.add_widget(back_btn)
        btn_box.add_widget(next_btn)

        layout.add_widget(title)
        layout.add_widget(self.input)
        layout.add_widget(btn_box)

        self.add_widget(layout)

    def go_next(self, instance):
        selected.remove('swim')
        print(selected)

        # For Each Sport go through process
        length = len(selected)
        for i in range(length):
            self.manager.current = selected[i]

        if not selected:
            self.manager.current = "intro"

    def go_back(self, instance):
        self.manager.current = "race"
