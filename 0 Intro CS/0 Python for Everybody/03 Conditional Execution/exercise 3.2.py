#top
print("Gross Pay calculator")

#user prompt
shrs = input("Enter Hours: ")
srph = input("Enter Rates: ")

#checker
try:
    #conversion str to float
    fh = float(shrs)
    fr = float(srph)
except:
    print("Error, please enter numeric input")
    quit()

#conditions
if fh > 40:
    gpreg = fr * fh
    gpovt = (fh - 40.0) * (fr * 0.5)
    gp = gpreg + gpovt
    print(gp)
else:
    gp = fr * fh
    print(gp)