print ([1, 24, 76]) #List constants are surrounded by square brackets and the elements in the list are separated by commas
print (['red', 'yellow' , 'blue'])
print (['red', 24, 98.6])
print ([1,[5,6],7])
print ([]) # A list can be empty

friends = ['Joseph', 'Glenn', 'Sally'] # This variable is basically 'holding' the list. The list in this case = names of friends
for friend in friends:
    print('Happy New Year:', friend)
print('Done!',)

print(range(len(friends))) # The range function returns a list of numbers that range from zero to one less than the paramete
                            # The len() function takes a list as a parameter and returns the number of elements in the list
for i in range(len(friends)): #this code do the exact same thing that the 'for' above.
    friend = friends[i]
    print('Happy New Year:', friend)

#lists are mutable, mutable is another other for changeable - - we can change an element of a list using the index operator
lotto = [2, 14, 26, 41, 63]
lotto[2] = 28   #On this line we change the 'value' of the number on the position 2 to 28. It was 26, now is 28
print(lotto)
#Strings are “immutable” - we cannot change the contents of a string - we must make a new string to make any change
