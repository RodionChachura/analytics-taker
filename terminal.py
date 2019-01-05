import json

from active_users import get_active_users_number

KEY_FILE_LOCATION = 'client_secrets.json'
VIEW_ID = '187148380'

with open(KEY_FILE_LOCATION) as f:
  keyfile_dict = json.load(f)
active_users_number = get_active_users_number(VIEW_ID, keyfile_dict)
print('active users number: {0}'.format(active_users_number))

