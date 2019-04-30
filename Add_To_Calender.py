from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar.events', 'https://www.googleapis.com/auth/drive']

# TODO make this aviable for more countrys than just Spain
def get_event(summary, description, start_date, end_date, user):
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_date,
            'timeZone': 'Europe/Madrid',
        },
        'end': {
            'dateTime': end_date,
            'timeZone': 'Europe/Madrid',
        },
        'attendees': [
            {'email': user}
        ]
    }
    return event


def get_google_calender_service():
    # If modifying these scopes, delete the file token.pickle.

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
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

    service_calender = build('calendar', 'v3', credentials=creds)
    return service_calender

def get_google_drive_service():
    creds = None
    #SCOPES = ['https://www.googleapis.com/auth/drive']
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
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


def get_json_file(service_drive):
    # Call the Drive v3 API
    results = service_drive.files().list(
        fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))


def main():

    service_calender = get_google_calender_service()

    service_drive = get_google_drive_service()


    # to write an event into the calender you need to specify summary, description, start_date, end_date, user
    # this is just for testing usages
    summary = 'This is the summary'
    description = 'This is the description'
    start_date = datetime.datetime(2019, 4, 25, 14, 20, 0, 0, tzinfo=None, fold=0).isoformat()
    end_date = datetime.datetime(2019, 4, 25, 14, 40, 0, 0, tzinfo=None, fold=0).isoformat()
    print(end_date)
    user = 'johntitorium@gmail.com'

    event = get_event(summary, description, start_date, end_date, user)
    service_calender.events().insert(calendarId='primary', body=event).execute()


if __name__ == '__main__':
    main()