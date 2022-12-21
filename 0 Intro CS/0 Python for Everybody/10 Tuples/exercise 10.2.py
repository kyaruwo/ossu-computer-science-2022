# a loop that ask the user for the filename
while True:
    filename = input("Enter file:")
    try:
        filebody = open(filename)
        break
    except:
        filename = "mbox-short.txt"
        filebody = open(filename)
        break
        #the 3 lines code above can be change into the 2 lines of code bellow and continuely ask the user for the correct filename
        #print("cannot find,",filename)
        #continue
        #too lazy to write the filename :<

#making a dictionary that counts the frequency of the hour the email was sent
hour_counts = dict()
#loop through every line in the file
for line in filebody:
    #check if the line starts with "From "
    if line.startswith("From "):
        #split the line of words by " " or spaces
        split_line = line.split()
        #get the line of word that represent the time
        time = split_line[5]
        #split the time by ":"
        time = time.split(":")
        #get the hour
        hour = time[0]
        #check if the hour is in or not in the dictionary and count the hour frequency
        if hour in hour_counts:
            hour_counts[hour] += 1
        else:
            hour_counts[hour] = 1
        #the 4 lines of code above can also be;
        #hour_counts[hour] = hour_counts.get(hour, 0) + 1
    else:
        continue

#sorting the dictionary and printing its keys and values
sorted_hour_counts = list()
#a loop through the keys and values of the dictionary and append them to a list
for (hr, count) in hour_counts.items():
    sorted_hour_counts.append((hr, count))
#sort the list
sorted_hour_counts.sort()
#print the list
for (hr, count) in sorted_hour_counts:
    print(hr, count)