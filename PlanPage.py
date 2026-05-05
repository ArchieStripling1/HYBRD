from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.togglebutton import ToggleButton

from SportSelection import selected
from kivy.app import App

class PlanPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen


    def on_enter(self):
        data = App.get_running_app().data
        plan_length = int(data.get("CurrentPlanLength", 0))
        activity_days = data.get("ActivityDays")
        long_run_day = data.get("LongRunDay")

        #Days in the week
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        #Dictionary for the plan.
        plan = {}

        #For week in range 1 to the length of the current plan
        for week in range(1, plan_length + 1):
            #Create nested dictionary for each week in range
            plan[f"Week {week}"] = {}
            #Create day for each day in the week
            for day in days:
                #For each day if an activity day the value of that day will = 'run'
                if day in activity_days and day is not long_run_day:
                    plan[f"Week {week}"][day] = "Run"
                #For each day if it is a long run day the value of that day will = 'long run'
                elif day == long_run_day:
                    plan[f"Week {week}"][day] = "Long Run"
                #Else the value of the day will be rest
                else:
                    plan[f"Week {week}"][day] = "Rest"  # default value


        print(plan)



