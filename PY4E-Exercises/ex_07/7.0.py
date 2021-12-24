#fname = input("Enter file name: ")
#fh = open(fname)

#count = 0
#for line in fh:
    #s = line.rstrip()
    #print(s.upper())
    #count = count + 1


fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    rs = line.strip('X-DSPAM-Confidence: ')
    frs = float(rs)
    total = total + frs
    r = total/count

print('Average spam confidence:', r)
