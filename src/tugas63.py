from datetime import datetime

date_string = "08 Jun 2002 06:00AM"

date = datetime.strptime(date_string, '%d %b %Y %I:%M%p')

print(type(date))
print(date)