import boto3

client_iam = boto3.client('iam')

def get_user_details():
    password_last_used = ""
    response = client_iam.list_users()
    for user in response['Users']:
        print(F"user {user}")
        user_name = user['UserName']
        create_date = user['CreateDate']
        if 'PasswordLastUsed' in user:
            password_last_used = user['PasswordLastUsed']
        print(f"{user_name}, {create_date}, {password_last_used}")