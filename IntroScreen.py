from kivy.graphics import Color, RoundedRectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, SlideTransition, FadeTransition
from kivy.animation import Animation

from Theme import *


class IntroScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        root = FloatLayout()

        with root.canvas.before:
            Color(*BG)
            self.bg = RoundedRectangle(pos=root.pos, size=root.size)

        root.bind(size=self.update_bg, pos=self.update_bg)

        title = Label(
            text="HYBRD",
            font_size=64,
            bold=True,
            color=TEXT,
            pos_hint={"center_x": 0.5, "center_y": 0.62}
        )

        subtitle = Label(
            text="Hybrid Athlete Planner",
            font_size=22,
            color=SUBTEXT,
            pos_hint={"center_x": 0.5, "center_y": 0.53}
        )

        tap = Label(
            text="Tap Anywhere To Begin",
            font_size=18,
            color=PRIMARY,
            pos_hint={"center_x": 0.5, "center_y": 0.18}
        )

        anim = Animation(opacity=0.3, duration=1) + Animation(opacity=1, duration=1)
        anim.repeat = True
        anim.start(tap)

        root.add_widget(title)
        root.add_widget(subtitle)
        root.add_widget(tap)

        self.add_widget(root)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def on_touch_down(self, touch):
        old_transition = self.manager.transition

        # Use fade ONLY for intro to sport
        self.manager.transition = FadeTransition(duration=0.4)

        self.manager.current = "sport"

        # Restore normal transition
        self.manager.transition = old_transition

        return super().on_touch_down(touch)