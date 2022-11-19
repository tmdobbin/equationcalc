import ecFunctions
c = 3*10**8 # a constant to represent the speed of light
wavelength = ecFunctions.inputInt("wavelength(if unknown put '?') = ")

if wavelength != "?":
    wavelength = float(wavelength)
    frequency = round((c / wavelength), 3)
    print(f"{frequency=}hz (3dp)")

else:
    frequency = float(ecFunctions.inputInt("frequency = "))
    wavelength = round((c / frequency), 3)
    print(f"{wavelength=}m (3dp)")
    