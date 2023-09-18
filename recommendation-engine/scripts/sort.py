import json
from operator import itemgetter

d = open('data_dump.json', 'r').read()

data = json.loads(d)

f = open("sort_data.json", "a")

for i in range(len(data)):
    for j in range(len(data[i]["items"])):
        for k in range(len(data[i]["items"][j]["items"])):
            data[i]["items"][j]["items"][k]["items"] = sorted(
                data[i]["items"][j]["items"][k]["items"], key=itemgetter('Rating'), reverse=True)

print(data)

for item in data:
    f.write(json.dumps(item))
    f.write(",")
