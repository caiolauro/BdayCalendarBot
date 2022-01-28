# Birthdays WhatsApp Bot

## Project description

This project sends you reminders to not forget Birthday dates of people you love.

### Project Expansion
Imagine you can schedule an entire Gcalendar event using WhatsApp. Informing name, event date and time, description and even invitations. 

### Technologies applied

It makes use of Google Calendar API in order to pull the special dates information.  
The date information gets compared by the current date. If '''special_date == current_date''' then the python application acctionate Selenium Web Driver to send a reminder in WhatsApp. The WhatsApp message destiny could be a group that you create only for you or even a close person you wanna share those special dates.

#### References:
https://karenapp.io/articles/how-to-automate-google-calendar-with-python-using-the-calendar-api/