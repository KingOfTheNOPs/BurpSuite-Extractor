import bs4
import base64
import re
import json

from bs4 import BeautifulSoup
# Import the Burp File
path = 'FILE-TO-OPEN'
burp_file = open(path,'r')
xml = burp_file.read()
# Parse the XML with BeautifulSoup
parsed = BeautifulSoup(xml, "html.parser")
for document in parsed.find_all('item'):
    try:
        #extract response data
        resp = document.response.string 
        data = base64.b64decode(resp)
        content = data.split(b'\r\n\r\n')[1]
        stringed = str(data)
        # get everything after Content-Length Header
        index=stringed.find("Content-Length:")
        important= stringed[index:]
        json_data_index = important.find("\\r\\n\\r\\n")
        json_data = important[json_data_index+8:]
        # data had trailing ' to remove
        json_data =  json_data[:-1]
        json_data_parsed = json.loads(json_data)
        # saving data based on name in response
        first_name = json_data_parsed.get("firstName", "Unknown")
        last_name = json_data_parsed.get("lastName", "Unknown")
        # Remove invalid characters from filename
        file_name = f"{first_name}_{last_name}.json".replace(" ", "_").replace("(", "").replace(")", "")
        with open(file_name, "w") as json_file:
            json.dump(json_data_parsed, json_file, indent=4)
    except Exception as e:
        print(e)
        pass
