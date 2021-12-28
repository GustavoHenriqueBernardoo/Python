# Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead
#of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of
#your dictionary.
fname = input('Enter file name:')
if len(fname) < 1 : fname = 'mbox-short.txt'
fhand = open(fname)
counts = dict()
for line in fhand:
    line = line.rstrip()
    #print(line)
    if line.startswith('From '):
        sline = line.rstrip()
        #print(sline)
        wds = sline.split()
        mail = wds[1]
        smail = mail.split('@') # This line I find the @ in the middle of the address and split it, removing the @
        email = smail[1]
        counts[email] = counts.get(email, 0) + 1
print(counts)
