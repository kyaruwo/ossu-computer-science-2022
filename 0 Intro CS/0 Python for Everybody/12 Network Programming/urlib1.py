import urllib.request, urllib.parse, urllib.error

fhand0 = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand0:
    print(line.decode().strip())

#can be treated like a file
fhand1 = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
counts = dict()
for line in fhand1:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

#reading web pages
fhand2 = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")
for line in fhand2:
    print(line.decode().strip())