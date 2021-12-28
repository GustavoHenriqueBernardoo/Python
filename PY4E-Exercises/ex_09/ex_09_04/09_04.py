# Exercise 4: Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created, look through the dictionary using a
# maximum loop (see Section [maximumloop]) to find who has the most messages and print how many messages the person has.
fname = input('Enter the name of the file :')
if len(fname) < 1 : fname = 'mbox-short.txt'
fhand = open(fname)
mailbox = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        sline = line.split()
        email = sline[1]
        email = email.split()
        for address in email:
            mailbox[address] = mailbox.get(address, 0) + 1

bigcount = None
bigword = None
for word,count in mailbox.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print(bigword, bigcount)
