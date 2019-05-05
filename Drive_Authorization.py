from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import Add_To_Calender

import json
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload
import os
import time
# our scopes for authentication at google services
SCOPES = ['https://www.googleapis.com/auth/drive']

# a upload script for google drive, only used by RabbitMq for uploading messages from campus virtual to google drive
def upload_file_to_drive(file_content):
    drive = Add_To_Calender.get_google_drive_service()
    text_file = open("text.txt", "w")
    text_file.write(file_content)
    text_file.close()
    file_metadata = {'name': 'test.json'}
    media = MediaFileUpload("text.txt",
                            mimetype='application/json')
    drive.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
    time.sleep(1)

