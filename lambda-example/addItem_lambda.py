'''
This is a lambda function which adds/inserts new items to dynamodb table.
'''

import json
import boto3

def lambda_handler(event,context):
    print(event)
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('newtable')
    print(event['body'])
    
    body = json.loads(event['body'])
    id = body['id']
    name = body['name']
    price = body['price']
    quantity = body['quantity']
  
   

    response = table.put_item( Item={"id":id, "name":name, "price":price, "quantity":quantity})
    print(response)
    response={"Message":"Item with id = "+id+" has been added"}
    return(response)
    