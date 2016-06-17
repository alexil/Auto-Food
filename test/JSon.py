import json
from pprint import pprint

with open('data.json') as data_file:
    data = json.load(data_file)

pprint(data)

print("--\n--\n")
mmm = data['maps']

for ll in mmm:
    print(ll['id'])
    # print(ll[id])

