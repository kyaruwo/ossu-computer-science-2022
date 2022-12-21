while True:
    filehandle = input("Enter filename: ")

    if filehandle == "quit":
        quit()
    else:
        try:
            filebody = open(filehandle)
        except:
            print("Cannot find filename,", filehandle)
            continue
    break

for line in filebody:
    splitline = line.split()
    if len(splitline) < 1:
        continue
    elif splitline[0] == "From":
        print(splitline[2])

#filename mbox-short.txt