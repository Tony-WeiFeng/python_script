import urllib2

jsonData = '''{"designId":"33cd4179-ca89-476d-8de7-da5f99461b78","token":"185620d5649916058b72efe62bdf7938","transactionId":"ezhome"}'''
opener = urllib2.build_opener(urllib2.HTTPHandler)
request = urllib2.Request('http://ec2-54-235-252-117.compute-1.amazonaws.com:9000/deleteDesign',data = jsonData)
request.add_header('Content-Type', 'application/json')
request.get_method = lambda:'DELETE'
url = opener.open(request)

print url