import json
import boto3
from botocore.vendored import requests
import time


def lambda_handler(event, context):

    print("First json.dumps: ",json.dumps(event, indent=4, sort_keys=True))

    print("LINE1")
    s3_info = event['Records'][0]['s3']
    bucket_name = s3_info['bucket']['name']
    key_name = s3_info['object']['key']
    print("bucket_name: ",bucket_name)
    
    client = boto3.client('rekognition',region_name='us-east-1')
    print("LINE1.1")
    
    pass_object = {'S3Object':{'Bucket':bucket_name,'Name':key_name}}
    print("pass_object: ", pass_object)
    print("LINE2")
    
    resp = client.detect_labels(Image=pass_object)
    print("LINE3")
    
    print('<---------Now response object---------->')
    print("json dumps: ",json.dumps(resp, indent=4, sort_keys=True))
    timestamp =time.time()
    
    
    labels = []

    for i in range(len(resp['Labels'])):
        labels.append(resp['Labels'][i]['Name'])
    
    print('<------------Now label list----------------->')
    print(labels)
    
    #print('<------------Now required json-------------->')
    format = {'objectKey':key_name,'bucket':bucket_name,'createdTimestamp':timestamp,'labels':labels}
    required_json = json.dumps(format)
    print("required_json",required_json)
    
    url = "https://vpc-photos2-sddcn5ldtjc3nh3ohvzojacdtm.us-east-1.es.amazonaws.com/photos2/0"
    # url = "https://vpc-photos-rm6eekicpb4hlkkuxyx7fzdihq.us-east-1.es.amazonaws.com"
    
    headers = {"Content-Type": "application/json"}
    #url2 = "https://vpc-photos-b4al4b3cnk5jcfbvlrgxxu3vhu.us-east-1.es.amazonaws.com/photos/_search?pretty=true&q=*:*"
    
    r = requests.post(url, data=json.dumps(format).encode("utf-8"), headers=headers)
    # resp_elastic = requests.get(url2,headers={"Content-Type": "application/json"}).json()
    print('<------------------GET-------------------->')
    
    print(r.text)
    # print("resp_elastic: ",json.dumps(resp_elastic, indent=4, sort_keys=True))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

    #testing the codepipeline
    #TESTING THE BUILD PIPELINE
    #testing the fils