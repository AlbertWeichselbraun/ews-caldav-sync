#!/usr/bin/env python3

from exchangelib import Credentials, Account, Configuration
from exchangelib.credentials import DELEGATE
from os import getenv
from pickle import dump

user = getenv('EWS_USER')
email = getenv('EWS_EMAIL')
pwd  = getenv('EWS_PASS')
server = getenv('EWS_SERVER')

server = 'owa.fh-htwchur.ch'

credentials = Credentials('edu03\\weichsalbert', pwd)
config = Configuration(service_endpoint='https://owa.fh-htwchur.ch/EWS/Exchange.asmx', credentials=credentials)
account = Account(primary_smtp_address=email, config=config, access_type=DELEGATE)

for no, item in enumerate(account.calendar.all()[:10]):
    with open("cal-"+str(no)+".pickle", "wb") as f:
       dump(item, f)

