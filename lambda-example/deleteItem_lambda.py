'''
This is a lambda function which deletes an item from dynamodb table.
'''
import json
import boto3

#function definition
def lambda_handler(event,context):
    print(event)
    id=int(event['pathParameters']['id'])
    print(id)
    dynamodb = boto3.resource('dynamodb')
    #table name
    table = dynamodb.Table('newtable')
    #inserting values into table
    response = table.delete_item( Key= {'id': id})
    response={"Message":"Item with id = "+str(id)+" is deleted"}
    return response
