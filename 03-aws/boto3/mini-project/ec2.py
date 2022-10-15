import boto3
import os
from botocore.exceptions import ClientError
import logging

from datetime import datetime, timedelta

# bucket_name = os.environ['BUCKET_NAME']
data = []

client_ec2 = boto3.client('ec2')
client_cloudwatch = boto3.client('cloudwatch')

def get_ec2_cpu_utilization(instance_id, start_time, end_time):
    response = client_cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {
            'Name': 'InstanceId',
            'Value': instance_id
            },
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=60,
        Statistics=[
            'Average',
        ],
        Unit='Percent'
    )
    return response["Datapoints"][0]["Average"]


def ec2_instance_details():
    response = client_ec2.describe_instances()

    # Set time range to cover the last full calendar month
    # Note that the end date is EXCLUSIVE (e.g., not counted)
    now = datetime.datetime.utcnow()
    # Set the end of the range to start of the current month
    end = datetime.datetime(year=now.year, month=now.month, day=1)
    # Subtract a day and then "truncate" to the start of previous month
    start = end - datetime.timedelta(days=1)
    start = datetime.datetime(year=start.year, month=start.month, day=1)
    
    for details in response['Reservations']:
        for instance in details['Instances']:
            name = cpu_utilization = ""
            id = instance['InstanceId']
            state = instance['State']['Name']
            type = instance['InstanceType']
            image = instance['ImageId']
            launch_time = instance['LaunchTime']
            print(f"launch_time : {launch_time}")
            print(f"start_time: {start}")
            state_transition_reason = instance['StateTransitionReason']
            if state == "running":
                if start <= launch_time:
                    cpu_utilization = get_ec2_cpu_utilization(id. start, end)
                elif start < launch_time <= end:
                    cpu_utilization = get_ec2_cpu_utilization(id. launch_time, end)
                elif launch_time > end:
                    cpu_utilization = get_ec2_cpu_utilization(id. launch_time, datetime.now())
            data.append([id,state,type,image,launch_time.strftime("%d-%m-%Y"),state_transition_reason,cpu_utilization])
    return data


# def publish_to_s3():
#     s3 = boto3.client('s3')
#     try:
#         response = s3.upload_file(file_path, bucket_name, file_name)
#     except ClientError as e:
#         logging.error(e)
