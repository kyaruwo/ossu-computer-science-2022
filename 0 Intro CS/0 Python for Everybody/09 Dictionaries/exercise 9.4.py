#filename prompt
while True:
    fname = input("Enter filename:")
    try:
        fbody = open(fname)
        break
    except:
        print("file cannot be found,", fname)

#makes a list array can also be, emails = list()
emails = []
#makes a dictionary {(key,value),(key,value)} can also be mail_count = dict()
mail_dict = {}

#loops through the line of text
for line in fbody:
    #looks for the line that startswith "From "
    if line.startswith("From "):
        #splits the line of words and add them to a list and overwrite the old list to a new one
        email = line.split()
        #checks if the second variable in the array "email" is in the "mail_dict" dictionary,
        #if not add the variable and add 1 to its value; else add 1 to the value of the variable in the dictionary
        mail_dict[email[1]] = mail_dict.get(email[1], 0) + 1
        ##"mail_dict[email[1]] = mail_dict.get(email[1], 0) + 1" can also be;
        #if email[1] not in mail_dict:
        #    mail_dict[email[1]] = 1
        #else:
        #    mail_dict[email[1]] = mail_dict[email[1]] + 1
    else:
        continue

#declarations
most_email = None
most_email_count = 0

#compare all keys&values to each other and find the most email sender
for i, j in mail_dict.items():
    #compare the current sender to the current most sender
    if j > most_email_count:
        #set the current most_email to most email
        most_email = i
        #set the current most_email_count to most_email_count
        most_email_count = j

#output the most email sender and its email count
print(most_email, most_email_count)