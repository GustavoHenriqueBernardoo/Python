
num = 0
value = input("Write the number that you want:")

try:
    fv = float(value)
except:
    print ("Error: Invalid input")
    exit()

while True:
    line = input ('> ')
    if line [num] == 'num':
        continue
    if line == 'done':
        break
    print(num)
print ('Done!')
