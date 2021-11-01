import json
import sys
import boto3

#This is unfinished. :( 
#I'm submitting what I have as I dont have the time to go back and work this further.

client = boto3.client('cloudformation')

file = sys.argv[1]
print(file)
with open(file) as region_file:
	print(region_file)
	data = json.load(region_file)
	for d in data['regions']:
		try:
			response = client.create_stack(
				StackName='andrewwellsm01x132',
				TemplateBody='file://template132.yml',
				Parameters='file://parameters132.json'
			)
		except:
			print("Error")
