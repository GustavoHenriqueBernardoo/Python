import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse
import urllib.error
import ssl
sum = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = 'http://py4e-data.dr-chuck.net/comments_1410736.xml'
html = urllib.request.urlopen(url)
data = html.read()
print("Retrieved",len(data),"characters")
#html.decode()

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
print('Count:', len(lst))
for item in lst:
    sum = sum+float(item.find('count').text)
print(sum)
