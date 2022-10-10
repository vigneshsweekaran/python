import iam
import ec2
import xlsxwriter
from datetime import datetime

date_time = datetime.now()
unique_no = date_time.strftime("%y%m%d%H%M%S")
file_name = "ec2-instances-"+unique_no+".xlsx"
file_path = "/tmp/"+file_name

header = ['Id', 'State', 'Type', 'Image-Id', 'Launch-Time', 'Last state', 'Cpu Utilization']
table_header = [{'header': column_name} for column_name in header]


def create_xlsx(data):
    workbook = xlsxwriter.Workbook(file_path, {'remove_timezone': True})
    worksheet_compute = workbook.add_worksheet("Compute")
    worksheet_users = workbook.add_worksheet("Users")
    worksheet_compute.add_table('A1:G7', {'data': data, 'columns': table_header})
    workbook.close()


ec2_data = ec2.ec2_instance_details()
user_data = iam.get_user_details()
if ec2_data:
    create_xlsx(ec2_data)
#   publish_to_s3()