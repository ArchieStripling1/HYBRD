from kivy.graphics import Color, RoundedRectangle
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
from Theme import *

class PlanPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # setup Kivy screen

        # Scroll area
        self.scroll = ScrollView()

        self.content = BoxLayout(
            orientation='vertical',
            spacing=30,
            padding=25,
            size_hint_y=None
        )

        self.content.bind(
            minimum_height=self.content.setter('height')
        )
        self.scroll.add_widget(self.content)

        self.add_widget(self.scroll)


    def on_enter(self):
        data = App.get_running_app().data
        race = data.get("race")
        plan_length = int(data.get("CurrentPlanLength", 0))
        PB = float(data.get(f"{race}_pb", 2))
        longest_run = int(data.get("Longest_Run"))
        weekly_miles = int(data.get("Weekly_Distance"))
        activity_days = data.get("ActivityDays")
        long_run_day = data.get("LongRunDay")
        level = data.get("Level")
        weekly_hard_run = 0

        #Days in the week
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # Idea for different types of intervals but is there a cleaner way to store this??

        interval_5k_types = {

        }
        interval_10k_types = {

        }
        interval_half_types = {

        }
        interval_marathon_types = {

        }
        tempo_5k_types = {

        }
        tempo_10k_types = {

        }
        tempo_half_types = {

        }
        tempo_marathon_types = {

        }



        interval_types = [
            '1KM Repeats x 5',
            'Mile Repeats x 3',
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
        #Variable settings that change for each race.
        raceDistance = 0

        if race == "5k":
            raceDistance = 5

            # Work out what their race pace based off their last PB
            predictedPace = PB - plan_length * 10
            race_pace = predictedPace / 5

            # Create different paces for different runs.
            easy_pace = formatPace(race_pace + 120)
            tempo_pace = formatPace(race_pace)
            interval_pace = formatPace(race_pace - 15)

        elif race == "10k":
            # if user has not run that far it will get the PB that they have,
            # not run a half-marathon yet so they will use their 10k PB for reference.
            raceDistance = 10

            if PB == 2.0:
                PB = float(data.get("5k_pb", 2))
                race_pace = PB / 5

            else:
                # Work out what their race pace based off their last PB
                predictedPace = PB - plan_length * 15
                race_pace = predictedPace/ 10

                # Create different paces for different runs.
                easy_pace = formatPace(race_pace + 105)
                tempo_pace = formatPace(race_pace)
                interval_pace = formatPace(race_pace - 15)
        elif race == "half":
            raceDistance = 21.1
            if PB == 2.0:
                PB = float(data.get("10k_pb", 2))
                race_pace = PB / 10
            else:
                # Work out what their race pace based off their last PB
                predictedPace = PB - plan_length * 20
                race_pace = predictedPace / 21.1

                # Create different paces for different runs.
                easy_pace = formatPace(race_pace + 90)
                tempo_pace = formatPace(race_pace)
                interval_pace = formatPace(race_pace - 15)
        elif race == "marathon":
            raceDistance = 42.2
            if PB == 2.0:
                PB = float(data.get("half_pb", 2))
                race_pace = PB / 21.1
            else:
                # Work out what their race pace based off their last PB
                predictedPace = PB - plan_length * 25
                race_pace = predictedPace / 42.2

                # Create different paces for different runs.
                easy_pace = formatPace(race_pace + 75)
                tempo_pace = formatPace(race_pace)
                interval_pace = formatPace(race_pace - 15)


        # Change max distances based of their longest run and race distance.
        if raceDistance > longest_run:
            race_settings = {
                "5k": {
                    "max_long_run": 5,
                    "max_easy_run": 3,
                    "speed": "fast"
                },
                "10k": {
                    "max_long_run": 10,
                    "max_easy_run": 6,
                    "speed": "semi-fast"

                },
                "half": {
                    "max_long_run": 20,
                    "max_easy_run": 8,
                    "speed": "medium"
                },
                "marathon": {
                    "max_long_run": 34,
                    "max_easy_run": 15,
                    "speed": "slow"
                }
            }
        else:
            race_settings = {
                "5k": {
                    "max_long_run": 12,
                    "max_easy_run": 6,
                    "speed": "fast"
                },
                "10k": {
                    "max_long_run": 14,
                    "max_easy_run": 8,
                    "speed": "semi-fast"

                },
                "half": {
                    "max_long_run": 23,
                    "max_easy_run": 13,
                    "speed": "medium"
                },
                "marathon": {
                    "max_long_run": 38,
                    "max_easy_run": 20,
                    "speed": "slow"
                }
            }

        print(PB)

        #Dictionary for the plan.
        plan = {}
        current_weekly_distance = 0

        #For week in range 1 to the length of the current plan
        for week in range(1, plan_length + 1):

            week_name = f"Week {week}"

            plan[week_name] = {}

            #Created a recovery week every 4 weeks which decrease the load
            recovery_week = False

            if week % 4 == 0:
                recovery_week = True
                weekly_miles *= 0.8
            else:
                weekly_miles *= 1.05


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
                        "pace": easy_pace
                    }
                    plan[week_name][day] = workout

                    #Keep track of how far they have run this week.
                    current_weekly_distance += long_run_distance

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
                            "pace": workout_pace
                        }
                        plan[week_name][day] = workout
                        current_weekly_distance += 8

                    # Remaining = easy runs
                    else:
                        easy_distance = (
                            (weekly_miles / len(activity_days))
                        )

                        # Prevent going over max
                        if easy_distance > race_settings[race]["max_easy_run"]:
                            easy_distance = race_settings[race]["max_easy_run"]

                        if recovery_week:
                            easy_distance *= 0.8

                        # Create nested dict to store everything for the run
                        workout = {
                            "type": "Easy Run",
                            "distance": int(easy_distance),
                            "pace": easy_pace
                        }
                        plan[week_name][day] = workout
                        current_weekly_distance += easy_distance

                    #No more than one hard run a week right now.
                    weekly_hard_run += 1

                # Race Week Workout
                if week == plan_length:
                    workout = {
                        "type": "Rest"
                    }
                    plan[week_name][day] = workout
                    if day == "Wednesday":
                        workout = {
                            "type": "Race Practice Session!",
                            "distance": "Race Pace Miles x 3",
                            "pace": tempo_pace
                        }
                        plan[week_name][day] = workout
                    if day == "Sunday":
                        workout = {
                            "type": "Race Day!",
                            "distance": race.capitalize(),
                            "pace": formatPace(race_pace)
                        }
                        plan[week_name][day] = workout



            # Reset for next week
            weekly_hard_run = 0
            weekly_miles = current_weekly_distance
            current_weekly_distance = 0

        App.get_running_app().data["GeneratedPlan"] = plan

        # Get Week and workout in that week
        for week, workouts in plan.items():

            # Initialize Card
            card = BoxLayout(
                orientation='vertical',
                spacing=15,
                padding=20,
                size_hint_y=None
            )

            # Dynamic height
            card.bind(minimum_height=card.setter("height"))

            # Card background
            with card.canvas.before:
                Color(*CARD)
                card.rect = RoundedRectangle(
                    pos=card.pos,
                    size=card.size,
                    radius=[25]
                )

            # Keep card updated
            def update_rect(instance, value):
                instance.rect.pos = instance.pos
                instance.rect.size = instance.size

            # Bind Card with updated variables
            card.bind(pos=update_rect, size=update_rect)

            # Week Title
            week_label = Label(
                text=week,
                font_size=30,
                bold=True,
                color=TEXT,
                size_hint_y=None,
                height=50
            )

            # Add Week to Card
            card.add_widget(week_label)

            # Get the day and workout in workouts
            for day, workout in workouts.items():

                # Skip rest days as these don't need to be displayed in the plan section
                if workout["type"] == "Rest":
                    continue

                # Get all Workout info
                workout_text = f"[b]{day}[/b]\n"
                workout_text += f"{workout['type']}\n"

                if "session" in workout:
                    workout_text += f"Session: {workout['session']}\n"

                if "distance" in workout:
                    workout_text += f"Distance: {workout['distance']}\n"

                if "pace" in workout:
                    workout_text += f"Pace: {workout['pace']}"

                # Workout Card
                workout_card = BoxLayout(
                    orientation='vertical',
                    padding=15,
                    size_hint_y=None,
                    height=140
                )

                # Workout card background
                with workout_card.canvas.before:
                    Color(*SUBTEXT)
                    workout_card.rect = RoundedRectangle(
                        pos=workout_card.pos,
                        size=workout_card.size,
                        radius=[18]
                    )
                # Keep Workout Updated
                def update_workout_rect(instance, value):
                    instance.rect.pos = instance.pos
                    instance.rect.size = instance.size


                # Bind Card with updated variables
                workout_card.bind(
                    pos=update_workout_rect,
                    size=update_workout_rect
                )

                # Day workouts
                day_label = Label(
                    text=workout_text,
                    markup=True,
                    font_size=18,
                    color=TEXT,
                    halign="left",
                    valign="middle",
                    text_size=(650, None)
                )
                # Add day and workout to workout card
                workout_card.add_widget(day_label)

                # Add workout card to week card.
                card.add_widget(workout_card)

            # Add whole week card
            self.content.add_widget(card)


    def restart(self, instance):

        self.manager.current = "intro"
        self.data = {}




# Format their paces
def formatPace(PB):

    # Turn seconds into minutes and seconds rounded to the nearest division of 5.
    minutes = int(PB // 60)
    seconds = 5 * int(round((PB % 60)/ 5))

    # Return the formated string.
    return f"{minutes}:{seconds:02d}/km"




