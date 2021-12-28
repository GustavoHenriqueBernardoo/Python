fhand = open ('romeo.txt')
counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
#print(counts)
lst = []
for key, val in counts.items():
    newtup = (val, key) #newtup = new tuple in switch order, val and key insted of key and val
    lst.append(newtup) # adding the key and value into the new tuple list
lst = sorted(lst, reverse=True) # sorting the tuple list by reverse order because we switch val and key to works

for val, key in lst [:10] : # [:10] means starts with 0 and not including 10.
    print(key, val)
