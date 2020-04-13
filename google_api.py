import pickle
import os.path
import calendar
from datetime import date
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

        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials_google.json', self.SCOPES)
                creds = flow.run_local_server(port=0)

            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        self.service = build('sheets', 'v4', credentials=creds)

    def update_sheet(self, spreadsheet_id, range_, value_range_body):
        service = self.service
        request = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=range_,
            valueInputOption='RAW',
            includeValuesInResponse=True,
            body=value_range_body)

        request.execute()

    def save(self, amount_calculate, spreadsheet_id, range_):

        today = date.today()
        month = format(today.month + 1)

        sheet_range = range_ + 'C' + month
        values = {"values": [[amount_calculate]]}

        self.update_sheet(spreadsheet_id, sheet_range, values)

        last_day_of_month = calendar.monthrange(today.year, today.month)[1]

        if last_day_of_month == last_day_of_month:
            month = format(today.month + 2)
            sheet_range = range_ + 'B' + month

            self.update_sheet(spreadsheet_id, sheet_range, values)
