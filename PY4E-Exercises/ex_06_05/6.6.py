str = '   X-DSPAM-Confidence:  0.8475    '.strip()
print (str)
new = str.replace('DSPAM', 'Gustavo')
print(new)
fn = new.find('Gustavo')
print (fn)
name = new[fn:9]
print(name)
