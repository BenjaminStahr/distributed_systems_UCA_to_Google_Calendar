from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


'''def authorize_drive():
    google_authorization = GoogleAuth()
    google_authorization.DEFAULT_SETTINGS['client_config_file'] = "client_secret.json"
    google_authorization.LoadCredentialsFile("mycreds.txt")
    return GoogleDrive(google_authorization)'''


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

file1 = drive.CreateFile({'title': 'Hello.txt'})
file1.SetContentString('Hello World!') # Set content of the file from given string.
file1.Upload()
