import json

# Opening JSON file
f = open('Proximity.json',)
# returns JSON object as
# a dictionary
data = json.load(f)
# Iterating through the json
# list
# for i in data:
#     print(i)
rss=[]
for i in range(len(data) -1):
    rss.append((data[i]['rss']))
print("rss=", rss)

# Closing file
f.close()
