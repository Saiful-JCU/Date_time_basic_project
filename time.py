import time
from datetime import datetime

times = time.strftime('%H:%M:%S')
print(times)

# Convert current time and comparison time to datetime objects
current_time = datetime.strptime(times, '%H:%M:%S')

morning = datetime.strptime('06:00:00', '%H:%M:%S')

noon_time = datetime.strptime('12:00:00', '%H:%M:%S')

evening = datetime.strptime('16:00:00', '%H:%M:%S')


night = datetime.strptime('19:00:00', '%H:%M:%S')

if current_time <= morning:
    print('Good morning')
elif current_time <= noon_time:
    print('Good Afternoon ')
elif current_time <= evening:
    print('Good Evening')
else:
    print('Good Night')