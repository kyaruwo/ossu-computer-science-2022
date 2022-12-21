#declaration
largest = None
smallest = None

#main loop
while True:
    numstr = input("Enter a number: ")

    #done checker
    if numstr == "done":
        break
    else:
        #input checker
        try:
            numint = int(numstr)
        except:
            print("Invalid input")
            continue

    #largest and smallest setter
    if largest == None and smallest == None:
        largest = numint
        smallest = numint

    #largest tracker
    if numint > largest:
        largest = numint
    #smallest tracker
    elif numint < smallest:
        smallest = numint

#output
print("Maximum is", largest)
print("Minimum is", smallest)