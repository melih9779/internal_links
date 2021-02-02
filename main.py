import pandas as pd
from trnlp import *


csv = pd.read_csv("data3.csv",usecols=['Content 1', 'Address']).dropna()
print(csv)
block_list= ['.','_','-','*','>','<','-','?']
data = []


for index, row in csv.iterrows():
    data.append({"data":simple_token(row["Content 1"], sw=block_list),"url":row["Address"]})
    

search= ["keywords"]
search_url = []
insert_url = []
for a in data:
    if a["data"][0] not in block_list:
        url_once = a["url"]
        for b in a["data"]:
            
            for a_f in data:
                for b_f in a_f["data"]:
                    url_two = a_f["url"]
                    if b == b_f and b in search and url_once != url_two:
                        ##print(b)
                        in_url = a["url"]+a_f["url"]
                        in_url2 = a_f["url"]+a["url"]
                        if not in_url in insert_url and not in_url2 in insert_url:
                            search_url.append({"url1":a["url"],"url2":a_f["url"],"keyword":b})
                            insert_url.append(in_url)

print(pd.array(search_url))
