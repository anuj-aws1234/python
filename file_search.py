import os
import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAIQSV6PYW3VGTIBTA'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'testingbucket22'


path = 'C:/Users/admin/Desktop'

files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))

for k in files:
    file_stats = os.stat(k)
    if int(f'{file_stats.st_size}') < 51200:
        print(k)




