# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import boto3
import botocore
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

#download file from s3
#BUCKET_NAME = input('Please enter bucket name')
#KEY = input('Enter file name with extension')

BUCKET_NAME = "testautomationayo"

KEY = "newTestFile.txt"

#destFile = input('please enter dest. file name with ext')
destFile = "testfile1.pdf"
connect_str = ""
KeyId = open("accessKeyID.txt", "r")
AWS_ACCESS_KEY_ID = KeyId.read()

secretKey = open("secretAccessKey.txt", "r")
AWS_PRIVATE_KEY = secretKey.read()
s3 = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_PRIVATE_KEY)
connnectString = open("connectionString.txt", "r" )
#connect_str = os.getenv('DefaultEndpointsProtocol=https;AccountName=cs2100320010df450ac;AccountKey=fOWNDW3JlaMljTS9wEaJb7tUTbfBJqqAnb41vOAiFMAAXCBWP8WiGODR4Y9EJewjI229FOlYxzar2hsLI8c7YA==;EndpointSuffix=core.windows.net')
connect_str = connnectString.readline()


blob_service_client = BlobServiceClient.from_connection_string(connect_str)

#service = BlobServiceClient(account_url="https://<my-storage-account-name>.blob.core.windows.net/", credential=credential)
import os

try:
    file = s3.Object(BUCKET_NAME, KEY)
    body = file.get()['Body'].read()
    #s3.Bucket(BUCKET_NAME).download_file(KEY, destFile)
    azure_container_client = blob_service_client.get_container_client(container="testcontainer")
    azure_container_client.upload_blob(name=KEY, data=body, overwrite=True)
    #print(body)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code']== "404":
        print("The object does not exist.")
    else:
        raise
