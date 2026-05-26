from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.togglebutton import ToggleButton

from SportSelection import selected
from kivy.app import App

class BuildPlan(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        self.daysSelected = []

        layout = BoxLayout(orientation='vertical', padding=25, spacing=25)

            # Header
        title = Label(
            text="Build Plan",
            font_size=36,
            size_hint=(1, 0.15),
            bold=True
        )

        layout.add_widget(title)

        scroll = ScrollView(size_hint=(1, 0.75))
        content = BoxLayout(
            orientation='vertical',
            spacing=20,
            size_hint_y=None
        )
        content.bind(minimum_height=content.setter('height'))

        #Race Type

        self.race_label = Label(font_size=22, size_hint_y=None, height=30)

        #Distance

        # Current Weekly Mileage
        self.weekly_label = Label(font_size=20, size_hint_y=None, height=30)

        # Current Longest Effort
        self.longest_label = Label(font_size=20, size_hint_y=None, height=30)

        # Current PB
        self.currentPB_label = Label(font_size=20, size_hint_y=None, height=30)

        # Level Section for basing workout off of how much experience you have running.
        expertise = Label(
            text="What level Runner are you: ",
            font_size=20
        )
        # Creates Dropdown
        dropdown = DropDown()

        level_list = ["Beginner", "Intermediate", "Advanced"]
        # For each day in days
        for level in level_list:
            btn = Button(
                text=level,
                size_hint_y=None,
                height=44
            )
            # On button click it selects the text from the day and creates a button using an anonymous function
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))

            dropdown.add_widget(btn)

        self.levelBtn = Button(
            text="Select Level",
            size_hint=(1, None),
            height=50
        )

        self.levelBtn.bind(on_release=dropdown.open)
        # Dropdown uses x as the day and sets the long run day variable.
        dropdown.bind(on_select=lambda instance, x: self.set_level(x))

        #Length of Plan
        length = Label(
            text="How many weeks do you want this plan to be: ",
            font_size=20,
            size_hint_y=None,
            height=30

        )
        self.planLength = TextInput(
            hint_text="No. Weeks",
            font_size=22,
            size_hint=(1, None),
            height=55,
            multiline=False,
            background_normal="",
            background_active="",
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
            padding=[10, 15]
        )

        self.planLength.bind(on_text_validate=self.update_length)


        # Days Available
        activityDays = Label(
            text="What days do you want to run: ",
            font_size=20
        )
        days = ["Monday", "Tuesday", "Wednesday","Thursday", "Friday","Saturday","Sunday"]
        grid = GridLayout(
            rows=1,
            cols=7,
            size_hint_y=None,
            height=60,
            spacing=5
        )


        for day in days:
            grid.add_widget(self.create_button(day))

        # Long Distance Effort Day
        longRunDay = Label(
            text="What day do you want to do your long run: ",
            font_size=20
        )
        #Creates Dropdown
        dropdown2 = DropDown()

        #For each day in days
        for day in days:
            btn = Button(
                text=day,
                size_hint_y=None,
                height=44
            )
            #On button click it selects the text from the day and creates a button using an anonymous function
            btn.bind(on_release=lambda btn: dropdown2.select(btn.text))

            dropdown2.add_widget(btn)

        self.longRunBtn = Button(
            text="Select Day",
            size_hint=(1, None),
            height=50
        )

        self.longRunBtn.bind(on_release=dropdown2.open)
        #Dropdown uses x as the day and sets the long run day variable.
        dropdown2.bind(on_select=lambda instance, x: self.set_long_run_day(x))

        # Build Plan Button
        buildPlanBtn = Button(
            text="Build Plan",
            size_hint=(1, None),
            height=50
        )
        buildPlanBtn.bind(on_press = self.build_plan)

        content.add_widget(self.race_label)
        content.add_widget(self.weekly_label)
        content.add_widget(self.longest_label)
        content.add_widget(self.currentPB_label)
        content.add_widget(expertise)
        content.add_widget(self.levelBtn)
        content.add_widget(length)
        content.add_widget(self.planLength)
        content.add_widget(activityDays)
        content.add_widget(grid)
        content.add_widget(longRunDay)
        content.add_widget(self.longRunBtn)
        content.add_widget((buildPlanBtn))
        scroll.add_widget(content)
        layout.add_widget(scroll)
        self.add_widget(layout)

    def on_enter(self):
        data = App.get_running_app().data
        race = data.get("race")

        # Race Types
        raceRun = ['5k', '10k', 'half', 'marathon']
        raceCycle = ['cycle_20', 'cycle_50', 'cycle_100']
        raceSwim = ['swim_1000', 'swim_2000', 'swim_4000']
        raceTriathlon = ['ironman_70.3', 'ironman_140.6']

        weeklyRunDistance = data.get("Weekly_Distance")
        weeklySwimDistance = data.get("Weekly_Swimming")
        weeklyCycleDistance = data.get("Weekly_Cycle")
        longestRun = data.get("Longest_Run")
        longestSwim = data.get("Longest_Swim")
        longestCycle = data.get("Longest_Cycle")
        #Find out what their race pb is.
        currentRunPB = data.get(f"{race}_pb")
        currentSwimPB = data.get("CurrentSwimPB")
        currentCyclePB = data.get("CurrentCyclePB")

        # if Race is a Running Race
        if race in raceRun:

            self.race_label.text = f"🏁 Race: {race.upper()}"
            self.longest_label.text = f"🏁 Longest Run: {longestRun} KM"
            self.weekly_label.text = f"🏁 Current Weekly Running Distance: {weeklyRunDistance} KM"
            self.currentPB_label.text = f"🏁 Your Current {race.upper()} PB is: {currentRunPB}"

        # if Race is a Swimming Race
        elif race in raceSwim:

            self.race_label.text = f"🏁 Race: {race.upper()}"
            self.longest_label.text = f"🏁 Longest Swim: {longestSwim} M"
            self.weekly_label.text = f"🏁 Current Weekly Swimming Distance: {weeklySwimDistance} M"
            self.currentPB_label.text = f"🏁 Your Current {race.upper()} PB is: {currentSwimPB}"

        # if Race is a Cycling Race
        elif race in raceCycle:

            self.race_label.text = f"🏁 Race: {race.upper()}"
            self.longest_label.text = f"🏁 Longest Cycle: {longestCycle} KM"
            self.weekly_label.text = f"🏁 Current Weekly Cycling Distance: {weeklyCycleDistance} KM"
            self.currentPB_label.text = f"🏁 Your Current {race.upper()} Average is: {currentCyclePB} KMH"

        # if Race is a Triathlon Race
        elif race in raceTriathlon:

            # Needs changing so it outputs all of this data
            self.race_label.text = f"🏁 Race: {race.upper()}"
            self.longest_label.text = f"🏁 Longest Run: {longestRun} KM"
            self.longest_label.text = f"🏁 Longest Run: {longestCycle} KM"
            self.longest_label.text = f"🏁 Longest Run: {longestSwim} M"

            self.weekly_label.text = f"🏁 Current Weekly Running Distance: {weeklyRunDistance} KM"
            self.weekly_label.text = f"🏁 Current Weekly Cycling Distance: {weeklyCycleDistance} KM"
            self.weekly_label.text = f"🏁 Current Weekly Swimming Distance: {weeklySwimDistance} M"

    def update_length(self, instance):
        App.get_running_app().data["CurrentPlanLength"] = self.planLength.text

    def update_sessions(self, instance):
        App.get_running_app().data["CurrentAmountSessions"] = self.noSessions.text

    def create_button(self, day):
        btn = ToggleButton(
            text=day,
            size_hint=(1, None),
            height=60,
            font_size=20,
            background_color=(0.9, 0.9, 0.9, 1)
        )
        btn.bind(on_press=lambda instance: self.toggle_day(instance, day))
        return btn

    def toggle_day(self, instance, day):
        if instance.state == "down":
            instance.background_color = (0.2, 0.6, 1, 1)
            if day not in self.daysSelected:
                self.daysSelected.append(day)
        else:
            instance.background_color = (0.9, 0.9, 0.9, 1)
            if day in self.daysSelected:
                self.daysSelected.remove(day)

        print("Selected days:", self.daysSelected)

        # Save globally
        App.get_running_app().data["ActivityDays"] = self.daysSelected

    def set_long_run_day(self, day):
        self.longRunBtn.text = day
        App.get_running_app().data["LongRunDay"] = day
        print("Long run day:", day)

    def set_level(self, level):
        self.levelBtn.text = level
        App.get_running_app().data["Level"] = level
        print("Level:", level)


    def build_plan(self, instance):
        self.manager.current = "plan"
