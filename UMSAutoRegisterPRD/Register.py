#!/usr/bin/python
import json
import thread
import httplib
import urllib
import time
import hashlib

'''
def registerURL (unamer):
    for j in range(2):
        email = unamer + '_' + str(j) + '@test.com'
        registerJsonString = "{\"email\": \"" + email + "\",\"password\": \"098f6bcd4621d373cade4e832627b4f6\",\"tenant\": \"fp\"}"
        postSender(registerJsonString)
    thread.exit_thread()  
    
def postSender(regJsonString):
    data = urllib.urlencode(regJsonString)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection("ums.beta.homestyler.com:8080")
    conn.request("POST", "/v1.0/user", data, headers)
    response = conn.getresponse()
    print response.status, response.reason


def run():
    for i in range(3):
        userName = 'test_' + str(i);
        thread.start_new_thread(registerURL, (userName,))
'''

now = str(int(time.time())*1000)

h = hashlib.sha256(now+'adsk-ezhome')
secret = h.hexdigest()

def registerURL (uname):
    for j in range(1200):
        email = uname + '_' + str(j) + '@autodesk.com'
        #password is '111111'
        
        registerJsonString = "{\"email\": \"" + email + "\",\"password\": \"96e79218965eb72c92a549dd5a330112\",\"tenant\": \"ezhome\"}"
#        jsonData = json.dumps(registerJsonString)
        postSender(registerJsonString)
        
        print "The %s user has been created!",j+1
    
def postSender(registerJsonString):
    #data = urllib.urlencode(regJsonString)
    headers = {"hs_ts":now,"hs_secret":secret,"Content-type": "application/json", "Accept": "application/json","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"}
    conn = httplib.HTTPConnection("juran-3d-prod-ums-elb-public-1-1518510534.cn-north-1.elb.amazonaws.com.cn:8080")
    conn.request("POST", "/v1.0/user", registerJsonString, headers)

    response = conn.getresponse()
    print response.status, response.reason
    
'''
def run():
    for i in range(3):
        userName = '_test_' + str(i);
        thread.start_new_thread(registerURL, (userName,))
'''      
if __name__ == '__main__':
    registerURL('wei.feng')
    