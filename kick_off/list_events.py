import datetime
from cal_setup import get_calendar_service
event_list = []
def get_events_list():
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting List of events')
    events_result = service.events().list(
        calendarId='primary', timeMin=now,
        singleEvents=True,
        orderBy='startTime',).execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        if start[0:4] == '2022':
            event_list.append(dict(date = start, name =  event['summary']))
    print(event_list)
    return event_list
get_events_list()