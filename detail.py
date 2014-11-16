#!/usr/bin/python

# Do not remove
GOOGLE_LOGIN = GOOGLE_PASSWORD = AUTH_TOKEN = None

import sys
from pprint import pprint

from config import *
from googleplay import GooglePlayAPI
from helpers import sizeof_fmt, print_header_line, print_result_line, print_result_json

if (len(sys.argv) < 2):
    print "Usage: %s packageName" % sys.argv[0]
    print "Details for an app."
    sys.exit(0)

packageName = sys.argv[1]

api = GooglePlayAPI(ANDROID_ID)
api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD, AUTH_TOKEN)

try:
    message = api.details(packageName)
except:
    print "Error: something went wrong."
    sys.exit(1)

print_result_json(message.docV2)
