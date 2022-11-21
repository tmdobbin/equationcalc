from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
c = 3 * 10 ** 8

class equationBuddyGrid(GridLayout):

    def calcWavelength(self, wavelength="", frequency=""):

        try:

            if wavelength == "" and frequency == "":
                self.display.text = "Error - No values present"
    
            if frequency != "" and wavelength == "":
                self.display.text = (f"{round((c / float(frequency)), 3)}m")

            if wavelength != "" and frequency == "":
                self.display.text = (f"{round((c / float(wavelength)), 3)}hz")

            if wavelength != "" and frequency != "":
                self.display.text = "Error - Two values present"
        
        except ValueError:
            self.display.text = "ValueError"

class equationBuddyApp(App):
    def build(self):
        return equationBuddyGrid()

if __name__ == "__main__":
    equationBuddyApp().run()