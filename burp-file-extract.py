import bs4
import base64
import re
from bs4 import BeautifulSoup
# Import the Burp File
path = 'FILEPATH'
burp_file = open(path,'r')
xml = burp_file.read()
# Parse the XML with BeautifulSoup
parsed = BeautifulSoup(xml, "html.parser")
for document in parsed.find_all('item'):
    try:
        resp = document.response.string 
        data = base64.b64decode(resp)
        content = data.split(b'\r\n\r\n')[1]
        stringed = str(data)
        pattern = r'filename=\"([^\\"]+)'
        match = re.search(pattern, stringed)
        filename= match.group(1)
        print(filename)
        f = open("/FOLDER-PATH/" + filename, "wb")
        f.write(content)
        f.close()
    except Exception as e:
        print(e)
        pass
