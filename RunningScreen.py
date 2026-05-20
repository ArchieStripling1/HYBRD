from kivy.app import App
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

        # Header
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

        # Slider
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

        # Slider
        self.weekly_slider = Slider(min=1, max=150, value=0)
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
        self.longest_value.text = f"{int(value)} km"

    # Update Slider Value

    def update_weekly(self, instance, value):
        self.weekly_value.text = f"{int(value)} km"

    def go_next(self, instance):
        longestDistance = int(self.longest_slider.value)
        weeklyDistance = int(self.weekly_slider.value)
        App.get_running_app().data["Longest_Run"] = longestDistance
        App.get_running_app().data["Weekly_Distance"] = weeklyDistance

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

        #reachable dictionary of PBs for distances
        self.inputs = {}
        layout = BoxLayout(orientation='vertical', padding=30, spacing=30)

        # Create list of all the PBs they will have depending on their furthest run.
        lst = []
        if distance == "Marathon":
            lst = ["marathon", "half", "10k", "5k"]
        elif distance == "Half-Marathon":
            lst = ["half", "10k", "5k"]
        elif distance == "10K":
            lst = ["10k", "5k"]
        elif distance == "5K":
            lst = ["5k"]

        for dist in lst:
            # Enter Longest Distance Time
            title = Label(
                text=f"Enter your {dist} time",
                font_size=30
            )

            pb_input = TextInput(
                hint_text="HH:MM:SS",
                font_size=24,
                height=30,
                size_hint=(1, 0.2),
                multiline=False
            )

            self.inputs[dist] = pb_input

            pb_input.bind(on_text_validate=self.update_input)

            layout.add_widget(title)
            layout.add_widget(pb_input)


        # Buttons

        btn_box = BoxLayout(
            size_hint=(1, 0.2),
            spacing=20
        )

        back_btn = Button(text="Previous")
        next_btn = Button(text="Next")

        back_btn.bind(on_press=self.go_back)
        next_btn.bind(on_press=self.go_next)

        btn_box.add_widget(back_btn)
        btn_box.add_widget(next_btn)

        layout.add_widget(btn_box)

        self.add_widget(layout)


    def update_input(self, instance):
        #For each distance they do create a data slot with the PB
        for dist, pb_input in self.inputs.items():
            PB = pb_input.text
            print(PB)

            App.get_running_app().data[f"{dist}_pb"] = PB

    def go_next(self, instance):
        selected.remove('running')
        print(selected)

        # For each sport go through process

        length = len(selected)
        for i in range(length):
            self.manager.current = selected[i]

        if not selected:
            self.manager.current = "BuildPlan"

    def go_back(self, instance):
        self.manager.current = "race"
