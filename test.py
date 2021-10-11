import requests
import json

query = """
{
 	manufacturer_list{
 	  id,
    name
 	}
}
""" 
url = "https://demo.netbox.dev/graphql/"
headers = {'Authorization': "Token b2d0cd582a5a2c5cc53647671c879f415e6e25ca" } 
r = requests.get(url, headers=headers, json={'query': query}) 
data = r.json()
manufacturer_list = data['data']['manufacturer_list']
resume_manufacturer = []
for element in manufacturer_list:
    resume_manufacturer.append(element['name'])
print(resume_manufacturer)
#print(json.dumps(r.json(), indent=4))
#print(r)