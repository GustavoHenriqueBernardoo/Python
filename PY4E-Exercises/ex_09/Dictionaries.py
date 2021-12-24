counts = dict() # create a empty dictionary
surname = {} # is the same thing as = dict() - create a empty dictionary
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen', 'cwen', 'cwen']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
#print('Counting the most common name:', counts)

surname ['name'] = 'Gustavo'
surname ['age'] = 27
#print(surname)
surname ['age'] = 30
#print('Changing the age in the dictionary', surname)

# Simplified Counting with get()
for name in names:
    counts[name] = counts.get(name, 0) + 1 # We can use get() and provide a default value of zero when the key(name) is not yet in the dictionary - and then just add one
print('Counting the most common name using .get:', counts)

#Dictionary as a set of counters

word = 'brontosaurus'
d = dict()
#for c in word:
    #if c not in d:
        #d[c] = 1
    #else:
        #d[c] = d[c] + 1
#print('Example using if:', d)
for c in word:
    d[c] = d.get(c, 0) + 1
print('Example using (key)get:\n', d)
