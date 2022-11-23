import math

def isFloat(num):
		try:
			float(num)
			return True
		except ValueError:
			return False

def suvat():

	def errorChecker(num, solvingFor):
		try:
			float(num)
			return print(solvingFor, "=", num)
		except:
			return print("This scenario is impossible")
	
	print("{:=^70}".format("Suvat Solver"))
	print()
	s = input("s (if unknown put '?') = ")
	if s != "?":
		s = float(s)
	u = input("u (if unknown put '?') = ")
	if u != "?":
		u = float(u)
	v = input("v (if unknown put '?') = ")
	if v != "?":
		v = float(v)
	a = input("a (if unknown put '?') = ")
	if a != "?":
		a = float(a)
	t = input("t (if unknown put '?') = ")
	if t != "?":
		t = float(t)
	print()
	answer = ""
	
	if isFloat(t) == True and t < 0:
		print("Time can not be negative")
		
	elif isFloat(v) == True and isFloat(u) == True and isFloat(a) == True and v < u and a > 0:
		print("This scenario is not possible")
		
	elif isFloat(v) == True and isFloat(u) == True and isFloat(a) == True and v > u and a < 0:
		print("This scenario is not possible")
		
	elif a == 0 and v != u:
		print("This scenario is not possible") 
		
	elif v == u and a!= 0:
		print("This scenario is not possible")
		
	
	if u == "?" and v != "?" and a != "?" and t != "?":
		answer = a * t
		answer = v - answer
		errorChecker(answer, "u")
	
	if v == "?" and u != "?" and a != "?" and t != "?":
		answer = a * t
		answer = answer + u
		errorChecker(answer, "v")
		
	if a == "?" and v != "?" and u != "?" and t != "?":
		answer = v - u 
		if t == 0:
			print("Time can not be equal to 0 in this scenario")
			
		answer = answer / t 
		errorChecker(answer, "a")
	
	if t == "?" and v != "?" and u !="?" and a != "?":
		answer = v - u 
		if a == 0:
			print("Acceleration can not be equal to 0 in this scenario")
			
		answer = answer / a 
		errorChecker(answer, "t")
		
	if s == "?" and v != "?" and t != "?" and a != "?":
		answer = v * t 
		answer = answer - (0.5 * a * (t*t))
		errorChecker(answer, "s")
		
	if v == "?" and s != "?" and a != "?" and t != "?":
		answer = a * (t*t)
		answer = s + answer
		if t == 0:
			print("Time can not be equal to 0 in this scenario")
		answer = answer / (t * 2)
		errorChecker(answer, "v")
			
	if a == "?" and v != "?" and t != "?" and s != "?":
		answer = v * t 
		answer = answer - s 
		answer = answer * 2 
		if t == 0:
			print("Time can not be equal to 0 in this scenario")
			
		answer = answer / (t * t)
		errorChecker(answer, "a")
		
	if t == "?" and v != "?" and a != "?" and s != "?":
		answer = v * v 
		answer = answer - (2 * a * s)
		answer = answer ** (1/2)
		answer = v - answer
		if a == 0:
			print("Acceleration can not be equal to 0 in this scenario")
			
		answer = answer / a  
		errorChecker(answer, "t")
		
	if s == "?" and u != "?" and t != "?" and a != "?":
		answer = t * t
		answer = answer * a * 0.5 
		answer = (u * t) + answer
		errorChecker(answer, "s")
		
	if u == "?" and s != "?" and a != "?" and t != "?":
		answer = t * t 
		answer = answer * a 
		answer = s - answer
		if t == 0:
			print("Time can not be equal to 0 in this scenario")
			
		answer = answer / (2 * t)
		errorChecker(answer, "u")
		
	if a == "?" and s != "?" and u != "?" and t != "?":
		answer = u * t
		answer = s - answer
		answer = 2 * answer
		if t == 0:
			print("Time can not be equal to 0 in this scenario")
			
		answer = answer / (t * t)
		errorChecker(answer, "a")
	
	if t == "?" and a != "?" and s != "?" and u != "?":
		answer = u * u 
		answer = (2 * a * s) + answer
		answer = answer - u
		if a == 0:
			print("Acceleration can not be equal to 0 in this scenario")
			
		answer = answer / a
		errorChecker(answer, "t")
		
	if s == "?" and t != "?" and u != "?" and v != "?":
		answer = t / 2
		answer = answer * (u + v)
		errorChecker(answer, "s")
		
	if u == "?" and s != "?" and t != "?" and v != "?":
		answer = 2 * s
		if t == 0:
			print("Time can not be equal to 0 in this scenario")
			
		answer = answer / t
		answer = answer + v
		errorChecker(answer, "u")
		
	if v == "?" and s != "?" and t != "?" and u != "?":
		answer = 2 * s 
		if t == 0:
			print("Time can not be equal to 0 in this scenario")
			
		answer = answer / t
		answer = answer - u 
		errorChecker(answer, "v")
	
	if t == "?" and s != "?" and u != "?" and v != "?":
		answer = 2 * s
		answer = answer / (u + v)
		errorChecker(answer, "t")
		
	if s == "?" and u != "?" and v != "?" and a != "?":
		answer = (u * u) + (v * v)
		answer2 = (2 * a)
		if answer2 == 0:
			print("Acceleration can not be equal to 0 in this scenario")
		answer = answer / answer2
		errorChecker(answer, "s")
		
	if u == "?" and a != "?" and s != "?" and v != "?":
		answer = (2 * a * s) - (v * v)
		answer = answer ** (1/2)
		errorChecker(answer, "u")
		
	if v == "?" and u != "?" and a != "?" and s != "?":
		answer = (u * u) + (2 + a + s)
		answer = answer ** (1/2)
		errorChecker(answer, "v")
		
	if a == "?" and v != "?" and u != "?" and s != "?":
		answer = (v * v) - (u * u)
		if s == 0:
			print("Displacement can not be equal to 0 in this scenario")
		answer = answer / (2 * s)
		errorChecker(answer, "a")
			
def QuadraticFormula():
	
	def QuadraticErrorChecker(X1, X2):
		imaginaryCounter = 0
		if isinstance(X1, complex):
			print("The first value is an imaginary number")
			imaginaryCounter = imaginaryCounter + 1
		else:
			print("x =", X1)
			
		if isinstance(X2, complex):
			print("The second value is an imaginary number")
			imaginaryCounter = imaginaryCounter + 1
		elif X1 == X2:
			print("This equation has 1 real root")
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
	
	print()
	print("{:=^70}".format("MAIN MENU"))
	print()
	print("1. Suvat Solver")
	print("2. Quadratic Formula")
	print("3. Physics Values")
	print("4. Exit")
	print()
	print("======================================================================")
	print()
	option = int(input("Select a menu option:\n"))
	print()
	
	if option	== 1:
		suvat()
		returnToMenu()

	elif option == 2:
		QuadraticFormula()
		returnToMenu()

	elif option == 3:
		physicsValues()
		returnToMenu()

	elif option == 4:
		print("\nThank you for using Equation Buddy!")

runMenu()