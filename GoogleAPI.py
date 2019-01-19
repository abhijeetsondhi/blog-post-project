import urllib.request
import json
endpoint='https://maps.googleapis.com/maps/api/directions/json?'
api_key='xxx'
origin=input('Source').replace(' ','+')
destination=input('Destination').replace(' ','+')
nav_request='origin={}&destination={}&apikey={}'.format(origin,destination,api_key)
request=endpoint + nav_request
response=urllib.request.urlopen(request).read() #response in string
directions = json.loads(response)
print(directions)
