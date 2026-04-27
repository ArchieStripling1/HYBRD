from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from SportSelection import selected
from kivy.app import App


class RaceScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Header
        title = Label(
            text="Select Your Race",
            font_size=36,
            size_hint=(1, 0.15),
            bold=True
        )

        layout.add_widget(title)

        # Scrollable area (important for many buttons)
        scroll = ScrollView(size_hint=(1, 0.75))
        content = BoxLayout(
            orientation='vertical',
            spacing=15,
            size_hint_y=None
        )
        content.bind(minimum_height=content.setter('height'))

        # Running
        content.add_widget(self.section_label("Running"))

        for text, value in [
            ("5K", "5k"),
            ("10K", "10k"),
            ("Half Marathon", "half"),
            ("Marathon", "marathon"),
        ]:
            content.add_widget(self.create_button(text, value))

        # Cycling
        content.add_widget(self.section_label("Cycling"))

        for text, value in [
            ("20K Ride", "cycle_20"),
            ("50K Ride", "cycle_50"),
            ("100K Ride", "cycle_100"),
        ]:
            content.add_widget(self.create_button(text, value))

        # Swimming
        content.add_widget(self.section_label("Swimming"))

        for text, value in [
            ("1000m", "swim_1000"),
            ("2000m", "swim_2000"),
            ("4000m", "swim_4000"),
        ]:
            content.add_widget(self.create_button(text, value))

        #Triathlon
        content.add_widget(self.section_label("Triathlon"))

        for text, value in [
            ("Half-IronMan", "ironman_70.3"),
            ("Full-IronMan", "ironman_140.6"),
        ]:
            content.add_widget(self.create_button(text, value))

        scroll.add_widget(content)
        layout.add_widget(scroll)


        next_btn = Button(
            text="Next",
            size_hint=(1, 0.1),
            font_size=24,
            background_color=(0.2, 0.6, 1, 1)  # blue
        )
        next_btn.bind(on_press=self.go_next)

        layout.add_widget(next_btn)

        self.add_widget(layout)

        self.selected_race = None


    def section_label(self, text):
        return Label(
            text=text,
            font_size=26,
            size_hint=(1, None),
            height=40,
            bold=True
        )

    # Create Button for each race value
    def create_button(self, text, value):
        btn = Button(
            text=text,
            size_hint=(1, None),
            height=60,
            font_size=20,
            background_color=(0.9, 0.9, 0.9, 1)
        )
        btn.bind(on_press=lambda instance: self.select_race(value))
        return btn


    def select_race(self, race_value):
        self.selected_race = race_value
        App.get_running_app().data["race"] = race_value
        print("Selected race:", race_value)

    # go to first in queue of selected sports
    def go_next(self, instance):
        self.manager.current = selected[0]


    def go_back(self, instance):
        self.manager.current = "sport"