fname = input('Enter the name of the File:')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fhand = open(fname)
count = 0
countday = dict()
for line in fhand:
    line = line.strip()
    #print(line)
    if line.startswith('From '):
        sline = line.split()
        #print(sline)
        email = sline[1:3]
        date = email[1]
        date = date.split() #This line is very important... because if I didn't add it, the for and in bellow was
                            #Counting in letter and not in words, so before start the looping
                            #I had to split the variable date in words.

        #print("BEFORE THE DICTIONARY LOOP: ", date)
        for weekday in date:
            countday[weekday] = countday.get(weekday, 0) + 1
        print(countday)
