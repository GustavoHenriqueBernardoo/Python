import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split() # first we have to decode the url page to unicode or string, that way we can aplly evertything we learn so far
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

#fhand = urllib.request.urlopen('https://docs.google.com/document/d/1rC448GZ1DDe-7bbEDoyFGQIOs4kSwaDL/edit')
#for line in fhand:
#    print(line.decode().strip())
