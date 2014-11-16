#!/usr/bin/python

# Do not remove
GOOGLE_LOGIN = GOOGLE_PASSWORD = AUTH_TOKEN = None

import sys
from pprint import pprint

from config import *
from googleplay import GooglePlayAPI
from helpers import sizeof_fmt, print_header_line, print_result_line, print_result_json

if (len(sys.argv) < 2):
    print "Usage: %s request [nb_results] [offset]" % sys.argv[0]
    print "Search for an app."
    print "If request contains a space, don't forget to surround it with \"\""
    sys.exit(0)

requests = sys.argv[1].split(";")
nb_res = None
offset = None

if (len(sys.argv) >= 3):
    nb_res = int(sys.argv[2])

if (len(sys.argv) >= 4):
    offset = int(sys.argv[3])

api = GooglePlayAPI(ANDROID_ID)
api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD, AUTH_TOKEN)

for request in requests:
    try:
        message = api.search(request, nb_res, offset)
    except:
        continue

    # print if nothing wrong
    if hasattr(message, "doc") and len(message.doc) > 0:
        doc = message.doc[0]
        for c in doc.child:
            print_result_json(c)
