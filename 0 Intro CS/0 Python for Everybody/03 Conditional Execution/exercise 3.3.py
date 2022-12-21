scorestr = input("Enter Score: ")

try:
    scoref = float(scorestr)
except:
    print("error, invalid input")
    quit()

if scoref > 1.0 or scoref < 0.0:
    print("error, grade is out of range")
elif scoref >= 0.9:
    print("A")
elif scoref >= 0.8:
    print("B")
elif scoref >= 0.7:
    print("C")
elif scoref >= 0.6:
    print("D")
elif scoref < 0.6:
    print("F")