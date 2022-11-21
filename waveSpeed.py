c = 3*10**8 # a constant to represent the speed of light

if __name__ == "__main__":
    import ecFunctions
    wavelength = input("wavelength(if unknown put '?') = ")

    if wavelength != "?":
        wavelength = float(wavelength)
        frequency = round((c / wavelength), 3)
        print(f"{frequency=}hz (3dp)")

    else:
        frequency = float(ecFunctions.inputInt("frequency = "))
        wavelength = round((c / frequency), 3)
        print(f"{wavelength=}m (3dp)")

else:
    def wavespeedCalc(frequency=None, wavelength=None):
        if wavelength is None:
            frequency = float(frequency)
            wavelength = round((c / frequency), 3)
            return wavelength
        
        if wavelength is not None:
            wavelength = float(wavelength)
            frequency = round((c / wavelength), 3)
            return frequency