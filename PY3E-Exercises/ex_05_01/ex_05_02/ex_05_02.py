largest = None
smallest = None
numfloat = 0
#value = 0

while True:
    sval = input ('Enter a Number: ')
    #print ('Before =', sval, largest, smallest, numfloat)
    if sval == 'done':
        break
    try:
        numfloat = float(sval)

    except:
        print('Invalid input')
        continue

    if smallest is None or numfloat < smallest:
            smallest = numfloat
            #print ('Smallest =', smallest)
            continue
    elif largest is None or numfloat > largest:
    #elif largest == 0 or numfloat > 2:
            largest = numfloat
            #print ('Largest = ', largest)
            continue
    #print(numfloat)

intlarg = int(largest)
intsm = int(smallest)

print ('Maximum is',intlarg)
print ('Minimum is',intsm)
