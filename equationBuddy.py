#Version 0.2.1
import math
import ecFunctions as ec
from math import factorial
pi = math.pi

def roundToNsf(value, nsf): # Code snippet from https://stackoverflow.com/questions/45178528/round-to-significant-figures-in-python (Uladzimir Treihis)
    """
    Rounds the number to the provided number of significant figures.
    """

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

def pascalsLine(n):

	
	answer5 = ""
	for i in range(n):
		b = n - i
		facN = factorial(n)
		facI = factorial(i)
		facB = factorial(b)
		answer4 = facI * facB
		answer4 = facN / answer4
		answer4 = float(answer4)
		nlen = len(str(answer4))
		answer4 = str(answer4)
		answer4 = (answer4[:nlen-2])
		answer5 = answer5 +" "+ str(answer4)
	
	return (answer5 +" "+"1")


def suvat(s,u,v,a,t,rounding):

	def errorChecker(num, solvingFor):
		try:
			float(num)
			if rounding == "1dp":
				num = round(num, 1)
			elif rounding == "2dp":
				num = round(num, 2)
			elif rounding == "3dp":
				num = round(num, 3)
			#elif rounding == "3sf":
				#num = roundToNsf(num, 3)
				print("number has been rounded to 3dp", "NUM", num)
			else:
				pass
			return f"{solvingFor} = {num}"
		except:
			return ("This scenario is impossible")
	
	if s != "":
		s = float(s)

	if u != "":
		u = float(u)

	if v != "":
		v = float(v)

	if a != "":
		a = float(a)

	if t != "":
		t = float(t)

	answer = ""
	answers = ""
	
	if isFloat(t) == True and t < 0:
		return ("Time can not be negative")
		
	elif isFloat(v) == True and isFloat(u) == True and isFloat(a) == True and v < u and a > 0:
		return ("This scenario is not possible")
		
	elif isFloat(v) == True and isFloat(u) == True and isFloat(a) == True and v > u and a < 0:
		return ("This scenario is not possible")
		
	elif a == 0 and v != u:
		return ("This scenario is not possible") 
		
	elif v == u and a!= 0 and v != "" and u != "":
		return ("This scenario is not possible")
		
	
	if u == "" and v != "" and a != "" and t != "":
		answer = a * t
		answer = v - answer
		answers = answers + "\n" + (errorChecker(answer, "u"))
	
	if v == "" and u != "" and a != "" and t != "":
		answer = a * t
		answer = answer + u
		answers = answers + "\n" + (errorChecker(answer, "v"))
		
	if a == "" and v != "" and u != "" and t != "":
		answer = v - u 
		if t == 0:
			return ("Time can not be equal to 0 in this scenario")
			
		answer = answer / t 
		errorChecker(answer, "a")
	
	if t == "" and v != "" and u !="" and a != "":
		answer = v - u 
		if a == 0:
			return ("Acceleration can not be equal to 0 in this scenario")
			
		answer = answer / a 
		errorChecker(answer, "t")
		
	if s == "" and v != "" and t != "" and a != "":
		answer = v * t 
		answer = answer - (0.5 * a * (t*t))
		answers = answers + "\n" + (errorChecker(answer, "s"))
		
	if v == "" and s != "" and a != "" and t != "":
		answer = a * (t*t)
		answer = s + answer
		if t == 0:
			return ("Time can not be equal to 0 in this scenario")
		answer = answer / (t * 2)
		answers = answers + "\n" + (errorChecker(answer, "v"))
			
	if a == "" and v != "" and t != "" and s != "":
		answer = v * t 
		answer = answer - s 
		answer = answer * 2 
		if t == 0:
			return ("Time can not be equal to 0 in this scenario")
			
		answer = answer / (t * t)
		answers = answers + "\n" + (errorChecker(answer, "a"))
		
	if t == "" and v != "" and a != "" and s != "":
		answer = v * v 
		answer = answer - (2 * a * s)
		answer = answer ** (1/2)
		answer = v - answer
		if a == 0:
			return ("Acceleration can not be equal to 0 in this scenario")

		answer = answer / a  
		answers = answers + "\n" + (errorChecker(answer, "t"))
		
	if s == "" and u != "" and t != "" and a != "":
		answer = t * t
		answer = answer * a * 0.5 
		answer = (u * t) + answer
		answers = answers + "\n" + (errorChecker(answer, "s"))
		
	if u == "" and s != "" and a != "" and t != "":
		answer = t * t 
		answer = answer * a 
		answer = s - answer
		if t == 0:
			return ("Time can not be equal to 0 in this scenario")
			
		answer = answer / (2 * t)
		answers = answers + "\n" + (errorChecker(answer, "u"))
		
	if a == "" and s != "" and u != "" and t != "":
		answer = u * t
		answer = s - answer
		answer = 2 * answer
		if t == 0:
			return ("Time can not be equal to 0 in this scenario")
			
		answer = answer / (t * t)
		answers = answers + "\n" + (errorChecker(answer, "a"))
	
	if t == "" and a != "" and s != "" and u != "":
		uSq = u * u 
		answer = (2 * a * s)
		answer = answer + uSq
		answer = answer ** (1/2)
		answer = answer - u
		if a == 0:
			return ("Acceleration can not be equal to 0 in this scenario")
			
		answer = answer / a
		answers = answers + "\n" + (errorChecker(answer, "t"))
		
	if s == "" and t != "" and u != "" and v != "":
		answer = t / 2
		answer = answer * (u + v)
		answers = answers + "\n" + (errorChecker(answer, "s"))
		
	if u == "" and s != "" and t != "" and v != "":
		answer = 2 * s
		if t == 0:
			return ("Time can not be equal to 0 in this scenario")
			
		answer = answer / t
		answer = answer + v
		answers = answers + "\n" + (errorChecker(answer, "u"))
		
	if v == "" and s != "" and t != "" and u != "":
		answer = 2 * s 
		if t == 0:
			return ("Time can not be equal to 0 in this scenario")
			
		answer = answer / t
		answer = answer - u 
		answers = answers + "\n" + (errorChecker(answer, "v"))
	
	if t == "" and s != "" and u != "" and v != "":
		answer = 2 * s
		answer = answer / (u + v)
		answers = answers + "\n" + (errorChecker(answer, "t"))
		
	if s == "" and u != "" and v != "" and a != "":
		answer = (u * u) + (v * v)
		answer2 = (2 * a)
		if answer2 == 0:
			return ("Acceleration can not be equal to 0 in this scenario")
		answer = answer / answer2
		answers = answers + "\n" + (errorChecker(answer, "s"))
		
	if u == "" and a != "" and s != "" and v != "":
		answer = (2 * a * s) - (v * v)
		answer = answer ** (1/2)
		answers = answers + "\n" + (errorChecker(answer, "u"))
		
	if v == "" and u != "" and a != "" and s != "":
		answer = (u * u) + (2 + a + s)
		answer = answer ** (1/2)
		answers = answers + "\n" + (errorChecker(answer, "v"))
		
	if a == "" and v != "" and u != "" and s != "":
		answer = (v * v) - (u * u)
		if s == 0:
			return ("Displacement can not be equal to 0 in this scenario")
		answer = answer / (2 * s)
		answers = answers + "\n" + (errorChecker(answer, "a"))

	if answers == "":
		return "Missing Values"

	return answers

