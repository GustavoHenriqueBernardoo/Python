# On this program we want to print just the third word in the line witch is the day of the week,
#like: saturday, monday and so on

han = open('mbox-short.txt')

for line in han:
    line = line.rstrip() # RSTRIP CHOP THE TXT IN LINES
    #print('Line:', line)
    wds = line.split() # SPLIT CHOP THE TXT INTO THE WORDS
    #print('Words:', wds)
    # the line bellow is the "Guardian"
    if len(wds) < 3: # what this line means = if we don't have any words here, we will skip it.
    #having no words means = blank lines
    # another guardian code wich works as well is:(If line == '' :)in the line bellow = (continue) without parenteses ofc
        continue
    if wds [0] != 'From' : #where the traceback happen...
        #print('Ignore:')
        continue
    print(wds[2])



# after all the debugging, correct code
#for line in han:
    #line = line.rstrip() # RSTRIP CHOP THE TXT IN LINES
    #wds = line.split() # SPLIT CHOP THE TXT INTO THE WORDS
    #if len(wds) < 3 or wds[0] != 'From' :
        #continue
    #print(wds[2])
