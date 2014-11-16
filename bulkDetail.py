#!/usr/bin/python

# Do not remove
GOOGLE_LOGIN = GOOGLE_PASSWORD = AUTH_TOKEN = None

import sys
from pprint import pprint

from config import *
from googleplay import GooglePlayAPI
from helpers import sizeof_fmt, print_header_line, print_result_line, print_result_json

if (len(sys.argv) < 2):
    print "Usage: %s packageName(;packageName)" % sys.argv[0]
    print "Details for an applications."
    sys.exit(0)

packageNames = sys.argv[1].split(";")

api = GooglePlayAPI(ANDROID_ID)
api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD, AUTH_TOKEN)

for packageName in packageNames:
    try:
        message = api.details(packageName)
    except:
        continue

    # print if nothing wrong
    print_result_json(message.docV2)
