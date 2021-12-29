# Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter
# a regular expression and count the number of lines that matched the regular expression:
import re
fhand = open('regex_sum_1410732.txt')
numlist = list()
for line in fhand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    numlist = numlist + x
sum = 0
for i in numlist:
    sum = sum + int(i)
print(sum)
