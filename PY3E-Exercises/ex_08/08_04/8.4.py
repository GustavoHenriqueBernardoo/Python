inpf = input('Enter the file name: ') #inpf = input file
fhand = open ('romeo.txt') # fhand = file hand
lst = list()
#delimeter = ''
#some = ['is, the, it, and']
try:
    fhand = open(inpf)
except:
     print('File does not exist:', inpf)
     exit()
for line in fhand:
    sl = line.split() #sl = split line
    for word in sl:
        print(sl)
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)


#t = list(line)  In this line I'm breaking the variable line into individual letter

# sort arranges the elements of the list from low to high:
#>>> list = ['d', 'c', 'e', 'b', 'a']
#>>> list.sort()
#>>> print(list)
#lst1 = sl[0] # lst = lists
#lst2 = sl[1]
#lst3 = sl[2]
#lst4 = sl[3]
#lst5 = sl[4]
#lst6 = sl[5]
#lst7 = sl[6]
#lst8 = sl[7]
#unique = lst1 + lst2 + lst3 + lst4 + lst5 +  lst6 + lst7 + lst8
