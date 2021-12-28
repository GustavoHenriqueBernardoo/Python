#Exercise 2: This program counts the distribution of the hour of the day for each of the messages.
#You can pull the hour from the "From" line by finding the time string and then splitting that string into
#parts using the colon character. Once you have accumulated the counts for each hour, print out the counts,
#one per line, sorted by hour as shown below.
fname = input('Enter file name:')
if len(fname) < 1 : fname = 'mbox-short.txt'
fhand = open(fname)
count = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        sline = line.split()
        hours = sline [5]
        shours = hours.split(':')
        fhours = shours[0]
        fh = fhours.split()
        #print(fh)
        for hour in fh:
            count[hour] = count.get(hour, 0) + 1
#print(count.items())
lst = list()
for key, val in sorted(count.items()) :
    print(key, val)
