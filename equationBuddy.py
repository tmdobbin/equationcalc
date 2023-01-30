# ver 0.1

import math
import ecFunctions as ec
pi = math.pi

def isFloat(num):
	try:
		float(num)
		return True
	except ValueError:
		return False

def suvat(s, u, v, a, t):

	finalresult = ""

	def errorChecker(num, solvingFor):
		try:
			float(num)
			num = round(num, 3)
			return f"{solvingFor} = {num}"
		except:
			return ("This scenario is impossible")
	
	# print("{:=^70}".format("Suvat Solver"))
	# print()
	# s = input("s (if unknown put '') = ")
	if s != "":
		s = float(s)
	# u = input("u (if unknown put '') = ")
	if u != "":
		u = float(u)
	# v = input("v (if unknown put '') = ")
	if v != "":
		v = float(v)
	# a = input("a (if unknown put '') = ")
	if a != "":
		a = float(a)
	# t = input("t (if unknown put '') = ")
	if t != "":
		t = float(t)
	# print()
	answer = ""
	
	if isFloat(t) == True and t < 0:
		return ("Time can not be negative")
		
	elif isFloat(v) == True and isFloat(u) == True and isFloat(a) == True and v < u and a > 0:
		return ("This scenario is not possible")
		
	elif isFloat(v) == True and isFloat(u) == True and isFloat(a) == True and v > u and a < 0:
		return ("This scenario is not possible")
		
	elif a == 0 and v != u:
		return ("This scenario is not possible") 
		
	elif v == u and a!= 0:
		return ("This scenario is not possible")
		
	
	if u == "" and v != "" and a != "" and t != "":
		answer = a * t
		answer = v - answer
		finalresult = finalresult + (errorChecker(answer, "u"))
	
	if v == "" and u != "" and a != "" and t != "":
		answer = a * t
		answer = answer + u
		finalresult = finalresult + (errorChecker(answer, "v"))
		
	if a == "" and v != "" and u != "" and t != "":
		answer = v - u 
		if t == 0:
			finalresult = finalresult + ("Time can not be equal to 0 in this scenario")
			
		answer = answer / t 
		errorChecker(answer, "a")
	
	if t == "" and v != "" and u !="" and a != "":
		answer = v - u 
		if a == 0:
			finalresult = finalresult +  ("Acceleration can not be equal to 0 in this scenario")
			
		answer = answer / a 
		errorChecker(answer, "t")
		
	if s == "" and v != "" and t != "" and a != "":
		answer = v * t 
		answer = answer - (0.5 * a * (t*t))
		finalresult = finalresult +  (errorChecker(answer, "s"))
		
	if v == "" and s != "" and a != "" and t != "":
		answer = a * (t*t)
		answer = s + answer
		if t == 0:
			finalresult = finalresult +  ("Time can not be equal to 0 in this scenario")
		answer = answer / (t * 2)
		finalresult = finalresult +  (errorChecker(answer, "v"))
			
	if a == "" and v != "" and t != "" and s != "":
		answer = v * t 
		answer = answer - s 
		answer = answer * 2 
		if t == 0:
			finalresult = finalresult +  ("Time can not be equal to 0 in this scenario")
			
		answer = answer / (t * t)
		finalresult = finalresult +  (errorChecker(answer, "a"))
		
	if t == "" and v != "" and a != "" and s != "":
		answer = v * v 
		answer = answer - (2 * a * s)
		answer = answer ** (1/2)
		answer = v - answer
		if a == 0:
			finalresult = finalresult +  ("Acceleration can not be equal to 0 in this scenario")

		answer = answer / a  
		finalresult = finalresult +  (errorChecker(answer, "t"))
		
	if s == "" and u != "" and t != "" and a != "":
		answer = t * t
		answer = answer * a * 0.5 
		answer = (u * t) + answer
		finalresult = finalresult +  (errorChecker(answer, "s"))
		
	if u == "" and s != "" and a != "" and t != "":
		answer = t * t 
		answer = answer * a 
		answer = s - answer
		if t == 0:
			finalresult = finalresult +  ("Time can not be equal to 0 in this scenario")
			
		answer = answer / (2 * t)
		finalresult = finalresult +  (errorChecker(answer, "u"))
		
	if a == "" and s != "" and u != "" and t != "":
		answer = u * t
		answer = s - answer
		answer = 2 * answer
		if t == 0:
			finalresult = finalresult +  ("Time can not be equal to 0 in this scenario")
			
		answer = answer / (t * t)
		finalresult = finalresult +  (errorChecker(answer, "a"))
	
	if t == "" and a != "" and s != "" and u != "":
		uSq = u * u 
		answer = (2 * a * s)
		answer = answer + uSq
		answer = answer ** (1/2)
		answer = answer - u
		if a == 0:
			finalresult = finalresult +  ("Acceleration can not be equal to 0 in this scenario")
			
		answer = answer / a
		finalresult = finalresult +  (errorChecker(answer, "t"))
		
	if s == "" and t != "" and u != "" and v != "":
		answer = t / 2
		answer = answer * (u + v)
		finalresult = finalresult +  (errorChecker(answer, "s"))
		
	if u == "" and s != "" and t != "" and v != "":
		answer = 2 * s
		if t == 0:
			finalresult = finalresult +  ("Time can not be equal to 0 in this scenario")
			
		answer = answer / t
		answer = answer + v
		finalresult = finalresult +  (errorChecker(answer, "u"))
		
	if v == "" and s != "" and t != "" and u != "":
		answer = 2 * s 
		if t == 0:
			finalresult = finalresult +  ("Time can not be equal to 0 in this scenario")
			
		answer = answer / t
		answer = answer - u 
		finalresult = finalresult +  (errorChecker(answer, "v"))
	
	if t == "" and s != "" and u != "" and v != "":
		answer = 2 * s
		answer = answer / (u + v)
		finalresult = finalresult +  (errorChecker(answer, "t"))
		
	if s == "" and u != "" and v != "" and a != "":
		answer = (u * u) + (v * v)
		answer2 = (2 * a)
		if answer2 == 0:
			finalresult = finalresult +  ("Acceleration can not be equal to 0 in this scenario")
		answer = answer / answer2
		finalresult = finalresult +  (errorChecker(answer, "s"))
		
	if u == "" and a != "" and s != "" and v != "":
		answer = (2 * a * s) - (v * v)
		answer = answer ** (1/2)
		finalresult = finalresult +  (errorChecker(answer, "u"))
		
	if v == "" and u != "" and a != "" and s != "":
		answer = (u * u) + (2 + a + s)
		answer = answer ** (1/2)
		finalresult = finalresult +  (errorChecker(answer, "v"))
		
	if a == "" and v != "" and u != "" and s != "":
		answer = (v * v) - (u * u)
		if s == 0:
			finalresult = finalresult +  ("Displacement can not be equal to 0 in this scenario")
		answer = answer / (2 * s)
		finalresult = finalresult +  (errorChecker(answer, "a"))

	return finalresult

