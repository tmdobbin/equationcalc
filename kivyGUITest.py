from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import equationBuddyEdited as eb

class equationBuddy(App):
    
    def build(self):

        sm = ScreenManager()

        class mainMenuScreen(Screen):

            def __init__(self, **kwargs):

                super().__init__(**kwargs)
                
                layout = BoxLayout(orientation = "vertical")
                self.add_widget(layout)

                switchToQuadraticButton = Button(text = "Quadratic Calculator")
                switchToQuadraticButton.bind(on_press = lambda x: sm.switch_to(quadraticScreen))
                layout.add_widget(switchToQuadraticButton)

                switchToSuvatButton = Button(text = "Suvat Calculator")
                switchToSuvatButton.bind(on_press = lambda x: sm.switch_to(suvatScreen))
                layout.add_widget(switchToSuvatButton)

        class quadraticCalculatorScreen(Screen):
            
            def __init__(self, **kwargs):

                super().__init__(**kwargs)

                layout = BoxLayout(orientation = "vertical")
                self.add_widget(layout)

                inputBoxA = TextInput(multiline = False, hint_text = "a")
                layout.add_widget(inputBoxA)

                inputBoxB = TextInput(multiline = False, hint_text = "b")
                layout.add_widget(inputBoxB)

                inputBoxC = TextInput(multiline = False, hint_text = "c")
                layout.add_widget(inputBoxC)

                calculateButton = Button(text = "Calculate for x")
                calculateButton.bind(on_press = lambda x: print(f"tmp debug solve for x {inputBoxA.text=} {inputBoxB.text=} {inputBoxC.text=}"))
                layout.add_widget(calculateButton)

                backButton = Button(text = "Back to main menu")
                backButton.bind(on_press = lambda x: sm.switch_to(mainScreen))
                layout.add_widget(backButton)


        class suvatCalculatorScreen(Screen):

            def __init__(self, **kwargs):

                super().__init__(**kwargs)

                layout = BoxLayout(orientation = "vertical")
                self.add_widget(layout)

                inputBoxS = TextInput(multiline = False, hint_text = "s")
                layout.add_widget(inputBoxS)

                inputBoxU = TextInput(multiline = False, hint_text = "u")
                layout.add_widget(inputBoxU)

                inputBoxV = TextInput(multiline = False, hint_text = "v")
                layout.add_widget(inputBoxV)

                inputBoxA = TextInput(multiline = False, hint_text = "a")
                layout.add_widget(inputBoxA)

                inputBoxT = TextInput(multiline = False, hint_text = "t")
                layout.add_widget(inputBoxT)

                calculateButton = Button(text = "Calculate missing values")
                calculateButton.bind(on_press = lambda x: suvat(inputBoxS.text, inputBoxU.text, inputBoxV.text, inputBoxA.text, inputBoxT.text))
                layout.add_widget(calculateButton)

                backButton = Button(text = "Back to main menu")
                backButton.bind(on_press = lambda x: sm.switch_to(mainScreen))
                layout.add_widget(backButton)

                answerBox = Label(text = "Answer goes here (DEBUG)")
                layout.add_widget(answerBox)

                def suvat(s, u, v, a, t): #tmp before they are imported from main file

                    answerBox.text = str(eb.suvat(s, u, v, a, t))

        mainScreen = mainMenuScreen(name = "main")
        quadraticScreen = quadraticCalculatorScreen(name = "quadratic")
        suvatScreen = suvatCalculatorScreen(name = "suvat")

        sm.add_widget(mainScreen)
        sm.add_widget(quadraticScreen)
        sm.add_widget(suvatScreen)
        
        return sm

if __name__ == "__main__":
    equationBuddy().run()

