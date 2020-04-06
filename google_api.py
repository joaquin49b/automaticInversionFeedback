from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class GoogleApi:

    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


    def __init__(self):
        self.auth()


    def auth(self):
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
                    'credentials_google.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)


    def update_sheet(self):
        service = self.service

        spreadsheet_id = '1Ab_xhYiDHsBS6JuuwxqdNLitjz_DbcSxFeT7pIBAJJk'
        ranges = []
        include_grid_data = True

        request = service.spreadsheets().get(spreadsheetId=spreadsheet_id,
                                             ranges=ranges, includeGridData=include_grid_data)
        response = request.execute()

        print(response)
