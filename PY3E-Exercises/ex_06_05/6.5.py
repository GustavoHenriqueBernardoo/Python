str = 'X-DSPAM-Confidence:0.8475'
lower = str.lower()

print (lower)
print (str[:19])
#info = 0
#while info < len(str):
    #letter = str[info]
    #print (info, letter)
    #info = info + 1
pos = str.find('0.8475')
print (pos)
numpos = str[pos:]
print (numpos)
floatnum = float(numpos)
print (floatnum)

#letter = str.strip()
#print (letter)

# worked exercise by Charles
str = 'X-DSPAM-Confidence:0.8475'
ipos = str.find(':') #this line basically search for the ':' and hold the value where the ':' are in the varialbe 'ipos'
piece = str[ipos+2:] # Piece hold the information of 'ipos' from there and beyond. The +2 means, two letter ahead of 'ipos'
value = float(piece)
print(value)
