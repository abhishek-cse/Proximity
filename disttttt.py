
from pymongo import MongoClient as mc
from pymongo import errors as mongoerror
from pymongo import *

#mongo_host="sundry.wifitics.com"
mongo_port=27017

#mongo_proximity1_username="proxiana"
#mongo_proximity1_password="proximfiltereddata"
mongo_host="3.6.162.156"
mongo_proximity2_username="tushar"
mongo_proximity2_password="tushar422"




mongo_proximity_db="proximity_macids"
url="mongodb://{}:{}@{}:{}/?authSource={}"
url=url.format(mongo_proximity2_username,mongo_proximity2_password,mongo_host,mongo_port,mongo_proximity_db)
mongo_client=mc(url,appname="wt_mongo_client",connect=False,maxPoolSize=500)
mongo_conn=mongo_client.proximity_macids


url2="mongodb://{}:{}@{}:{}/?authSource=proximity_distance_filter&authMechanism=SCRAM-SHA-256"
url2=url2.format(mongo_proximity2_username,mongo_proximity2_password,mongo_host,mongo_port)
mongo_client2=mc(url2,appname="wt_mongo_client2")
db=mongo_client2['proximity_distance_filter']
collection = db['18:A6:F7:72:D5:CA']
#mongo_conn=mongo_client2.proximity_distance
#mongo_conn = mongo_client2['proximity_distance_filter']

#mongo_proximity1_username="proxiana"
#mongo_proximity1_password="proximfiltereddata"
mongo_proximity2_username="nmswifitics"
mongo_proximity2_password="nms221308"




a=list(mongo_conn.list_collection_names())


prefixes = ('IMF', 'RU','ping_')
newlist = [x for x in a if not x.startswith(prefixes)]


cursor=mongo_conn['18:A6:F7:72:D5:CA'].find()

docs=list(cursor)
# print(docs)
rss=[]
callingstationid=[]
for i in range(len(docs)):
    rss.append((docs[i]['rss']))
    callingstationid.append((docs[i]['callingstationid']))

# for j in range(len(docs)):
#   #x=(dict(zip((docs[j]['rss']), (docs[j]['callingstationid']))))
#   #print(docs[j]['rss'])
#   # print(docs[j]['callingstationid'])
#   print(dict(zip((docs[j]['rss']), (docs[j]['callingstationid']))))

ans = []

for x in rss:
    def res(x):
        return 10 ** ((-69-(x))/(10 * 2))
    ans.append(res(x))

strAns=list(map(str, ans))
#print((strAns))
# print((callingstationid))
mydictionary = dict(zip(callingstationid, strAns))
new_dict={}


# def Convert(tup, di):
#   for a, b in tup:
#     di.setdefault(a, []).append(b)
#   return di

def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

# x=Convert((next(iter(mydictionary.items()))), new_dict)
#for k,v in mydictionary:
for i in range(len(mydictionary)):
 x=Convert(list(next(iter(mydictionary.items()))))
# print(type(x))
 print(x)
 collection.insert_one(x)
 mydictionary.pop(next(iter(mydictionary.keys())))

import json

# for i in range(len(mydictionary)):
#   if i>0:
#     print(mydictionary.)
#     break




  # print(mydictionary.items())
# print(len(mydictionary.keys()))
# print(len(mydictionary.values()))
jsonobject= json.dumps(mydictionary)

# print(jsonobject)
# collection.insert_one(jsonobject)

D_0M_5M=0
D_5M_10M=10
for value in ans :
    if value >=1 and value <5 :
        D_0M_5M=D_0M_5M+1
    elif 5 <= value < 10:
        D_5M_10M = D_5M_10M + 1
# print(D_0M_5M)

#add a dictionary for distance corresponding to calling station id's - i am working on this
#dump the data in the table proximity_distance_filter
# this is being done for a single router which is a table(collection) in the DB.
# do this for all the tables -- follow the code in space 2

