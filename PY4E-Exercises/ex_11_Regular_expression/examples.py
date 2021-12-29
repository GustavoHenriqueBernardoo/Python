# Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter
# a regular expression and count the number of lines that matched the regular expression:

# Search for lines that contain 'From'
import re
hand = open ('mbox-short.txt')
#for line in hand:
#    line = line.rstrip()
#    if re.search('^F..m:', line):
#        print(line)

# Search for lines that have an at sign between characters
#for line in hand:
    #line = line.rstrip()
    #x = re.findall('\S+@\S+', line)
    #if len(x) > 0:
        #print(x)

# Search for lines that have an at sign between characters
# The characters must be a letter or number
for line in hand :
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
    if len(x) > 0:
        print(x)
