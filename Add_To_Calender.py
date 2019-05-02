from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import ast


# our scopes for authentication at google services
SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/drive']


# a function for sending events to the calender, where you only have the data
# probably just used for testing purpose in the project
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
# else it returns None
def get_string_from_file(service_drive):
    results = service_drive.files().list(
        fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('There were no items in the specified google drive')
        return None
    else:
        for item in items:
            if item['name'] == 'test.json':
                body = service_drive.files().get_media(fileId=item['id']).execute()
                service_drive.files().delete(fileId=item['id']).execute()
                return ast.literal_eval(body.decode("utf-8").replace('"', "'"))
        print('There were no test.json in the specified google drive')
        return None


# a method, which gets all entrys from the specified google drive account since the 1st of january
def get_all_events(service_calender):
    jan_2018 = datetime.datetime(2018, 1, 1, 0, 0, 0, 0, tzinfo=None,
                                 fold=0).isoformat() + 'Z'  # 'Z' indicates UTC time
    events_result = service_calender.events().list(calendarId='primary', timeMin=jan_2018,
                                                   maxResults=10000, singleEvents=True,
                                                   orderBy='startTime').execute()
    events = events_result.get('items', [])
    return events


# searches for the older version of the same event and deletes it, in the case it finds it
def delete_event_already_exists(event, service_calender):
    if event is not None:
        events = get_all_events(service_calender)
        for existing_event in events:
            if existing_event['summary'] == event['summary']:
                print('same summary')
                print(event['start']['dateTime'])
                print(existing_event['start']['dateTime'])
                if existing_event['start']['dateTime'] == event['start']['dateTime']:
                    if existing_event['end']['dateTime'] == event['end']['dateTime']:
                        print('same time data')
                        if existing_event['attendees'][0]['email'] == event['attendees'][0]['email']:
                            print('same email')
                            service_calender.events().delete(calendarId='primary', eventId=existing_event['id']).execute()
                            print('deleted an event from the calendar')


# a function, which encapsulates the complete logic of the getting the information from google drive
# and writing it into a google calender
def process_event():
    service_calender = get_google_calender_service()
    service_drive = get_google_drive_service()
    event = get_string_from_file(service_drive)
    if event is not None:
        delete_event_already_exists(event, service_calender)
        service_calender.events().insert(calendarId='primary', body=event).execute()
        print('event added successfully to the calendar')


def main():
    process_event()


if __name__ == '__main__':
    main()