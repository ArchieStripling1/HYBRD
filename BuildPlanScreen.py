from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from SportSelection import selected

class RaceScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        #Race Type

        #Distance

        #Current Weekly Mileage

        #Current Longest Effort

        #Current PB

        #Length of Plan

        #Sessions per activity per week

        #Days Available

        #Long Distance Effort Day

        #Build Plan Button

