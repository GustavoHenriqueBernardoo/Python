largest = None
smallest = None
num = 0
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        numb = int(num)
    except:
        print ("Invalid input")
        continue
    if smallest is None:
        smallest = numb
    elif numb < smallest :
        smallest = numb
    if largest is None:
        largest = numb
    elif numb > largest:
        largest = numb
print ("Maximum is", largest)
print ("Minimum is", smallest)
