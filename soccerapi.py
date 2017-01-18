import json
import requests

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': '17ea9f531ef24bfabc288bba11b27cf7', 'X-Response-Control': 'minified' }
connection.request('GET', '/v1/competitions', None, headers )
response = json.loads(connection.getresponse().read().decode())

# print (response)

competitions = response["competitions"]