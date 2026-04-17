
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from IntroScreen import IntroScreen
from SportSelection import SportSelectionScreen
from RunningScreen import RunningScreen, RunningTimeMarathon, RunningTimeHalf, RunningTime10k, RunningTime5k
from CyclingScreen import CyclingScreen, Cycling100K, Cycling50K, Cycling10K
from SwimmingScreen import SwimmingScreen, Pace1000M, Pace400M, Pace100M


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
        sm.add_widget(Pace1000M(name="Pace1000M"))
        sm.add_widget(Pace400M(name="Pace400M"))
        sm.add_widget(Pace100M(name="Pace100M"))
        sm.add_widget(Cycling100K(name="Cycling100K"))
        sm.add_widget(Cycling50K(name="Cycling50K"))
        sm.add_widget(Cycling10K(name="Cycling10K"))



        return sm


if __name__ == "__main__":
    MainApp().run()