#Exercise 1: Revise a previous program as follows: Read and parse the "From" lines and pull out the addresses
#from the line. Count the number of messages from each person using a dictionary.

#After all the data has been read, print the person with the most commits by creating a list of (count, email)
#tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.
fname = input('Enter file name:')
if len(fname) < 1: fname = 'mbox-short.txt'
fhand = open(fname)
count = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        sline = line.strip()
        wds =  sline.split()
        email = wds[1]
        email = email.split() # we have to split before the count, if we didn't the count bellow will count by words and not the whole email
        for word in email:
            count[word] = count.get(word, 0) + 1

lst = []
bigcount = None
bigsend = None
for key, val in count.items():
    newtup = (val, key)
    lst.append(newtup)
    if bigcount is None or val > bigcount:
        bigcount = val
        bigsend = key
#lst = sorted(lst, reverse=True)
print(bigsend, bigcount)
