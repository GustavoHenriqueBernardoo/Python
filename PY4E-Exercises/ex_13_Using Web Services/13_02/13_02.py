# ----------------------------------------------------------------------------------
#Calling a JSON API
#In this assignment you will write a Python program somewhat similar
#to http://www.py4e.com/code3/geojson.py. The program will prompt for a location,
#contact a web service and retrieve JSON for the web service and parse that data,
#and retrieve the first place_id from the JSON. A place ID is a textual identifier
#that uniquely identifies a place as within Google Maps.
# ----------------------------------------------------------------------------------

import json,ssl
import urllib.request,urllib.parse, urllib.error



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



#Stroring the given parameters
api_key = 42
serviceurl = "http://py4e-data.dr-chuck.net/json?"
# sample_address = "South Federal University"
data_address = "IT College of Estonia"
address_wanted = data_address

#Setting the GET parameters on the URL
parameters = {"address": address_wanted, "key":api_key}
paramsurl = urllib.parse.urlencode(parameters)

#Generating the complete URL. Printing it in order to check if it's correct.
queryurl = serviceurl.strip() + paramsurl.strip()
print("DATA URL: ", queryurl)

#Obtaining and reading the data
try :
    data_read = urllib.request.urlopen(queryurl , context=ctx).read()
    data = data_read.decode()
    # Parsing the data and looking for the field we want.
    jsondata = json.loads(data)
    print(jsondata)
    place_id = jsondata["results"][0]["place_id"]
    print("PLACE ID: ", place_id)
except:
    print("Error.....")
    print("-"*50)
    print(data)
