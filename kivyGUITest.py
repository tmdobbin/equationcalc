from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.lang import Builder
from functools import partial
import equationBuddy as eb
import kivy
import regex as re

TRANSITIONSPEED = 0.3

class equationBuddy(App): # Define the main class for the app
    
    def build(self): # Define the build process for the GUI

        sm = ScreenManager() # Setup the screen manager

        class mainMenuScreen(Screen): # Define the class for the main menu

            def __init__(self, **kwargs): # Make sure these widgets are created every time this class is initialised

                super().__init__(**kwargs)
                
                mainLayout = BoxLayout(orientation = "vertical") #Setup the main vertical layout
                self.add_widget(mainLayout) #Add to the mainMenuScreen object

                switchToQuadraticButton = Button(text = "Maths Calculators") # Create a button to switch to Quadratic Calculator.
                switchToQuadraticButton.bind(on_press = lambda x: sm.switch_to(mathsScreen, duration = TRANSITIONSPEED, direction = "left")) # lambda x: allows for buttons to run functions while passing variables.
                mainLayout.add_widget(switchToQuadraticButton) # Add button to the main Layout 

                switchToSuvatButton = Button(text = "Physics Calculators")
                switchToSuvatButton.bind(on_press = lambda x: sm.switch_to(physicsScreen, duration = TRANSITIONSPEED, direction = "left"))
                mainLayout.add_widget(switchToSuvatButton) #Same stuff

        class mathsSelectScreen(Screen):

            def __init__(self, **kwargs):

                super().__init__(**kwargs)

                mainLayout = BoxLayout(orientation = "vertical")
                self.add_widget(mainLayout)

                firstRow = BoxLayout(orientation = "horizontal")
                mainLayout.add_widget(firstRow)

                switchToQuadraticButton = Button(text = "Quadratic Calculator") # Create a button to switch to Quadratic Calculator.
                switchToQuadraticButton.bind(on_press = lambda x: sm.switch_to(quadraticScreen, duration = TRANSITIONSPEED, direction = "left")) # lambda x: allows for buttons to run functions while passing variables.
                firstRow.add_widget(switchToQuadraticButton) # Add button to the main Layout 

                switchToSuvatButton = Button(text = "Suvat Calculator")
                switchToSuvatButton.bind(on_press = lambda x: sm.switch_to(suvatScreen, duration = TRANSITIONSPEED, direction = "left"))
                firstRow.add_widget(switchToSuvatButton) #Same stuff

                secondRow = BoxLayout(orientation = "horizontal")
                mainLayout.add_widget(secondRow)

                switchToAreaButton = Button(text = "Area Calculators")
                switchToAreaButton.bind(on_press = lambda x: sm.switch_to(areaSelScreen, duration = TRANSITIONSPEED, direction = "left"))
                secondRow.add_widget(switchToAreaButton)

                switchToPascalsLineButton = Button(text = "Pascal's Line")
                switchToPascalsLineButton.bind(on_press = lambda x: sm.switch_to(pascalsLineScreen, duration = TRANSITIONSPEED, direction = "left"))
                secondRow.add_widget(switchToPascalsLineButton)

                backButton = Button(text = "Back")
                backButton.bind(on_press = lambda x: sm.switch_to(mainScreen, direction = "right", duration = TRANSITIONSPEED))
                mainLayout.add_widget(backButton)
                
        class pascalsLineCalculatorScreen(Screen):

            def __init__(self, **kwargs):

                super().__init__(**kwargs)

                mainLayout = BoxLayout(orientation = "vertical")
                self.add_widget(mainLayout)

                answerLabel = Label(text = "Tmp debug text")
                mainLayout.add_widget(answerLabel)

                rowInputBox = TextInput(
                    multiline = False, 
                    hint_text = "Row", 
                    input_type = "text",
                    input_filter = "int")

                mainLayout.add_widget(rowInputBox)

                calculateButton = Button(text = "Calculate")
                calculateButton.bind(on_press = lambda x: pascalsLine(int(rowInputBox.text)))
                mainLayout.add_widget(calculateButton)

                backButton = Button(text = "Back")
                backButton.bind(on_press = lambda x: sm.switch_to(mathsScreen, direction = "right", duration = TRANSITIONSPEED))
                mainLayout.add_widget(backButton)

                def pascalsLine(row):
                    answerLabel.text = str(eb.pascalsLine(row))

        class areaSelectScreen(Screen):

            def __init__(self, **kwargs):

                super().__init__(**kwargs)

                mainLayout = BoxLayout(orientation = "vertical")
                self.add_widget(mainLayout)

                firstRow = BoxLayout(orientation = "horizontal")
                mainLayout.add_widget(firstRow)

                switchToQuadraticButton = Button(text = "Square") # Create a button to switch to Quadratic Calculator.
                switchToQuadraticButton.bind(on_press = lambda x: print("Square button pressed")) # lambda x: allows for buttons to run functions while passing variables.
                firstRow.add_widget(switchToQuadraticButton) # Add button to the main Layout 

                switchToSuvatButton = Button(text = "Triangle")
                switchToSuvatButton.bind(on_press = lambda x: print("Triangle button pressed"))
                firstRow.add_widget(switchToSuvatButton) #Same stuff

                secondRow = BoxLayout(orientation = "horizontal")
                mainLayout.add_widget(secondRow)

                switchToAreaButton = Button(text = "TMP BTN")
                switchToAreaButton.bind(on_press = lambda x: print("DEBUG - TMP BUTTON PRESSED"))
                secondRow.add_widget(switchToAreaButton)

                switchToTmpScreenButton = Button(text = "TMP BTN")
                switchToTmpScreenButton.bind(on_press = lambda x: print("DEBUG - TMP BUTTON PRESSED"))
                secondRow.add_widget(switchToTmpScreenButton)

                backButton = Button(text = "Back")
                backButton.bind(on_press = lambda x: sm.switch_to(mathsScreen, direction = "right", duration = TRANSITIONSPEED))
                mainLayout.add_widget(backButton)


        class physicsSelectScreen(Screen):

            def __init__(self, **kwargs):

                super().__init__(**kwargs)

                mainLayout = BoxLayout(orientation = "vertical")
                self.add_widget(mainLayout)

                switchToAreaButton = Button(text = "TMP BTN")
                switchToAreaButton.bind(on_press = lambda x: print("DEBUG - Physics button 1 BUTTON PRESSED"))
                mainLayout.add_widget(switchToAreaButton)

                switchToTmpScreenButton = Button(text = "TMP BTN")
                switchToTmpScreenButton.bind(on_press = lambda x: print("DEBUG - Physics button 2 BUTTON PRESSED"))
                mainLayout.add_widget(switchToTmpScreenButton)

                backButton = Button(text = "Back")
                backButton.bind(on_press = lambda x: sm.switch_to(mainScreen, direction = "right", duration = TRANSITIONSPEED))
                mainLayout.add_widget(backButton)

        class quadraticCalculatorScreen(Screen): #Define the screen for the quadratic calculator
            
            def __init__(self, **kwargs):

                super().__init__(**kwargs)

                mainLayout = BoxLayout(orientation = "vertical") #Main vertical layout again
                self.add_widget(mainLayout)

                inputBoxA = TextInput(
                    multiline = False, 
                    hint_text = "a", 
                    input_type = "text",
                    input_filter = "float") #Input boxes

                mainLayout.add_widget(inputBoxA) 

                inputBoxB = TextInput(
                    multiline = False, 
                    hint_text = "b", 
                    input_type = "text",
                    input_filter = "float") # input_type = number is to bring up numpad on mobile devices

                mainLayout.add_widget(inputBoxB)

                inputBoxC = TextInput(
                    multiline = False, 
                    hint_text = "c", 
                    input_type = "text",
                    input_filter = "float") # input_filter is to only allow float type numbers.

                mainLayout.add_widget(inputBoxC)

                roundingLayout = BoxLayout(orientation = "horizontal") # Make a nested horizontal layout for the rounding text and checkbox
                mainLayout.add_widget(roundingLayout)

                roundingLabel = Label(text = "Rounding", size_hint = (0.3, 1)) # Add the text label on the left
                roundingLayout.add_widget(roundingLabel)

                roundingDropdown = DropDown() # This snippet waa taken from the official kivy docs
                options = ["None", "3sf", "3dp", "2dp", "1dp"]
                for option in options:
                    # When adding widgets, we need to specify the height manually
                    # (disabling the size_hint_y) so the dropdown can calculate
                    # the area it needs.

                    btn = Button(text=option, size_hint_y=None, height=100)

                    # for each button, attach a callback that will call the select() method
                    # on the dropdown. We'll pass the text of the button as the data of the
                    # selection.
                    btn.bind(on_release=lambda btn: roundingDropdown.select(btn.text))

                    # then add the button inside the dropdown
                    roundingDropdown.add_widget(btn)

                # create a big main button
                mainbutton = Button(text='Choose Rounding', size_hint=(0.7, 1))

                # show the dropdown menu when the main button is released
                # note: all the bind() calls pass the instance of the caller (here, the
                # mainbutton instance) as the first argument of the callback (here,
                # dropdown.open.).
                mainbutton.bind(on_release=roundingDropdown.open)

                # one last thing, listen for the selection in the dropdown list and
                # assign the data to the button text.
                roundingDropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

                roundingLayout.add_widget(mainbutton)

                calculationLayout = BoxLayout(orientation = "horizontal") #Another nested layout for calculation stuff
                mainLayout.add_widget(calculationLayout)

                calculateButton = Button(text = "Calculate for x")
                calculateButton.bind(on_press = lambda x: quadratic(inputBoxA.text, inputBoxB.text, inputBoxC.text, mainbutton.text))
                calculationLayout.add_widget(calculateButton)

                answerBox = Label(text = "") # Default/placeholder text before answer is calculated
                calculationLayout.add_widget(answerBox)

                backButton = Button(text = "Back")
                backButton.bind(on_press = lambda x: sm.switch_to(mathsScreen, direction = "right", duration = TRANSITIONSPEED))
                mainLayout.add_widget(backButton) # Back button switches back to the main screen, reversing the transition.

                
                def quadratic(a, b, c, rounding): # Function that returns the state of the roundingCheckbox.

                    answerBox.text = eb.quadraticFormula(a, b, c, rounding)


        class suvatCalculatorScreen(Screen):

            def __init__(self, **kwargs):

                super().__init__(**kwargs)

                mainLayout = BoxLayout(orientation = "vertical") #Same stuff as before
                self.add_widget(mainLayout)

                inputBoxS = TextInput(
                    multiline = False, 
                    hint_text = "s", 
                    input_type = "text",
                    input_filter = "float")

                mainLayout.add_widget(inputBoxS)

                inputBoxU = TextInput(
                    multiline = False, 
                    hint_text = "u", 
                    input_type = "text",
                    input_filter = "float")

                mainLayout.add_widget(inputBoxU)

                inputBoxV = TextInput(
                    multiline = False, 
                    hint_text = "v", 
                    input_type = "text",
                    input_filter = "float")

                mainLayout.add_widget(inputBoxV)

                inputBoxA = TextInput(
                    multiline = False, 
                    hint_text = "a", 
                    input_type = "text",
                    input_filter = "float")

                mainLayout.add_widget(inputBoxA)

                inputBoxT = TextInput(
                    multiline = False, 
                    hint_text = "t", 
                    input_type = "text",
                    input_filter = "float")

                mainLayout.add_widget(inputBoxT)

                roundingLayout = BoxLayout(orientation = "horizontal")
                mainLayout.add_widget(roundingLayout)

                roundingLabel = Label(text = "Rounding")
                roundingLayout.add_widget(roundingLabel)

                roundingCheckbox = CheckBox(active = False)
                roundingLayout.add_widget(roundingCheckbox)

                calculateLayout = BoxLayout(orientation = "horizontal")
                mainLayout.add_widget(calculateLayout)

                calculateButton = Button(text = "Calculate missing values")
                calculateButton.bind(on_press = lambda x: suvat(inputBoxS.text, inputBoxU.text, inputBoxV.text, inputBoxA.text, inputBoxT.text, roundingCheckbox.active))
                calculateLayout.add_widget(calculateButton)

                answerBox = Label(text = "")
                calculateLayout.add_widget(answerBox)

                backButton = Button(text = "Back")
                backButton.bind(on_press = lambda x: sm.switch_to(mathsScreen, direction = "right", duration = TRANSITIONSPEED))
                mainLayout.add_widget(backButton)

                def suvat(s, u, v, a, t, rounding): #tmp before they are imported from main file

                    answerBox.text = str(eb.suvat(s, u, v, a, t, rounding))

        mainScreen = mainMenuScreen(name = "main") # Define the screens with names
        mathsScreen = mathsSelectScreen(name = "maths")
        physicsScreen = physicsSelectScreen(name = "physics")
        pascalsLineScreen = pascalsLineCalculatorScreen(name = "pascalsline")
        areaSelScreen = areaSelectScreen(name = "areasel")
        quadraticScreen = quadraticCalculatorScreen(name = "quadratic")
        suvatScreen = suvatCalculatorScreen(name = "suvat")

        sm.add_widget(mainScreen) # Add the screens to the main screen manager
        sm.add_widget(mathsScreen)
        sm.add_widget(physicsScreen)
        sm.add_widget(areaSelScreen)
        sm.add_widget(quadraticScreen)
        sm.add_widget(suvatScreen)
        
        return sm

if __name__ == "__main__":
    equationBuddy().run()

