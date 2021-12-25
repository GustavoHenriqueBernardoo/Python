fname = input('Enter the name of the File:')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fhand = open(fname)
count = 0
for line in fhand:
    line = line.strip()
    #print(line)
    if line.startswith('From:'):
        sline = line.strip()
        print(sline)
