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

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Header
        title = Label(
            text="Build Plan",
            font_size=36,
            size_hint=(1, 0.15),
            bold=True
        )

        layout.add_widget(title)

        #Race Type

        self.race_label = Label(
            text="Your Race is: ",
            font_size=20
        )

        layout.add_widget(self.race_label)
        #Distance


        # Current Weekly Mileage
        self.weekly_label = Label(
            text="Your Current Weekly Mileage is: ",
            font_size=20
        )
        layout.add_widget(self.weekly_label)

        # Current Longest Effort
        self.longest_label = Label(
            text="Your Longest Run is: ",
            font_size=20
        )
        layout.add_widget(self.longest_label)

        # Current PB
        self.currentPB_label = Label(
            text="Your Current PB is: ",
            font_size=20
        )
        layout.add_widget(self.currentPB_label)


        #Length of Plan

        #Sessions per activity per week

        #Days Available

        #Long Distance Effort Day

        #Build Plan Button

        self.add_widget(layout)

    def on_enter(self):
        data = App.get_running_app().data
        race = data.get("race")

        # Race Types
        raceRun = ['5k', '10k', 'half', 'marathon']
        raceCycle = ['cycle_20', 'cycle_50', 'cycle_100']
        raceSwim = ['swim_1000' 'swim_2000', 'swim_4000']
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

