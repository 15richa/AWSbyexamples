'''
This is lambda function to scan a dynamo table
'''

#importing packages
import json
import boto3

#function definition
def lambda_handler(event,context):
    dynamodb = boto3.resource('dynamodb')
    #table name
    table = dynamodb.Table('newtable')
    #inserting values into table
    #response = table.put_item(
       # Item={ 'id': '3', 'name':'aniket','price':'550','quantity':'90'})
    #return response
    response = table.scan()
    
    return response['Items']