def quadraticFormula(coA, coB, coC, rounding):

	# print(f"{rounding=}")
	
	finalresult = ""
	
	def QuadraticErrorChecker(X1, X2, rounding):

		finalresult = ""

		imaginaryCounter = 0
		if isinstance(X1, complex):
			# print("The first value is an imaginary number")
			imaginaryCounter = imaginaryCounter + 1
			
		if isinstance(X2, complex):
			# print("The second value is an imaginary number")
			imaginaryCounter = imaginaryCounter + 1
		elif X1 == X2:
			return f"x= {X1}"
			# print("This equation has 1 real root")

		if imaginaryCounter == 2:
			return ("This equation has no real roots.")

		if rounding == "1dp":

			X1 = round(X1, 1)
			if X1 > 0:

				X1 = -abs(X1)

			else:
				X1 = abs(X1)

			finalresult = f"x= {str(X1)}"

		elif rounding == "2dp":

			X1 = round(X1, 2)

			if X1 > 0:
				X1 = -abs(X1)

			else:
				X1 = abs(X1)

			finalresult = f"x= {str(X1)}"

		elif rounding == "3dp":

			X1 = round(X1, 3)

			if X1 > 0:
				X1 = -abs(X1)

			else:
				X1 = abs(X1)

			finalresult = f"x= {str(X1)}"

		#elif rounding == "3sf":

			# X1 = roundToNsf(X1, 3)

			# if X1 > 0:
			# 	X1 = -abs(X1)

			# else:
			# 	X1 = abs(X1)

			# finalresult = f"x= {str(X1)}"

		else:
			if X1 > 0:
				X1 = -abs(X1)

			else:
				X1 = abs(X1)
			finalresult = f"x= {str(X1)}"

		if rounding == "1dp":

			X2 = round(X2, 1)
			if X2 > 0:

				X2 = -abs(X2)

			else:
				X1 = abs(X2)

			finalresult = f"{finalresult}\nx= {str(X2)}"

		elif rounding == "2dp":

			X2 = round(X2, 2)

			if X2 > 0:
				X2 = -abs(X2)

			else:
				X2 = abs(X2)

			finalresult = f"{finalresult}\nx= {str(X2)}"

		elif rounding == "3dp":

			X2 = round(X2, 3)

			if X2 > 0:
				X2 = -abs(X2)

			else:
				X2 = abs(X2)

			finalresult = f"{finalresult}\nx= {str(X2)}"

		#elif rounding == "3sf":

			# X2 = roundToNsf(X2, 3)

			# if X2 > 0:
			# 	X2 = -abs(X2)

			# else:
			# 	X2 = abs(X2)

			# finalresult = f"{finalresult}\nx= {str(X2)}"

		else:
			if X2 > 0:
				X2 = -abs(X2)

			else:
				X2 = abs(X2)
			finalresult = f"{finalresult}\nx= {str(X2)}"

		return finalresult

	# print("{:=^70}".format("Quadratic Formula"))
	# print()
	if coA != "":
		coA = float(coA)
	else:
		return "Missing values"
	
	if coB != "":
		coB = float(coB)
	else:
		return "Missing values"

	if coC != "":
		coC = float(coC)
	else:
		return "Missing values"
	# print()
	
	if coA == 0:
		return ("This function requires a coefficient for A")
	if coB > 0: 
		conCoB = -abs(coB)
	if coA < 0:
		conCoB = abs(coB)
	else:
		conCoB = coB
		
	answer = (coB * coB) - (4 * coA * coC)
	answer = answer ** (1/2)
	answer1 = conCoB + answer
	answer1 = answer1 / (2 * coA)
	answer2 = conCoB - answer
	answer2 = answer2 / (2 * coA)
	finalresult = QuadraticErrorChecker(answer1, answer2, rounding)
	
	return finalresult
	
