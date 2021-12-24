n =  'Gustavo Bernardo'
print (n[6])
print (n[0:6]) #or (n[:6]) or n([8:]) | to print all the name or letter of the variable n (n[:])
print (n[7:30])
#remeber that the number 0 count as well. In the name Gustavo we have 7 letter, but in python count 6 because zero count. So 0 to 6 are 7 letters....
#Space count as well
print('the lengh of Gustavo Bernardo is:',len(n))

question = 'From marquard@uct.ac.za'
print (question [14:17])
print (len(question))
index = 0
while index <len(question):
    letter = question[index]
    print (index ,letter)
    index = index + 1

#loopping through String:
print ('For and In looping')
for letter in n:
    print(letter)

print ('While loop')
index = 0
while index < len(n):
    letter = n[index]
    print (index, letter)
    index = index +1
print ('Another example of For and In')
for letter in 'Ronaldo':
    print(letter)
#Looping and counting
print ('Looping and counting')
count = 0
for letter in n:
    if letter == 'a':
        count = count + 1
print(count)

str = '   X-DSPAM-Confidence:  0.8475    '.strip() # Using strip to remove all the spaces
print (str)
new = str.replace('DSPAM', 'Gustavo') # Using string.replace to Return a copy of the string with all occurrences of substring old replaced by new.
print(new)
name = new.find('Gustavo')
print (name)



#str1 = "Hello "
#str2 = 'there!'
#bob = str1 + str2
#print (bob)

#str3 = '123'
#x = int(str3) + 1
#print(x)
#try:
#    str3 = float(str3)
#except:
#    exit()
#str3 = str3 + 9000000
#print (str3)

#name = input('Enter:')
#print (name)
#apple = input ('Enter:')
#(The wrong way of doing this) x = apple - 10 (The right way is: x = int(apple) - 10)
#x = int(apple) - 10
#print (x)
