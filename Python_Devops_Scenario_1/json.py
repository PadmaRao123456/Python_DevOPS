import json
# Script to parse Json
json = json.loads(open('AWS_Ec2.json').read())
value = json['name']
print(value)