def physicsValues():
	
	print("{:=^70}".format("Physics Values"))
	print()
	print("Speed Of Light = 3 x 10^8 m/s")
	print("Electron Charge = 1.60 x 10^-19 C")
	print("Plancks Constant = 6.63 x 10^-34 J/s")
	print("Electron Mass = 9.11 x 10^-31 kg")
	print("Proton Mass = 1.67 x 10^-27 kg")
	print("Neutron Mass = 1.67 x 10^-27 kg")
	print("Gravity = 9.81 N/kg")

def photonEnergy():
	print("{:=^70}".format("PHOTON ENERGY"))
	print()
	
	speedOfLight = 3*10**8
	plancksConstant = 6.63*10**-34

	wavelength = input("wavelength (in nanometres) = ")

	if wavelength == "":
		frequency = input("frequency (in hertz) = ")

		if " x 10^" in frequency:
			frequency = ec.standardFormUserToInt(frequency)
			E = str(plancksConstant * frequency)
			E1 = E[:5]
			E2 = E[len(E)-3:]
			E3 = "E = "+E1+" x 10^"+E2
			print(E3)

		else:
			frequency = float(frequency)
			E = str(plancksConstant * frequency)
			E1 = E[:5]
			E2 = E[len(E)-3:]
			E3 = "E = "+E1+" x 10^"+E2
			print(E3)

	elif " x 10^" in wavelength:
		wavelength = ec.standardFormUserToInt(wavelength)
		E = str(plancksConstant * speedOfLight / wavelength * (10 ** 9))
		E1 = E[:5]
		E2 = E[len(E)-3:]
		E3 = "E = "+E1+" x 10^"+E2
		print(E3)

	else:
		wavelength = float(wavelength)
		E = str(plancksConstant * speedOfLight / wavelength  * (10 ** 9))
		E1 = E[:5]
		E2 = E[len(E)-3:]
		E3 = "E = "+E1+" x 10^"+E2
		print(E3)

def returnToMenu():

	print("\n{:=^70}".format("Return To Menu?"))
	menuReturn = input("\nWould you like to go back to menu? (y/n)\n")
	if menuReturn == "y":
		print("\nReturning to main menu...")
		runMenu()
	elif menuReturn == "n":
		print("\nThank you for using Equation Buddy!")
	else:
		print("\nInvalid answer given. Closing program.")
		print("\nThank you for using Equation Buddy!")

def runMenu():
	print("{:=^70}".format("Equation Buddy"))
	print("1. Maths")
	print("2. Physics")
	print("3. Exit")
	
	option = int(input("Enter an option"))
	
	if option == 1:
		mathsMenu()
	elif option == 2:
		physicsMenu()
	elif option == 3:
		exit()
	else:
		print("Please select a valid option")
	
