from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
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

        #Current Weekly Mileage

        #Current Longest Effort

        #Current PB

        #Length of Plan

        #Sessions per activity per week

        #Days Available

        #Long Distance Effort Day

        #Build Plan Button
        self.add_widget(layout)

    def on_pre_enter(self):
        data = App.get_running_app().data
        race = data.get("race")

        self.race_label.text = f"🏁 Race: {race.upper()}"

