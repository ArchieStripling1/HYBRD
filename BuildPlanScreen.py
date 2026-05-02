from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from SportSelection import selected
from kivy.app import App

class BuildPlan(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=25, spacing=25)

        # Header
        title = Label(
            text="Build Plan",
            font_size=36,
            size_hint=(1, 0.15),
            bold=True
        )

        layout.add_widget(title)

        #Race Type

        self.race_label = Label(font_size=22)

        #Distance

        # Current Weekly Mileage
        self.weekly_label = Label(font_size=20)

        # Current Longest Effort
        self.longest_label = Label(font_size=20)

        # Current PB
        self.currentPB_label = Label(font_size=20)

        #Length of Plan
        length = Label(
            text="How many weeks do you want this plan to be: ",
            font_size=20
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

        # Sessions per activity per week
        sessions = Label(
            text="How many sessions do you want to do a week: ",
            font_size=20
        )
        self.noSessions = TextInput(
            hint_text="No. Sessions",
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

        self.noSessions.bind(on_text_validate=self.update_sessions)

        # Days Available
        daysAvailable = Label(
            text="What days are you available for Running: ",
            font_size=20
        )

        # Long Distance Effort Day
        longRunDay = Label(
            text="What day do you want to do your long run: ",
            font_size=20
        )

        # Build Plan Button


        layout.add_widget(self.race_label)
        layout.add_widget(self.weekly_label)
        layout.add_widget(self.longest_label)
        layout.add_widget(self.currentPB_label)
        layout.add_widget(length)
        layout.add_widget(self.planLength)
        layout.add_widget(sessions)
        layout.add_widget(self.noSessions)
        layout.add_widget(daysAvailable)
        layout.add_widget(longRunDay)
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
        currentRunPB = data.get("CurrentRunPB")
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
