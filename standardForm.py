def standardForm(answer):
    string = str(answer)
    round1 = str(round(float(string[:6]), 3))
    round2 = string[len(string)-3:]
    print("E =", round1, "x 10^" + round2)

standardForm()