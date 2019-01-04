import requests
import json
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'client_secrets.json'
VIEW_ID = '187148380'

credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)

session = requests.Session()
session.headers= { 'Authorization': 'Bearer ' + credentials.get_access_token().access_token }

url_kwargs = {
    'view_id': VIEW_ID,
    'get_args': 'metrics=rt:activeUsers'
}
response = session.get('https://www.googleapis.com/analytics/v3/data/realtime?ids=ga:{view_id}&{get_args}'.format(**url_kwargs))
if response:
    result = response.json()
    active_users = result['totalsForAllResults']['rt:activeUsers']