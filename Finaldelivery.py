#!/usr/bin/env python
# coding: utf-8

# In[17]:


#!/usr/bin/python
import csv, json

csvFilePath = "C:\\data.csv"
jsonFilePath = "file.json"

data = []
root={}
id1 ="-1" 
id2= "-1"
id3="-1"
with open (csvFilePath,'r') as csvFile:
    
        csvReader = csv.DictReader(csvFile)
        for csvRow in csvReader:
            if not (csvRow["Level 1 - Name"]):
                continue
            if  (csvRow["Level 1 - Name"]) and (id1 !=(csvRow["Level 1 - ID"].strip())):
                id1 = csvRow["Level 1 - ID"].strip()
                socket = {
                     "label":csvRow["Level 1 - Name"],
                "id":csvRow["Level 1 - ID"],
                "link":csvRow["Level 1 - URL"],
                "Children":[]
            }
                data.append(socket)
            if  (csvRow["Level 2 - Name"])  and (id2 !=(csvRow["Level 2 - ID"].strip())):
                id2 = csvRow["Level 2 - ID"].strip()
                packet={}
                packet= {
                    "label":csvRow["Level 2 - Name"],
                    "id":csvRow["Level 2 - ID"],
                    "link":csvRow["Level 2 URL"],
                    "Children":[]
                }
                for i in data:
                    if (i["id"] ==id1):
                        i["Children"].append(packet)
                
            if  (csvRow["Level 3 - Name"]) and (id3 !=(csvRow["Level 3 - ID"].strip())):
                id3 = csvRow["Level 3 - ID"].strip()
                packet= {}
                packet={
                    "label":csvRow["Level 3 - Name"],
                    "id":csvRow["Level 3 - ID"],
                    "link":csvRow["Level 3 URL"],
                    "Children":[]
                }
                for j in data:
                    for k in j["Children"]:
                        if (k["id"]==id2):
                            k["Children"].append(packet)
                
root[csvRow["Base URL"]]= data   
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(root, indent = 4))


# In[ ]:




