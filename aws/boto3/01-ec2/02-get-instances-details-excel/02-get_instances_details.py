import boto3
import xlsxwriter
import os
from botocore.exceptions import ClientError
import logging
import json

from datetime import datetime, timedelta

# bucket_name = os.environ['BUCKET_NAME']

header = ['Id', 'State', 'Type', 'Image-Id', 'Lauch-Time', 'Last state', 'Cpu Utilization']
data = []

date_time = datetime.now()
unique_no = date_time.strftime("%y%m%d%H%M%S")
file_name = "ec2-instances-"+unique_no+".xlsx"
file_path = "/tmp/"+file_name

client_ec2 = boto3.client('ec2')
client_cloudwatch = boto3.client('cloudwatch')

def get_ec2_cpu_utilization(instance_id):
    response = client_cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {
            'Name': 'InstanceId',
            'Value': instance_id
            },
        ],
        StartTime=datetime(2022, 10, 8),
        EndTime=datetime.now(),
        Period=60,
        Statistics=[
            'Average',
        ],
        Unit='Percent'
    )
    return response["Datapoints"][0]["Average"]

def ec2_instance_details():
    response = client_ec2.describe_instances()
    
    for details in response['Reservations']:
        for instance in details['Instances']:
            name = cpu_utilization = ""
            id = instance['InstanceId']
            state = instance['State']['Name']
            type = instance['InstanceType']
            image = instance['ImageId']
            launch_time = instance['LaunchTime']
            state_transition_reason = instance['StateTransitionReason']
            if state == "running":
                cpu_utilization = get_ec2_cpu_utilization(id)
            data.append([id,state,type,image,launch_time,state_transition_reason,cpu_utilization])



def create_xlsx(data):
    workbook = xlsxwriter.Workbook(file_path, {'remove_timezone': True})
    worksheet = workbook.add_worksheet("Compute")
    row = 0

    for item in data :
        item_length = len(item)
        for index in range(item_length):
            worksheet.write(row, index, item[index])
        row += 1

    workbook.close()


# def publish_to_s3():
#     s3 = boto3.client('s3')
#     try:
#         response = s3.upload_file(file_path, bucket_name, file_name)
#     except ClientError as e:
#         logging.error(e)


ec2_instance_details()
if data:
    create_xlsx(data)
#   publish_to_s3()