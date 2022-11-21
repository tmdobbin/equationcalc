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
