import tkinter as tk
c = 3*10**8 # Speed of Light
root = tk.Tk()
root.title("Wavespeed Calculator")
root.geometry("750x250")

root.grid_columnconfigure((0,1), weight=1)

def calculate():
    frequency = freqInput.get()
    wavelength = wavelengthInput.get()

    if wavelength == "":
        frequency = float(frequency)
        result.configure(text=f"{round((c / frequency), 3)}m (3dp)")
    
    if wavelength != "":
        wavelength = float(wavelength)
        result.configure(text=f"{round((c / wavelength), 3)}hz (3dp)")


freqLabel = tk.Label(root, text="Frequency (hz): ")
wavelengthLabel = tk.Label(root, text="Wavelength (m): ")
result = tk.Label(root, text="Placeholder result text")
calcButton = tk.Button(root, text="Enter", width = 20, command = calculate)

freqInput = tk.Entry(root)
wavelengthInput = tk.Entry(root)
freqInput.insert(0, "")
wavelengthInput.insert(0, "")

result.grid(row = 0, columnspan = 2)
freqLabel.grid(row = 1, column = 0)
freqInput.grid(row = 1, column = 1)
wavelengthLabel.grid(row = 2, column = 0)
wavelengthInput.grid(row = 2, column = 1)
calcButton.grid(row = 3, columnspan = 2)

root.mainloop()