def mathsMenu():
	print("{:=^70}".format("Maths Functions"))
	print("1. Suvat Solver")
	print("2. Quadratic Solver")
	print("3. Area Solver")
	print("4. Pascals Line")
	print("5. Main Menu")
	print("5. Exit")	
	
	mathOption = int(input("Enter an option"))
	
	if mathOption == 1:
		s = input("S = ")
		u = input("U = ")
		v = input("V = ")
		a = input("A = ")
		t = input("T = ")
		rounding = input("Rounding T/F")
		if rounding.lower()== "t":
			rounding = True
		else:
			rounding = False 
		print(suvat(s,u,v,a,t,rounding))
		returnToMenu()
	elif mathOption == 2:
		coA = input("Co Efficient A = ")
		coB = input("Co Efficient B = ")
		coC = input("Co Efficient C = ")
		rounding = input("Rounding T/F")
		if rounding.lower()== "t":
			rounding = True
		else:
			rounding = False
		print(quadraticFormula(coA, coB, coC, rounding))
		returnToMenu()
	elif mathOption == 3:
		areaMenu()
		returnToMenu()
	elif mathOption == 5:
		runMenu()
	elif mathOption == 4:
		n = int(input("n = "))
		print(pascalsLine(n))
		returnToMenu()
	elif mathOption == 6:
		exit()
	else:
		print("Please select a valid option")
		
def physicsMenu():
	print("{:=^70}".format("Physics Functions"))
	print("1. Physics Values")
	print("2. Photon Energy")
	print("3. Main Menu")
	print("4. Exit")
	
	physicsOption = int(input("Enter an Option"))
	
	if physicsOption == 1:
		physicsValues()
		returnToMenu()
	elif physicsOption == 2:
		photonEnergy()
		returnToMenu()
	elif physicsOption == 3:
		runMenu()
	elif physicsOption == 4:
		exit()
	else:
		print("Please select a valid option")
  
def get_value():
    
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

def calculate_square_area(side):
    area = side**2
    return area

def calculate_triangle_area(base, height):

    area = base * height/2
    return area

def calculate_elipse_area(a,b):

    area = a*b*pi
    return area

def calculate_circle_area(radius, pi):

    area = radius**2*pi
    return area

def calculate_trapezium_area(base, top, height):

    area = ((base + top)/2)*height
    return area

def calculate_parallelogram_area(base,height):

    area = base * height
    return area

def square():
    
    print("enter side of square")
    side = get_value()
    area = calculate_square_area(side)
    print("the area of the square is", area)

def elipse():
    
    print("enter radius 1 of your elipse")
    a = get_value()
    print("enter radius 2 of your elipse")
    b = get_value()
    area = calculate_elipse_area(a,b)
    print("The area of your elipse is", area)

def circle():
    
    print("enter the radius of the circle")
    radius = get_value()
    area = calculate_circle_area(radius, pi)
    print("the area of your circle is", area)

def triangle():

    print ("enter the base of your triangle")
    base = get_value()
    print("enter the height of your triangle")
    height = get_value()
    area = calculate_triangle_area(base, height)
    print ("the area of your triangle is", area)

def trapezium():

    print ("Enter side A of your trapezium")
    base = get_value()
    print("Enter side B of your trapezium")
    top = get_value()
    print("Enter the height of your trapezium")
    height = get_value()
    area = calculate_trapezium_area(base, top, height)
    print ("the area of your trapezium", area)

def parallelogram():
    print ("Enter the base of your parallelogram")
    base = get_value()
    print ("Enter the height of your parallelogram")
    height = get_value()
    area = calculate_parallelogram_area(base,height)
    print ("The area of your parallelogram is", area) 

def areaMenu():

    end_programme = False
    
    while end_programme == False:
        print ("{:=^70}".format("Pick A Shape"))
        print ("1. Area of Square")
        print ("2. Area of Triangle")
        print ("3. Area of Circle")
        print ("4. Area of Trapezium")
        print ("5. Area of Parallelogram")
        print ("6. Area of an Elipse")
        print ("7. Return to Original Menu")
        choice = input()
        
        while choice not in ["1", "2", "3", "4","5","6","7"]:
            print ("You must choose 1,2,3,4,5,6 or 7")
            print("please reselect number")
            choice = input()
        if choice == "1":
            square()
        elif choice =="2":
            triangle()
        elif choice =="3":
            circle()
        elif choice =="4":
            trapezium()
        elif choice =="5":
            parallelogram()
        elif choice =="6":
            elipse()
        elif choice =="7":
            end_programme = True
            
    print ("Returning to the First Menu, thank you")

def exit():
    print("Thanks for using Equation Buddy, Goodbye!")

if __name__ == "__main__":    
	runMenu()

