from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import ast


# our scopes for authentification at google services
SCOPES = ['https://www.googleapis.com/auth/calendar.events', 'https://www.googleapis.com/auth/drive']


# TODO make this available for more countrys than just Spain
# a function for sending events to the calender, where you only have the data
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


# function for getting the calender service and login
def get_google_calender_service():
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


# a function for logging in to google drive and getting the remote drive service
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


# a function, which searches for a file named test.json in the google drive and returns a dict representation of this
# json, the name of the json we can change in the future
def get_string_from_file(service_drive):
    # Call the Drive v3 API
    results = service_drive.files().list(
        fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        for item in items:
            if item['name'] == 'test.json':
                body = service_drive.files().get_media(fileId=item['id']).execute()
                return ast.literal_eval(body.decode("utf-8").replace('"', "'"))


# setting up calender service and drive service and inserting two events into the calender
def main():

    service_calender = get_google_calender_service()
    service_drive = get_google_drive_service()
    text = get_string_from_file(service_drive)

    print(text)

    # to write an event into the calender you need to specify summary, description, start_date, end_date, user
    # this is just for testing usages
    summary = 'This is the summary, muh'
    description = 'This is the description'
    start_date = datetime.datetime(2019, 4, 25, 14, 20, 0, 0, tzinfo=None, fold=0).isoformat()
    end_date = datetime.datetime(2019, 4, 25, 14, 20, 0, 0, tzinfo=None, fold=0).isoformat()
    user = 'evfim1234@gmail.com'

    event = get_event(summary, description, start_date, end_date, user)
    service_calender.events().insert(calendarId='primary', body=event).execute()
    #service_calender.events().insert(calendarId='primary', body=text).execute()


if __name__ == '__main__':
    main()