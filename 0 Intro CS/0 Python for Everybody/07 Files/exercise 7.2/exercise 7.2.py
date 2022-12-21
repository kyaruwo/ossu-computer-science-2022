#filename input checker loop
while True:
    #filename input
    filehandle = input("Enter file name: ")
    #quit
    if filehandle == "quit":
        quit()
    #checker
    try:
        #file convert from handle to string
        filebody = open(filehandle)
    except:
        #error message
        print("Cannot find filename,", filehandle)
        continue
    break

#declaration
total = 0
count = 0
#filebody line loop finder
for line in filebody:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        #extract number
        numstr = line[19:]
        numfloat = float(numstr)
        #summation numfloat
        total += numfloat
        #count tracker
        count = count + 1

#computation
average = total / count

#output
print("Average spam confidence:", average)