import logging as logger

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


class GCalendar:
    def __init__(self, cal_id='primary', timezone='Asia/Seoul'):
        self.cal_id = cal_id
        self.timezone = timezone

        # rw calendar
        scope = 'https://www.googleapis.com/auth/calendar'
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', scope)
            creds = tools.run_flow(flow, store)
        self.service = build('calendar', 'v3', http=creds.authorize(Http()))

    def event_exists(self, event_id):
        service = self.service
        query = '{}={}'.format('event_id', event_id)
        event = service.events().list(calendarId=self.cal_id,
                                      privateExtendedProperty=query).execute()
        if len(event['items']) == 0:
            return False
        return True

    def create_event(self, event_id, title, location, description, start_dt, end_dt):
        if event_id is None or title is None or location is None or \
                description is None or start_dt is None or end_dt is None:
            logger.warning("Incomplete data. Skipping event...")
            return

        event = {
            'summary': title,
            'location': location,
            'description': description,
            'start': {
                'dateTime': start_dt.strftime('%Y-%m-%dT%H:%M:%S'),
                'timeZone': self.timezone,
            },
            'end': {
                'dateTime': end_dt.strftime('%Y-%m-%dT%H:%M:%S'),
                'timeZone': self.timezone,
            },
            'extendedProperties': {
                'private': {
                    'event_id': event_id
                }
            }
        }

        service = self.service
        event = service.events().insert(calendarId=self.cal_id,
                                        body=event).execute()
        logger.warning('Event created: %s' % (event.get('htmlLink')))
