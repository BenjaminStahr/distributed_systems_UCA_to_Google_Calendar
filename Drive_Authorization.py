from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def upload_file_to_drive(file_content):
    google_authorization = GoogleAuth()
    google_authorization.LoadCredentialsFile("mycreds.txt")

    if google_authorization.credentials is None:
        # Authenticate if they're not there
        google_authorization.LocalWebserverAuth()
    elif google_authorization.access_token_expired:
        # Refresh them if expired
        google_authorization.Refresh()
    else:
        # Initialize the saved creds
        google_authorization.Authorize()

    # Save the current credentials to a file
    google_authorization.SaveCredentialsFile("mycreds.txt")

    drive = GoogleDrive(google_authorization)

    file1 = drive.CreateFile({'title': 'test.json'})
    file1.SetContentString(file_content)
    '''file1.SetContentString(json.dumps(
        {
            "summary": "tarea para SD!!!",
            "description": "A chance to hear more about Googles developer products.",
            "start": {
                "dateTime": "2019-04-28T12:00:00+02:00",
                "timeZone": "Europe/Madrid"
            },
            "end": {
                "dateTime": "2019-04-28T13:00:00+02:00",
                "timeZone": "Europe/Madrid"
            },
            "attendees": [
                {"email": "johntitorium@gmail.com"}
            ]
        }))'''
    file1.Upload()