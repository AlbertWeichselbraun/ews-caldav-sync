#!/usr/bin/env python3

'''
class for converting exchange calendar items to ical
'''

from icalendar import Calendar, Event

class ExchangeCalendarItem(object):

    def __init__(self, item):
        self.item = item

    def get_ical(self):
        event = Calendar()

        event['summary'] = self.item.subject
