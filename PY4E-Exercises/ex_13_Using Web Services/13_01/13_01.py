import json
import urllib.request, urllib.parse, urllib.error
import ssl

count = 0
sum = 0
url = 'http://py4e-data.dr-chuck.net/comments_1410737.json'
html = urllib.request.urlopen(url)
data = html.read().decode()
#print("Retrived", (data),"characters")

js = json.loads(data)
#print('User counts:',len(js))
#print(js.items())

for item in js['comments']: #loop through each item in the list 'comments'
    count = count + 1 # now item is a dictionary with name and count in it
    sum = sum + item['count']
# -----------------------------------------------------------
# Another way of doing the line above:
# x = x + int(items['count'])
# Here we are already converting the VALUE of 'items' into a integer
# -----------------------------------------------------------

"""
    sum is equal to sum, which is (0 = 0 + count).
    In item['count'] we are looping through each 'value' in the key 'count' and adding in into the variable sum
    REMEMBER THAT ITEM IS A DICTIONARY WITH KEYs AND VALUEs
"""
print(sum)






#name = js['comments'] [0] ['name']
#count = js['comments'] [0] ['count']
#print(name, count)
#for item in js:
    #print('Comments', item[:])
#for word in js:
    #print('LOADING')
    #for word in js:
        #print(word)
