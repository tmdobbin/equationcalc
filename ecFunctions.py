#A number of functions intended to be called from other scripts.
if __name__ == "__main__":
    print("This is a library file")

#else:
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
        return int(float(round1))

    print(standardFormCompToUser("2e+5"))

    def standardFormUserToInt(sForm):

        x = sForm.partition(" x 10^")
        answer = float(str(x[0]).strip()) * 10 ** float(str(x[2]).strip())

        if "e" in str(answer):
            answer = format(answer, ".7f")
        elif ".0000" in str(answer):
            answer = int(answer)

        return answer

    print(standardFormUserToInt("2.45 x 10^5"))
    print(standardFormUserToInt("2.45 x 10^-5"))



    def roundToNsf(value, nsf): 

        integer_part = math.floor(value)
        if integer_part > 0:
            integer_part_len = len(str(integer_part))
            return round(value, nsf-integer_part_len)
        else:
            str_value = str(value)
            #if of the form "8e-05"
            if '-' in str_value:
                index = int(str_value[str_value.find('-')+1:]) - 1
            else:
                st = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
                index = next((i for i, ch in enumerate(str(value)) if ch in st), None) - 2
            return round(value, index+nsf)

    def isFloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return 

    def getValue():
    
        valid = False
        while valid == False:
            
            try:
                value = float(input())
                if value > 0:
                    valid = True
                else:
                    print("You must enter a positive number")

            except:
                print("You must enter a positive number without any characters or symbols")
        return value
