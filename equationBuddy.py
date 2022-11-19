import math

def isFloat(num):
		try:
			float(num)
			return True
		except ValueError:
			return False

def suvat():	

	Running = True 
	
	def errorChecker(num, solvingFor):
	    try:
	        float(num)
	        return print(solvingFor, "=", num)
	    except ValueError:
	        return print("This scenario is not possible")
	
	while Running == True:
	
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
		answer = ""
		
		if isFloat(t) == True and t < 0:
			print("Time can not be negative")
			break
		elif v < u and a > 0:
			print("This scenario is not possible")
			break
		elif v > u and a < 0:
			print("This scenario is not possible")
			break
		elif a == 0 and v != u:
			print("This scenario is not possible") 
			break
		elif v == u and a!= 0:
			print("This scenario is not possible")
			break
		
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
				break
			answer = answer / t 
			errorChecker(answer, "a")
		
		if t == "?" and v != "?" and u !="?" and a != "?":
			answer = v - u 
			if a == 0:
				print("Acceleration can not be equal to 0 in this scenario")
				break
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
				break
			answer = answer / (t * t)
			errorChecker(answer, "a")
			
		if t == "?" and v != "?" and a != "?" and s != "?":
			answer = v * v 
			answer = answer - (2 * a * s)
			answer = answer ** (1/2)
			answer = v - answer
			if a == 0:
				print("Acceleration can not be equal to 0 in this scenario")
				break
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
				break
			answer = answer / (2 * t)
			errorChecker(answer, "u")
			
		if a == "?" and s != "?" and u != "?" and t != "?":
			answer = u * t
			answer = s - answer
			answer = 2 * answer
			if t == 0:
				print("Time can not be equal to 0 in this scenario")
				break
			answer = answer / (t * t)
			errorChecker(answer, "a")
		
		if t == "?" and a != "?" and s != "?" and u != "?":
			answer = u * u 
			answer = (2 * a * s) + answer
			answer = answer - u
			if a == 0:
				print("Acceleration can not be equal to 0 in this scenario")
				break
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
				break
			answer = answer / t
			answer = answer + v
			errorChecker(answer, "u")
			
		if v == "?" and s != "?" and t != "?" and u != "?":
			answer = 2 * s 
			if t == 0:
				print("Time can not be equal to 0 in this scenario")
				break
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
				break
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
		else:
			print("x =", X2)
			
		if imaginaryCounter == 2:
			print("This equation has no real roots")
		
	coA = float(input("Coefficient A = "))
	coB = float(input("Coefficient B = "))
	coC = float(input("Coefficeint C = "))
	
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
	
	print("Speed Of Light =" ,3.00 * 10**8, "M/s")
	print("Electron Charge =",1.60 * 10**-19,"coulomb")
	print("Plancks Constant =",6.63 * 10**-34,"J/s")
	print("Electron Mass =", 9.11 * 10**-31,"kg")
	print("Proton Mass =", 1.67 * 10**-27,"kg")
	print("Neutron Mass =", 1.67 * 10**-27,"kg")
	print("Gravity = 9.81 N/kg")
							
menu = True
	
while menu == True:
	
	print("==============================MAIN MENU===============================")
	print("1. Suvat Solver")
	print("2. Quadratic Formula")
	print("3. Physics Values")
	print("4. Exit")
	option = int(input("Select a menu option"))
	
	if option	== 1:
		suvat()
	elif option == 2:
		QuadraticFormula()
	elif option == 3:
		physicsValues()
	elif option == 4:
		menu = False

			
			
		