def quadraticFormula():
	
	def QuadraticErrorChecker(X1, X2):
		imaginaryCounter = 0
		if isinstance(X1, complex):
			print("The first value is an imaginary number")
			imaginaryCounter = imaginaryCounter + 1
		elif len(str(X1)) > 4:
			X1 = round(X1, 3)
			print ("x =", X1)
		else:
			print("x =", X1)
			
		if isinstance(X2, complex):
			print("The second value is an imaginary number")
			imaginaryCounter = imaginaryCounter + 1
		elif X1 == X2:
			print("This equation has 1 real root")
		elif len(str(X2)) > 4:
			X2 = round(X2, 3)
			print ("x =", X2)
		else:
			print("x =", X2)
			
		if imaginaryCounter == 2:
			print("This equation has no real roots")

	print("{:=^70}".format("Quadratic Formula"))
	print()
	coA = float(input("Coefficient A = "))
	coB = float(input("Coefficient B = "))
	coC = float(input("Coefficeint C = "))
	print()
	
	if coA == 0:
		print("This function requires a coefficient for A")
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
	QuadraticErrorChecker(answer1, answer2)
	
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
	print("4. Main Menu")
	print("5. Exit")	
	
	mathOption = int(input("Enter an option"))
	
	if mathOption == 1:
		suvat()
		returnToMenu()
	elif mathOption == 2:
		quadraticFormula()
		returnToMenu()
	elif mathOption == 3:
		areaMenu()
		returnToMenu()
	elif mathOption == 4:
		runMenu()
	elif mathOption == 5:
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
