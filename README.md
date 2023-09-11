# BurpSuite-Extractor
Description: extracting files or JSON responses from burp when abusing a vulnerability like an IDOR with intruder. <br>
Explanation: the script takes burp's XML output for saved requests, base64 decodes the response and parses the CDATA and filename field in the response. The filename is then used when saving the contents extracted from the CDATA field. The solution worked for my scenario (PDFs, DOCs, XLS) but may not work for all filetypes. 


## Guide:
When you're able to reference and download any file by ID. Intercept the request and forward it to Intruder. <br>
Add a payload list based on reference (numbers for IDs). <br>
Run payload in Intruder and Filter results by 200s <br>
Select all, right click and "Save Selected Items" <br>
Then update the FILEPATH and FOLDERPATH in burp-file-extract.py <br>
The script should be ready to go! <br>

### Usage:
```
python3 burp-file-extract.py
python3 burp-json-extract.py
```

### Reference:
https://www.n00py.io/2020/05/extracting-files-from-burp-intruder-output/
