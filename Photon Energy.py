print("Calculating energy of photons using h,f,c and wavelength")
speedOfLight = 3*10**8
plancksConstant = 6.63*10**-34
# starting with E = hc / wavelength
wavelength = input("wavelength = ")
wavelength = float(wavelength)
E = plancksConstant * speedOfLight / wavelength
E = str(E)

E1 = E[:5]
E2 = E[len(E)-3:]

#newE = "E = ",E[:5]+" * 10"+E[len(E)-3:]

E3 = "E = "+E1+"*10"+E2
print(E3)
