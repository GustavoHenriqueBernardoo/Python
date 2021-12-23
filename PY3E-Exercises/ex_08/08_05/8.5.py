fname = input('Enter the name of the file:')
fhand = open('mbox-short.txt')
count = 0

try:
    fhand = open(fname)
except:
    print('This files does not exist:', fname)
    exit()
for line in fhand:
    line = line.rstrip()
    if not 'From:' in line:
        continue
    if len(line) < 60:
        count = count +1
        rl = line.split()
        se = rl[1]
        #rl = line.strip('From: ')
        #email = rl[0:30]
        #email = email.split()
        #se = email[:1] [0] # se = split email
        print(se)


#ic = int(count) # ic = integer count
#total = ic / 2
print('There were', count, 'lines in the file with From as the first word')
