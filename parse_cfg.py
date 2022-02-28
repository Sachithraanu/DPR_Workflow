import json
from airflow.models import Variable

###### PLEASE UPDATE THIS SECION  --- IF RUNNING ENVIRONEMT IS DIFFERENT FROM QA OR PROD ###################
aws = json.loads(Variable.get("tosca_aws"))
aws_creds = {
   'aws_access_key_id': aws['aws_access_key_id'],
   'aws_secret_access_key': aws['aws_secret_access_key']
}


email = json.loads(Variable.get("email"))
email_creds= {
   'email_id': email['username'],
   'email_pwd': email['password'],
}

username = 'PowerBI_SVC@toscaltd.com '
password = 'p3OT21p!HR9i'

redshift = json.loads(Variable.get("airflow_redshift"))
redshift_creds = {
   'user_id': redshift['user'],
   'user_pwd': redshift['password'],
   'db': redshift['dbname'],
   'host': redshift['host'],
   'port': redshift['port']
}


file_errors_email_list = [e.strip() for e in Variable.get("kruger_finance_file_errors_mail").split(",")]
file_data_email_list = [e.strip() for e in Variable.get("kruger_data_errors_mail").split(",")]

#file_errors_email_list = ['pavithra.kariyawasam@datamtx.com']
#file_data_email_list  = ['pavithra.kariyawasam@datamtx.com']
#######################################################################################################



S3_BUCKET = 'tosca-test'

base_url_sharepoint = 'https://toscaltd.sharepoint.com/sites/Operations/'

folder_path_sharepoint = '/sites/Operations/Shared Documents/Public/Daily Production Reporting/'

source_ActivityArchive = ('Site', 'Date', 'SC', 'Shift', 'Activity', 'Line', 'Supply Chain', 'Qty', 'Shift Hrs', 'Machine Hrs', 'Chain Hrs', 'Reg EE Hrs', 'OT EE Hrs', 'Hrly Rate', 'Activity Cost', '---', 'InWash', '---', '---', 'Change Flag') #removed IFCO billling
source_DayArchive = ('Site', 'Date', 'Service Center', 'Shift', 'Shift Staffing', 'Attendance', 'Notes', 'Change Flag', 'ADP Reg Hours', 'ADP OT Hours') #removed IFCO billling
source_DowntimeArchive = ('Site', 'Date', 'Wash Site', 'Line', 'Shift', 'Duration', 'Equipment', 'Reason', 'Notes', '0') #removed IFCO Billed

cites = ['Charlotte/DPR_V2 - Charlotte1.xlsm'
                ]

files = {'DPR_V2 - Charlotte1.xlsm': ['ActivityArchive', 'DayArchive', 'DowntimeArchive']
                 }