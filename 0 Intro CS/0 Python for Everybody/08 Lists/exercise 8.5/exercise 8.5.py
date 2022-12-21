while True:
    fname = input("Enter file name: ")
    try:
        fbody = open(fname)
    except:
        print("Cannot find filename,", fname)
        continue
    break

count = 0
for line in fbody:
    if line.startswith("From "):
        splitline = line.split()
        if len(splitline) < 2:
            continue
        else:
            #print the email address and count them
            print(splitline[1])
            count += 1

print("There were", count, "lines in the file with From as the first word")