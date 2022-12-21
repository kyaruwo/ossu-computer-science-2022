#gross pay computation
def computepay(hour, rate):
    #conditions
    if hourf > 40:
        #gross pay over time computation
        pay = (hour - 40.0) * (rate * 0.5)
        pay = hour * rate + pay
    else:
        #gross pay regular computation
        pay = hour * rate
    return pay


#top
print("Gross Pay calculator")

#user prompt
hourstr = input("Enter Hours: ")
ratestr = input("Enter Rates: ")

#checker
try:
    #conversion str to float
    hourf = float(hourstr)
    ratef = float(ratestr)
except:
    print("Error, please enter numeric input")
    quit()

gp = computepay(hourf, ratef)

print("Gross Pay:", gp)