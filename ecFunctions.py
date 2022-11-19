#A number of functions intended to be called from other scripts.
def inputInt(message):
    valid = False
    while not valid:

        try:
            userInput = int(input(message))
            valid = True

        except ValueError:
            continue

    return userInput

def inputFloat(message):
    valid = False
    while not valid:

        try:
            userInput = float(input(message))
            valid = True

        except ValueError:
            continue
        
    return userInput
