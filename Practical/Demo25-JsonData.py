import json

data='''{
"name" : "Swati",
"phone" :{ "type":"intl" , "number":"97867543" },
"email":{"hide":"yes" }
}
'''
'''
info=json.loads(data)
print('Name is',info["name"])
print('Hide',info["email"]["hide"])


print("---------------------------------------------------->")
'''


data='''[
{  "id":"001", "name":"Swati","project":"LKM" },
{  "id":"002", "name":"Anagha","project":"BT" }
]
'''

'''
info=json.loads(data)

print(info)
print('USer count',len(info))
#as it is a simply list we can iterate thru it


for item in info:
    print('Id is',item["id"])
    print('Name is',item["name"])
    
'''





#---------------- course era que------------------------------------

'''
from urllib.request import urlopen
import json

#url = input(r"Enter location: ")
url="http://py4e.dr-chuck.net/comments_93807.json"

address = urlopen(url)
#data = address.read()

total = 0

while True:
	if len(url)<1: break

	print("Retrieving: ", address)
	print("Retrieved ", len(data)," characters")

	info = json.loads(data)
	info = info["comments"]
	for item in info:
		print("Count: ",item["count"])
		total += int(item["count"])
		print("Sum: ", total)
	print("Final sum: ", total)
	break

'''

'''
from urllib.request import urlopen
import json
url="http://py4e.dr-chuck.net/comments_93807.json"

conn=urlopen(url)

print(conn)

'''





'''
import json

from urllib.request import urlopen
import json
url="http://py4e.dr-chuck.net/comments_93807.json"

conn=urlopen(url)

info=json.loads(conn)

#print(info)

#print(info['note'])
#print(info['comments'])

li=info['comments']
sum=0
for i in li:
    #print(i['count'])
    sum=sum+i['count']

print(sum)

'''



#----------------  correct code --------------------------------------------------
'''

import urllib
import json

url = input(r"Enter location: ")
address = urllib.urlopen(url)
data = address.read()

total = 0

while True:
	if len(url)<1: break

	print("Retrieving: ", address)
	print("Retrieved ", len(data)," characters")

	info = json.loads(data)
	info = info["comments"]
	for item in info:
		print("Count: ",item["count"])
		total += int(item["count"])
		print("Sum: ", total)
	print("Final sum: ", total)
	break



'''



#--------------------------2nd geo wala assignment done-------------------------------------------
from urllib.request import urlopen
from urllib.parse import urlencode
import json

place_name = input(r"Enter a place name: ")

base_url = "http://python-data.dr-chuck.net/geojson?sensor=false&"
address_param = urlencode({'address': place_name})

target = base_url + address_param

print("Retrieving {0}".format(target))


connection = urlopen(target)


raw_data = connection.read()

print("Retrieved {0} characters".format(len(raw_data)))

parsed_data = json.loads(raw_data)

print( "Place id", parsed_data["results"][0]["place_id"])








































      
