import requests
import time
import pickle
import random
import json

token='EAACpObVtkFIBABz5mlaaXZCN50kIzAImRoOOxzMgSEwZBZCsN4boWDgkWVHmC1t1iEAhBk35AmFj0InL0ZARUQT0QUOwYOemeGPjR08fKpZCbRZCXdo13xZCZC06ZBGYPBiztcuxcncnz0g1zzM3Er8lkSiAjv3wZBQWR9ZAZCUMcT4ZAR0wrPhSxhUKTNW4rVDiq52AZD'

me='https://graph.facebook.com/v2.9/me?access_token='+token
friends='https://graph.facebook.com/v2.9/me/friends?access_token='+token
#search='https://graph.facebook.com/v2.9/me/search?type=user&q=sachikanta thingbaijam&access_token='+token

me1=requests.get(me)
f1=requests.get(friends)
print(me1.text)
print(f1.text)
'''
def req_facebook(req):
    r= requests.get("https://graph.facebook.com/v2.9/" + req,{'access_token':token})

    return r
#req='https://graph.facebook.com/v2.9/me/post?access_token='+token
req = "1900306650028284/posts?fields=comments,likes&limit=4"
results=req_facebook(req).json()
data=[]

i=0
while True:
    try:
        time.sleep(random.randint(2,5))
        data.extend(results['data'])
        r=requests.get(results['paging']['next'])
        results=r.json()
        i+=1
        if i>5:
            break
    except:
        print ("done")
        break
pickle.dump(data,open("facebook_data.pkl","wb"))
loaded_data= pickle.load(file=open("facebook_data.pkl"))'''


