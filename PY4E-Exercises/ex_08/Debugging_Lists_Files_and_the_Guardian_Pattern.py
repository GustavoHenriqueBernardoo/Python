han = open('mbox-short.txt')

for line in han:
    line = line.rstrip() # RSTRIP CHOP THE TXT IN LINES
    wds = line.split() # SPLIT CHOP THE TXT INTO THE WORDS
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[2])
