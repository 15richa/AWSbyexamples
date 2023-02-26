'''
This is a lambda function to get item from dynamodb
'''

import json
import boto3

#function definition
def lambda_handler(event,context):
    print(event)
    id=event['pathParameters']['id']
    dynamodb = boto3.resource('dynamodb')
    #table name
    table = dynamodb.Table('newtable')
    #inserting values into table
    response = table.get_item( Key={"id":id})
    return response['Item']
