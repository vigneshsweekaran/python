import boto3

data = []

client_iam = boto3.client('iam')


def access_key_last_used(username):
    date = []
    access_key_list_response = client_iam.list_access_keys(UserName=username)
    for access_key in access_key_list_response['AccessKeyMetadata']: # User can have more than one keys
        access_key_id = access_key['AccessKeyId']
        access_key_last_used_response = client_iam.get_access_key_last_used(AccessKeyId=access_key_id)
        if "LastUsedDate" in access_key_last_used_response['AccessKeyLastUsed']:
            date.append(access_key_last_used_response['AccessKeyLastUsed']['LastUsedDate'].strftime("%d-%m-%Y"))
    return date


def get_user_details():
    password_last_used = access_key_last_used_time = ""
    response = client_iam.list_users()
    for user in response['Users']:
        user_name = user['UserName']
        create_date = user['CreateDate'].strftime("%d-%m-%Y")
        if 'PasswordLastUsed' in user:
            password_last_used = user['PasswordLastUsed'].strftime("%d-%m-%Y")
        access_key_last_used_time = "".join(access_key_last_used(user_name))
        data.append([user_name,create_date,password_last_used,access_key_last_used_time])
    return data