from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


# a upload script for google drive, only used by RabbitMq for uploading messages from campus virtual to google drive
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
    file1.Upload()