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
        hard_run_types = ["Interval Run", "Tempo Run"]
        interval_types = [
            '1KM Repeats',
            'Mile Repeats',
            'Pyramid Intervals'
        ]
        tempo_types =  [
            'Tempo 3-2-1',
            'Tempo 2KM Repeats',
            'Over and under 1KMs',
            'Tempo 5KM',
            'Rolling 400s',
            'Tempo 4KM'
        ]
        run_index = 0
        weekly_hard_run = 0
        #Dictionary for the plan.
        plan = {}

        #For week in range 1 to the length of the current plan
        for week in range(1, plan_length + 1):
            #Create nested dictionary for each week in range
            week_name = f"Week {week}"
            plan[week_name] = {}
            #Create day for each day in the week
            for day in days:
                #For each day if an activity day the value of that day will = 'run'
                if day == long_run_day:
                    plan[week_name][day] = "Long Run"
                #For each day if it is a long run day the value of that day will = 'long run'
                elif day in activity_days:
                    plan[week_name][day] = {hard_run_types[run_index % len(hard_run_types)],
                                            interval_types[run_index % len(interval_types)]}
                    run_index += 1

                    if weekly_hard_run > 0:
                        plan[week_name][day] = "Easy Run"
                    weekly_hard_run += 1


                #Else the value of the day will be rest
                else:
                    plan[week_name][day] = "Rest"  # default value

            weekly_hard_run = 0

        print(plan)



