#main loop, asking the file name
while True:
    filehandle = input("Enter file name: ")
    try:
        filebody = open(filehandle)
    except:
        print("Cannot find filename,", filehandle)
        continue
    break

#declaring the arrays
unsortedlist = list()
filteredlist = list()

#add words to a array
for line in filebody:
    linesplit = line.split()
    unsortedlist += linesplit

#filter loop
for i in unsortedlist:
    #filter argument
    if i in filteredlist:
        continue
    else:
        #add word to the filtered array
        filteredlist.append(i)

#sorting
filteredlist.sort()

#output
print(filteredlist)