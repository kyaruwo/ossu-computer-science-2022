#declaration
count = 0
total = 0.0

#main loop
while True:
    numstr = input("Enter a number: ")

    #done checker
    if numstr == "done":
        break
    else:
        #input error check
        try:
            numf = float(numstr)
        except:
            print("Invalid input")
            continue
        #count and total tracker
        count += 1  # or count = count + 1
        total += numf

#average computation
average = total / count

#output
print("Total:", total, "Count:", count, "Average:", average)