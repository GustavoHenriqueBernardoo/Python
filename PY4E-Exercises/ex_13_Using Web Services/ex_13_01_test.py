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


url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
html = urllib.request.urlopen(url).read()

#print('Retrieved', len(html), 'characters')
html.decode()

tree = ET.fromstring(html)
lst = tree.findall('count')
print(lst)
for item in lst:
    print('Name', item.find('name').text)
    print('Count', item.find('count').text)
