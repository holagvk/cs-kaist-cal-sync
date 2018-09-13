from csweb import CSWeb
from gcalendar import GCalendar


if __name__ == '__main__':
    web = CSWeb()
    cal = GCalendar('2mg4vsjdeejg8clpd7gvs5iudk@group.calendar.google.com')

    # fetch events from CS web
    event_ids = web.get_event_ids(refresh=True)
    for _id in event_ids:
        # exist in calendar?
        if not cal.event_exists('{}:{}'.format('CS', _id)):
            # fetch details from CS web
            event_details = web.get_event_details(_id)

            # insert in calendar
            cal.create_event('{}:{}'.format('CS', _id),
                             *event_details)
