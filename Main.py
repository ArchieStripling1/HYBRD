from asyncio.windows_events import NULL

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

from IntroScreen import IntroScreen
from SportSelection import SportSelectionScreen
from RunningScreen import RunningScreen, RunningTimeMarathon, RunningTimeHalf, RunningTime10k, RunningTime5k
from CyclingScreen import CyclingScreen
from SwimmingScreen import SwimmingScreen


class MainApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(IntroScreen(name="intro"))
        sm.add_widget(SportSelectionScreen(name="sport"))
        sm.add_widget(RunningScreen(name="running"))
        sm.add_widget(CyclingScreen(name="cycle"))
        sm.add_widget(SwimmingScreen(name="swim"))
        sm.add_widget(RunningTimeMarathon(name="RunningTimeMarathon"))
        sm.add_widget(RunningTimeHalf(name="RunningTimeHalf"))
        sm.add_widget(RunningTime10k(name="RunningTime10k"))
        sm.add_widget(RunningTime5k(name="RunningTime5k"))


        return sm


if __name__ == "__main__":
    MainApp().run()