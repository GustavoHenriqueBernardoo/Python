import json
import urllib.request, urllib.parse, urllib.error
import ssl
sum = 0
url = 'http://py4e-data.dr-chuck.net/comments_42.json'
html = urllib.request.urlopen(url)
data = html.read().decode()
count = list()
#print("Retrived", (data),"characters")

js = json.loads(data)
print('Counts:',len(js))
print(js)
name = js['comments'] [0] ['name']
count = js['comments'] [0] ['count']
print(name, count)
for item in js:
    print('Comments', item[:])
for word in js:
    print('LOADING')
    for word in js:
        print(word)
