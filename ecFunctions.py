#A number of functions intended to be called from other scripts.
if __name__ == "__main__":
    print("This is a library file")

else:
    def inputInt(message):
        valid = False
        while not valid:

            try:
                userInput = int(input(message))
                valid = True

            except ValueError:
                valid = False

        return userInput

    def inputFloat(message):
        valid = False
        while not valid:

            try:
                userInput = float(input(message))
                valid = True

            except ValueError:
                valid = False
            
        return userInput

    def standardForm():
        string = str(answer)
        round1 = str(round(float(string[:6]), 3))
        round2 = string[len(string)-3:]
        return ("E =", round1, "x 10^" + round2)
		
		
