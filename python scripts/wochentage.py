from datetime import datetime

# Create datetime object
date='2019-01-01'

# Define a list of weekday names
days = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']

#string to date type
date = datetime.strptime(date, '%Y-%m-%d')

# Index using weekday int value
weekday = days[date.weekday()]


print(weekday)