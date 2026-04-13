from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        mainLayout = BoxLayout(orientation='vertical')

        nextButton = Button(
            text="Next",
            font_size=40,
            background_color=(1, 1, 1, 1),  # RGBA, not string
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        mainLayout.add_widget(nextButton)

        return mainLayout


if __name__=="__main__":
        MainApp().run()


