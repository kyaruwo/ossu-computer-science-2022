text = "X-DSPAM-Confidence:    0.8475"

#collon find
collonpos = text.find(":")
#trimming
numstr = text[collonpos + 1:]
#removing spaces from left
stripnum = numstr.lstrip()
#converting str to float
numint = float(stripnum)
#output
print(numint)