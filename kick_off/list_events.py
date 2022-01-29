import datetime
from cal_setup import get_calendar_service
event_list = []
def get_events_list():
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.datetime.now().isoformat() + 'Z' # 'Z' indicates UTC time
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
            event_list.append(dict(date = start[0:10], name =  event['summary']))
    Events22 = dict(eventsList=event_list,today_ts=now)
    #print(Events22)
    return Events22



def get_today_events():
    message:str = '---->> Today Events <<----\n'
    
    events = get_events_list()['eventsList']
    today = datetime.datetime.now().isoformat()[0:10] # 'Z' indicates UTC time
    print(today)
    for event in events:
        if event['date'] ==  today:
            print(event['name'])
            event = '- ' + event['name'] + '\n'
            message = message + '\n' + event

    return message