from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_devices_info():
    query = """
    {
        device_list(manufacturer_id:"3"){
        id,
        name,
        device_type {
        id,
        manufacturer {
            id,
            name
        }
        }
        }
    }
    """
    url = "https://demo.netbox.dev/graphql/"
    headers = {'Authorization': "Token b2d0cd582a5a2c5cc53647671c879f415e6e25ca" } 
    r = requests.get(url, headers=headers, json={'query': query}) 
    print(json.dumps(r.json(), indent=4))

def get_manufacturer_list():
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
    return resume_manufacturer


@app.route("/")
def index():
    titulo = "Prueba obteniendo lista de manufactura de Netbox"
    manufacturer_list = get_manufacturer_list()
    return render_template("index.html", titulo=titulo, manufacturer_list=manufacturer_list)

if __name__ == "__main__":
    app.run(debug=True)