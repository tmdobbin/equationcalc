import equationCalcModules
c = 3*10**8 # a constant to represent the speed of light
wavelength = equationcalcmodules.inputInt("wavelength(if unknown put '?') = ")

if wavelength != "?":
    wavelength = float(wavelength)
    frequency = c / wavelength
    print(f"{frequency=}hz")

else:
    frequency = float(input("frequency = "))
    wavelength = c / frequency
    print(f"{wavelength=}m")
    