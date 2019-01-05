import os
from json import loads, dumps

import sentry_sdk

from active_users import get_active_users_number


def handler(event, context):
  view_id = os.environ.get('VIEW_ID')
  try:
    active_users_number = get_active_users_number(view_id)
    return {
      'statusCode': 200,
      'body': dumps({
        'activeUsersNumber': active_users_number
      }),
      'headers' : {
        'Access-Control-Allow-Origin' : '*'
      }
    }
  except Exception as e:
    sentry_sdk.init(os.environ.get('SENTRY_KEY'))
    sentry_sdk.capture_exception(e)
    return {
      'statusCode': 500,
      'body': dumps({
        'error': 'Fail to fetch data from google analytics'
      })
    }

