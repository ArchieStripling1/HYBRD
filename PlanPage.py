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
        PB = float(data.get("CurrentRunPB", 2))
        race = data.get("race")
        longest_run = int(data.get("Longest_Run"))
        weekly_miles = int(data.get("Weekly_Distance"))
        activity_days = data.get("ActivityDays")
        long_run_day = data.get("LongRunDay")
        weekly_hard_run = 0

        #Days in the week
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
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
        race_settings = {
            "5k": {
                "max_long_run" : 12
            },
            "10k": {
                "max_long_run" : 18
            },
            "half": {
                "max_long_run" : 28
            },
            "marathon": {
                "max_long_run" : 34
            }
        }

        if race == "5k":
            race_pace = PB / 5
        elif race == "10k":
            race_pace = PB / 10
        elif race == "half":
            race_pace = PB / 21.1
        elif race == "marathon":
            race_pace = PB / 42.2

        easy_pace = round(race_pace + 1.2, 2)
        tempo_pace = round(race_pace + 0.25, 2)
        interval_pace = round(race_pace - 0.15, 2)

        #Dictionary for the plan.
        plan = {}

        #For week in range 1 to the length of the current plan
        for week in range(1, plan_length + 1):

            week_name = f"Week {week}"

            plan[week_name] = {}

            current_weekly_distance = weekly_miles

            #Created a recovery week every 4 weeks which decrease the load
            recovery_week = False

            if week % 4 == 0:
                recovery_week = True
                current_weekly_distance *= 0.8
            else:
                current_weekly_distance *= 1.05


            for day in days:
                # Default
                workout = {
                    "type": "Rest"
                }
                plan[week_name][day] = workout

                # Long run
                if day == long_run_day:
                    distance_to_cover = (
                            race_settings[race]["max_long_run"] - longest_run
                    )

                    weekly_increase = (
                            distance_to_cover / max(plan_length - 2, 1)
                    )

                    long_run_distance = (
                            longest_run +
                            (weekly_increase * week)
                    )

                    # Prevent going over max
                    if long_run_distance > race_settings[race]["max_long_run"]:
                        long_run_distance = race_settings[race]["max_long_run"]

                    if recovery_week:
                        long_run_distance *= 0.8

                    workout = {
                        "type": "Long Run",
                        "distance": int(long_run_distance),
                        "pace": f"{easy_pace:.2f}/km"
                    }
                    plan[week_name][day] = workout

                # Other running days
                elif day in activity_days:

                    # First activity day = hard session
                    if weekly_hard_run == 0:

                        # Select actual session
                        if week % 2 == 0:
                            hard_type = "Tempo Run"

                            session = tempo_types[
                                week % len(tempo_types)
                                ]

                            workout_pace = tempo_pace

                        else:

                            hard_type = "Interval Run"

                            session = interval_types[
                                week % len(interval_types)
                                ]

                            workout_pace = interval_pace

                        # Create nested dict to store everything for the run
                        workout = {
                            "type": hard_type,
                            "session": session,
                            "pace": f"{workout_pace:.2f}/km"
                        }
                        plan[week_name][day] = workout

                    # Remaining = easy runs
                    else:
                        easy_distance = (
                            (current_weekly_distance - longest_run) / len(activity_days)
                        )

                        # Create nested dict to store everything for the run
                        workout = {
                            "type": "Easy Run",
                            "distance": int(easy_distance),
                            "pace": f"{easy_pace:.2f}/km"
                        }
                        plan[week_name][day] = workout

                    #No more than one hard run a week right now.
                    weekly_hard_run += 1


            # Reset for next week
            weekly_hard_run = 0

        App.get_running_app().data["GeneratedPlan"] = plan


        for week, workouts in plan.items():
            print(f"\n======== {week} ========")

            for day, workout in workouts.items():
                print(day, "->", workout)





