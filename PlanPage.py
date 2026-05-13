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
        PB = float(data.get("CurrentPB", 0))
        race = data.get("race")
        longest_run = int(data.get("Longest_Run"))
        weekly_miles = int(data.get("Weekly_Distance"))
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
        race_run_types = {"5k": 5, "10k": 10, "half": 21.1, "marathon": 42.2}
        run_index = 0
        long_run_progression = 0
        weekly_hard_run = 0
        value = race_run_types[race]

        #Dictionary for the plan.
        plan = {}

        #For week in range 1 to the length of the current plan
        for week in range(1, plan_length + 1):
            week_name = f"Week {week}"
            plan[week_name] = {}
            # Alternate workout type each week
            hard_type = hard_run_types[week % len(hard_run_types)]

            # Select actual session
            if hard_type == "Interval Run":
                session = interval_types[week % len(interval_types)]
            else:
                session = tempo_types[week % len(tempo_types)]

            for day in days:
                # Default
                plan[week_name][day] = {
                    "type": "Rest"
                }
                # Long run
                if day == long_run_day:
                    #Round to the nearest whole number
                    long_run_distance = round(
                        longest_run + (week * 1.5),
                        1
                    )

                    # Prevent overreaching
                    if long_run_distance > value * 0.8:
                        long_run_distance = round(value * 0.8, 1)

                    #Create nested dict to store everything for the run
                    plan[week_name][day] = {
                        "type": "Long Run",
                        "distance": long_run_distance
                    }

                # Other running days
                elif day in activity_days:

                    # First activity day = hard session
                    if weekly_hard_run == 0:

                        # Create nested dict to store everything for the run
                        plan[week_name][day] = {
                            "type": hard_type,
                            "session": session
                        }

                    # Remaining = easy runs
                    else:
                        # Round to the nearest whole number
                        easy_distance = round(
                            weekly_miles / len(activity_days) * 0.6,
                            1
                        )
                        # Create nested dict to store everything for the run
                        plan[week_name][day] = {
                            "type": "Easy Run",
                            "distance": easy_distance
                        }
                    #No more then one hard run a week right now.
                    weekly_hard_run += 1

            # Reset for next week
            weekly_hard_run = 0

        print(plan)



