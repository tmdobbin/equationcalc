from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder
import equationBuddy as eb

TRANSITIONSPEED = 0.3

class equationBuddy(App):
    
    def build(self):

        sm = ScreenManager()

        class mainMenuScreen(Screen):

            def __init__(self, **kwargs):

                super().__init__(**kwargs)
                
                layout = BoxLayout(orientation = "vertical")
                self.add_widget(layout)

                switchToQuadraticButton = Button(text = "Quadratic Calculator")
                switchToQuadraticButton.bind(on_press = lambda x: sm.switch_to(quadraticScreen, duration = TRANSITIONSPEED))
                layout.add_widget(switchToQuadraticButton)

                switchToSuvatButton = Button(text = "Suvat Calculator")
                switchToSuvatButton.bind(on_press = lambda x: sm.switch_to(suvatScreen, duration = TRANSITIONSPEED))
                layout.add_widget(switchToSuvatButton)

        class quadraticCalculatorScreen(Screen):
            
            def __init__(self, **kwargs):

                super().__init__(**kwargs)

                layout = BoxLayout(orientation = "vertical")
                self.add_widget(layout)

                inputBoxA = TextInput(multiline = False, hint_text = "a", input_type = "number", input_filter = "float")
                layout.add_widget(inputBoxA)

                inputBoxB = TextInput(multiline = False, hint_text = "b", input_type = "number", input_filter = "float")
                layout.add_widget(inputBoxB)

                inputBoxC = TextInput(multiline = False, hint_text = "c", input_type = "number", input_filter = "float")
                layout.add_widget(inputBoxC)

                roundingLayout = BoxLayout(orientation = "horizontal")
                layout.add_widget(roundingLayout)

                roundingLabel = Label(text = "Rounding")
                roundingLayout.add_widget(roundingLabel)

                roundingCheckbox = CheckBox(active = False)
                roundingLayout.add_widget(roundingCheckbox)

                calculationLayout = BoxLayout(orientation = "horizontal")
                layout.add_widget(calculationLayout)

                calculateButton = Button(text = "Calculate for x")
                calculateButton.bind(on_press = lambda x: (print(f"tmp debug solve for x {inputBoxA.text=} {inputBoxB.text=} {inputBoxC.text=}"), getRoundingState(roundingCheckbox)))
                calculationLayout.add_widget(calculateButton)

                answerBox = Label(text = "Answer goes here (DEBUG)")
                calculationLayout.add_widget(answerBox)

                backButton = Button(text = "Back to main menu")
                backButton.bind(on_press = lambda x: sm.switch_to(mainScreen, transition=SlideTransition(direction = "right", duration = TRANSITIONSPEED)))
                layout.add_widget(backButton)

                
                def getRoundingState(checkbox):
                    state = roundingCheckbox.active
                    print("Rounding checkbox is active:", state)
                    answerBox.text = str(state) + " - DEBUG, roundingCheckbox.active state"


        class suvatCalculatorScreen(Screen):

            def __init__(self, **kwargs):

                super().__init__(**kwargs)

                layout= BoxLayout(orientation = "vertical")
                self.add_widget(layout)

                inputBoxS = TextInput(multiline = False, hint_text = "s", input_type = "number", input_filter = "float")
                layout.add_widget(inputBoxS)

                inputBoxU = TextInput(multiline = False, hint_text = "u", input_type = "number", input_filter = "float")
                layout.add_widget(inputBoxU)

                inputBoxV = TextInput(multiline = False, hint_text = "v", input_type = "number", input_filter = "float")
                layout.add_widget(inputBoxV)

                inputBoxA = TextInput(multiline = False, hint_text = "a", input_type = "number", input_filter = "float")
                layout.add_widget(inputBoxA)

                inputBoxT = TextInput(multiline = False, hint_text = "t", input_type = "number", input_filter = "float")
                layout.add_widget(inputBoxT)

                roundingLayout = BoxLayout(orientation = "horizontal")
                layout.add_widget(roundingLayout)

                roundingLabel = Label(text = "Rounding")
                roundingLayout.add_widget(roundingLabel)

                roundingCheckbox = CheckBox(active = False)
                roundingLayout.add_widget(roundingCheckbox)

                calculateLayout = BoxLayout(orientation = "horizontal")
                layout.add_widget(calculateLayout)

                calculateButton = Button(text = "Calculate missing values")
                calculateButton.bind(on_press = lambda x: suvat(inputBoxS.text, inputBoxU.text, inputBoxV.text, inputBoxA.text, inputBoxT.text, roundingCheckbox.active))
                calculateLayout.add_widget(calculateButton)

                answerBox = Label(text = "Answer goes here (DEBUG)")
                calculateLayout.add_widget(answerBox)

                backButton = Button(text = "Back to main menu")
                backButton.bind(on_press = lambda x: sm.switch_to(mainScreen, transition=SlideTransition(direction = "right", duration = TRANSITIONSPEED)))
                layout.add_widget(backButton)

                def suvat(s, u, v, a, t, rounding): #tmp before they are imported from main file

                    answerBox.text = str(eb.suvat(s, u, v, a, t, rounding))

        mainScreen = mainMenuScreen(name = "main")
        quadraticScreen = quadraticCalculatorScreen(name = "quadratic")
        suvatScreen = suvatCalculatorScreen(name = "suvat")

        sm.add_widget(mainScreen)
        sm.add_widget(quadraticScreen)
        sm.add_widget(suvatScreen)
        
        return sm

if __name__ == "__main__":
    equationBuddy().run()

