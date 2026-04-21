
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

# Import all classes for each Screen.
from IntroScreen import IntroScreen
from SportSelection import SportSelectionScreen
from RunningScreen import RunningScreen, RunningTimeScreen
from CyclingScreen import CyclingScreen, CyclingTimeScreen
from SwimmingScreen import SwimmingScreen, SwimmingPace
from RaceScreen import RaceScreen
from BuildPlanScreen import BuildPlan


class MainApp(App):
    def build(self):

        self.data = {}  #  store everything here

        sm = ScreenManager()

        sm.add_widget(IntroScreen(name="intro"))
        sm.add_widget(SportSelectionScreen(name="sport"))
        sm.add_widget(RaceScreen(name="race"))
        sm.add_widget(RunningScreen(name="running"))
        sm.add_widget(CyclingScreen(name="cycle"))
        sm.add_widget(SwimmingScreen(name="swim"))

        # Running Screens2
        sm.add_widget(RunningTimeScreen(
            name="RunningTimeMarathon",
            distance="Marathon"))
        sm.add_widget(RunningTimeScreen(
            name="RunningTimeHalf",
            distance="Half-Marathon"))
        sm.add_widget(RunningTimeScreen(
            name="RunningTime10k",
            distance="10K"))
        sm.add_widget(RunningTimeScreen(
            name="RunningTime5k",
            distance="5K"))

        # Swimming Screens
        sm.add_widget(SwimmingPace(
            name="Pace100M",
            distance="100M"))
        sm.add_widget(SwimmingPace(
            name="Pace400M",
            distance="400M"
        ))
        sm.add_widget(SwimmingPace(
            name="Pace1000M",
            distance="1000M"
        ))

        # Cycling Screens
        sm.add_widget(CyclingTimeScreen(
            name="Cycling10K",
            distance="10K"
        ))
        sm.add_widget(CyclingTimeScreen(
            name="Cycling50K",
            distance="50K"
        ))
        sm.add_widget(CyclingTimeScreen(
            name="Cycling100K",
            distance="100K"
        ))

        sm.add_widget(BuildPlan(name="BuildPlan"))


        return sm


if __name__ == "__main__":
    # Run App
    MainApp().run()