import json
import requests

def registerUrl():
    #url = "http://l-.vc/api/destination/qunarSearchThinkYouLikeResult?vid=80011147&uid=894DFE59-6E2D-4D77-AD93-8F5759DBEEDA&gid=A39E13EC-7CA8-0DF5-665E-12C29318D2F6&username=bbufeld5488&num=10"
    #data = requests.get(url).json()
    #print data
    #print (type(data))
    #print json.dumps(data, ensure_ascii=False, indent=4)
    #f = open ('url1.txt','r')
    with open(r'url.txt') as f1:
        url = f1.readlines()
        result = requests.get(url[0]).json()
        result_json = json.dumps(result,ensure_ascii=False,indent=4)
        print json.dumps(result,ensure_ascii=False,indent=4)
        #print (url[0])
        #print (url[1])
        #print (url[2])

    with open(r'result.txt','w') as f2:
        f2.writelines(result_json)



registerUrl()
