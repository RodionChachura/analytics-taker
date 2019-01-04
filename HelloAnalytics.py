"""Hello Analytics Reporting API V4."""

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'client_secrets.json'
VIEW_ID = '187148380'

def main():
  credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)
  analytics = build('analyticsreporting', 'v4', credentials=credentials)
  response = analytics.reports().batchGet(
      body={
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
          'metrics': [{'expression': 'ga:sessions'}],
          'dimensions': [{'name': 'ga:country'}]
        }]
      }
  ).execute()
  print(response)
  # for report in response.get('reports', []):
  #   columnHeader = report.get('columnHeader', {})
  #   dimensionHeaders = columnHeader.get('dimensions', [])
  #   metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])

  #   for row in report.get('data', {}).get('rows', []):
  #     dimensions = row.get('dimensions', [])
  #     dateRangeValues = row.get('metrics', [])

  #     for header, dimension in zip(dimensionHeaders, dimensions):
  #       print(header + ': ' + dimension)

  #     for i, values in enumerate(dateRangeValues):
  #       print('Date range: ' + str(i))
  #       for metricHeader, value in zip(metricHeaders, values.get('values')):
  #         print(metricHeader.get('name') + ': ' + value)

if __name__ == '__main__':
  main()

