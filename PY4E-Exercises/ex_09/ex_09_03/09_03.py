# Write a program to read through a mail log, build a histogram using a dictionary to count
# how many messages have come from each email address, and print the dictionary.
fname = input('Enter the name of the file :')
if len(fname) < 1 : fname = 'mbox-short.txt'
fhand = open(fname)
count = 0
mailbox = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        sline = line.split()
        email = sline[1]
        email = email.split()

        for address in email:
            mailbox[address] = mailbox.get(address, 0) + 1

#print(list(mailbox.keys())) #You can get a list of keys, values, or items (both) from a dictionary
#print(list(mailbox.values())) #You can get a list of keys, values, or items (both) from a dictionary
print(list(mailbox.items())) #You can get a list of keys, values, or items (both) from a dictionary
