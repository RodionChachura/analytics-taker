import json
import sys

from active_users import get_active_users_number

active_users_number = get_active_users_number(sys.argv[1])
print('active users number: {0}'.format(active_users_number))

