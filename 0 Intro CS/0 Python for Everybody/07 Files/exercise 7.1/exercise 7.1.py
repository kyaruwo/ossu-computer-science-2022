#input state
while True:
    filehandle = input("Enter a file name: ")
    #exit
    if filehandle == "quit":
        quit()
    #filename checker
    try:
        filebody = open(filehandle)
    except:
        print("Filename cannot be found,", filehandle)
        continue
    break
#filebody print loop
for i in filebody:
    #newline strip
    i = i.rstrip()
    #text line uppercase and print
    print(i.upper())

    #please self never forget () after each method in a string variable variable, i.e i.strip() and i.upper()