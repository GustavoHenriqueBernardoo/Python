counts = { 'chuck' : 1, 'annie' : 42, 'jan' : 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])
#print the keys in alphabetical order
print('Espace\n')
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])
