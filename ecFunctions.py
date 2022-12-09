#A number of functions intended to be called from other scripts.
# This comment can be deleted at any time, it is a temporary change to test the apk autobuild
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
		
    def standardFormCompToUser(answer):
        string = str(answer)
        round1 = str(round(float(string[:6]), 3))
        round2 = string[len(string)-3:]
        return "E =", round1, "x 10^" + round2

    def standardFormUserToInt(sForm):
        x = sForm.partition(" x 10^")
        if int(x[2]) < 0:
            answer = "0."
            for i in range(abs(int(x[2]))-1):
                answer += "0"
            answer += x[0]

        if int(x[2]) > 0:
            answer = x[0]
            for i in range(abs(int(x[2]))-1):
                answer += "0"

        return answer

