import iam
import ec2
import xlsxwriter
from datetime import datetime

date_time = datetime.now()
unique_no = date_time.strftime("%y%m%d%H%M%S")
file_name = "ec2-instances-"+unique_no+".xlsx"
file_path = "/tmp/"+file_name

compute_header = ['Id', 'State', 'Type', 'Image-Id', 'Launch-Time', 'Last state', 'Cpu Utilization']
compute_table_header = [{'header': column_name} for column_name in compute_header]

users_header = ['Username', 'Create Date', 'Password last used', 'Access Key last used']
users_table_header = [{'header': column_name} for column_name in users_header]


def create_xlsx(ec2_data, users_data):
    workbook = xlsxwriter.Workbook(file_path, {'remove_timezone': True})
    worksheet_compute = workbook.add_worksheet("Compute")
    worksheet_users = workbook.add_worksheet("Users")
    worksheet_compute.add_table('A1:G7', {'data': ec2_data, 'columns': compute_table_header})
    worksheet_users.add_table('A1:G7', {'data': users_data, 'columns': users_table_header})
    workbook.close()


ec2_data = ec2.ec2_instance_details()
users_data = iam.get_user_details()
if ec2_data or users_data:
    print(users_data)
    create_xlsx(ec2_data, users_data)
#   publish_to_s3()