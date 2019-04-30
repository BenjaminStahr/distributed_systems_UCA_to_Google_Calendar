from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


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


def main():

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    '''now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
    
    event = {
        'summary': 'tarea para SD',
        'description': 'A chance to hear more about Google\'s developer products.',
        'start': {
            'dateTime': '2019-04-28T12:00:00+02:00',
            'timeZone': 'Europe/Madrid',
        },
        'end': {
            'dateTime': '2019-04-28T12:00:00+02:00',
            'timeZone': 'Europe/Madrid',
        },
        'attendees': [
            {'email': 'johntitorium@gmail.com'}
        ]
    }'''

    # to write an event into the calender you need to specify summary, description, start_date, end_date, user
    # this is just for testing usages
    summary = 'This is the summary'
    description = 'This is the description'
    start_date = datetime.datetime(2019, 4, 25, 14, 20, 0, 0, tzinfo=None, fold=0).isoformat()
    end_date = datetime.datetime(2019, 4, 25, 14, 40, 0, 0, tzinfo=None, fold=0).isoformat()
    print(end_date)
    user = 'johntitorium@gmail.com'

    event = get_event(summary, description, start_date, end_date, user)
    service.events().insert(calendarId='primary', body=event).execute()


if __name__ == '__main__':
    main()