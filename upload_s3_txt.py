import boto3
import base64
import json
#from boto3.exceptions import ClientError 
#import logging

#event is the json format come with post request : 
'''

event={
"body":"hey this is file . "
}

'''

def lambda_handler(event, context):
    s3=boto3.client('s3')
    with open("/tmp/log.txt","w") as f:
        f.write(event['body'])
        pass
        
    s3.upload_file("/tmp/log.txt","bucket2.sih","logs.txt")    
    
    return {
        'status': 'True',
       'statusCode': 200,
       'body': 'succcessful .'
      }