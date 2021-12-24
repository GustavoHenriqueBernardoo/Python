
fname = input('Enter the name of the file: ') # fn = file name
fhand = open ('mbox-short.txt') # fhand = file hand
ea = ('na na boo boo') # message for easter egg
if fname == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punkd!')
    exit()
try:
    fhand = open(fname)


except:
    print(' The file does not exist:', fname)
    exit()

total = 0
count = 0
for line in fhand:
    line = line.rstrip()
    if not 'X-DSPAM-Confidence:' in line:
        continue
    count = count + 1
    removestring = line.lstrip('X-DSPAM-Confidence: ') #this is my way!!!!!!!
    num = float(removestring)
    total = total + num
    tcl = total/count

print('Average spam confidence:',tcl)

    #print (removestring)
    #slice = removestring.split(",")
    #fn = float(removestring)

    #if fn.startswith('0'):
    #    count = count + 1
    #    print(count, fn)

    #if line.startswith('X-DSPAM-Confidence:'):
        #print(line)
        #pos = line.find('0.8475')
        #print(pos)
        #npos = line[pos:]
        #print(npos)
        #fpos = float(npos)
        #print(fpos)
