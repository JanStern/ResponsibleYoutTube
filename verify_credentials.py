from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set the scopes and client secrets file
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
CLIENT_SECRETS_FILE = 'credentials/desktop_client_cred.json'


def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build('youtube', 'v3', credentials=credentials)


def channels_list_by_username(service, **kwargs):
    results = service.channels().list(**kwargs).execute()
    print('This is a test API call:')
    print(results)


if __name__ == '__main__':
    # Disable OAuthlib's HTTP verification when running locally.
    # DO NOT leave this option enabled when running in production.
    import os

    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    service = get_authenticated_service()
    try:
        channels_list_by_username(service,
                                  part='snippet,contentDetails,statistics',
                                  forUsername='GoogleDevelopers')
    except HttpError as e:
        print(f'An HTTP error {e.resp.status} occurred:\n{e.content}')


    print("SUCCESS")
