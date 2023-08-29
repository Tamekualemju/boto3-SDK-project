# option : 1 (not advice)

import boto3

client = boto3.client(                                        #<---- this client is for for s3 communication, 
    's3',
    aws_access_key_id=ACCESS_KEY,                             #<---- access and secrete access key is give access to a specific aws account. hard coding you credentials is very wrong
    aws_secret_access_key=SECRET_KEY

)

# ## Option : 2
# import boto3
# client = boto3.client('3s', region_name="us-east-1")



# ## Otion : 3
# session = boto3.session.Session(profile_name='default')
# client = session.client('secretsmanager', region_name='us-east-1')