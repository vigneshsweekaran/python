import boto3
import csv
import datetime
import os
from botocore.exceptions import ClientError
import logging
import json

# bucket_name = os.environ['BUCKET_NAME']

header = ['Id', 'Name', 'State', 'Type', 'Image-Id', 'Lauch-Time', 'Last state']
data = []

date_time = datetime.datetime.now()
unique_no = date_time.strftime("%y%m%d%H%M%S")
file_name = "ec2-instances-"+unique_no+".csv"
file_path = "/tmp/"+file_name

def ec2_instance_details():
    name = ""
    client = boto3.client('ec2')
    response = client.describe_instances()
    
    for details in response['Reservations']:
        for instance in details['Instances']:
            id = instance['InstanceId']
            state = instance['State']['Name']
            type = instance['InstanceType']
            image = instance['ImageId']
            launch_time = instance['LaunchTime']
            state_transition_reason = instance['StateTransitionReason']
            data.append([id,state,type,image,launch_time,state_transition_reason])

def create_csv_file(data):
    with open(file_path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        # write multiple rows
        writer.writerows(data)

# def publish_to_s3():
#     s3 = boto3.client('s3')
#     try:
#         response = s3.upload_file(file_path, bucket_name, file_name)
#     except ClientError as e:
#         logging.error(e)

ec2_instance_details()
if data:
    create_csv_file(data)
#   publish_to_s3()