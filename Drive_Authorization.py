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
#SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/drive']

def get_google_drive_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    drive_service = build('drive', 'v3', credentials=creds)
    return drive_service


# a upload script for google drive, only used by RabbitMq for uploading messages from campus virtual to google drive
def upload_file_to_drive(file_content):
    drive = get_google_drive_service()
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

