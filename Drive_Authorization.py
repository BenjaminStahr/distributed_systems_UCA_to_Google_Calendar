import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
import time

SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/drive']


def get_google_drive_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            print("Loaded credentials from token.pickle")

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
                print("Credentials refreshed")
            except Exception as e:
                print(f"Failed to refresh credentials: {e}")
        else:
            try:
                flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
                creds = flow.run_local_server(port=0)
                print("Obtained new credentials")
            except Exception as e:
                print(f"Failed to obtain new credentials: {e}")
                return None

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
            print("Saved credentials to token.pickle")
    try:
        drive_service = build('drive', 'v3', credentials=creds)
        print("Google Drive service created successfully")
        return drive_service
    except Exception as e:
        print(f"Failed to create Google Drive service: {e}")
        return None


# A script to upload file content to Google Drive
def upload_file_to_drive(file_content):
    drive = get_google_drive_service()
    if not drive:
        print("Failed to get Google Drive service")
        return

    try:
        text_file_path = "text.txt"
        with open(text_file_path, "w") as text_file:
            text_file.write(file_content)

        file_metadata = {'name': 'test.json'}
        media = MediaFileUpload(text_file_path, mimetype='text/plain')
        file = drive.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f"File uploaded successfully, file ID: {file.get('id')}")

        time.sleep(1)
    except Exception as e:
        print(f"Failed to upload file: {e}")