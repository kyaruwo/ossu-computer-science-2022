#top
print("Gross Pay calculator")

#user prompt
shrs = input("Enter Hours: ")
srph = input("Enter Rates: ")

#conversion str to float
fh = float(shrs)
fr = float(srph)

#conditions
if fh > 40:
    gpreg = fr * fh
    gpovt = (fh - 40.0) * (fr * 0.5)
    gp = gpreg + gpovt
    print(gp)
else:
    gp = fr * fh
    print(gp)