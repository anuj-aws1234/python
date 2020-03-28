from datetime import datetime
from pytz import timezone
tz = timezone('EST')
datetime.now(tz)

print (datetime.datetime.utcnow() - datetime.timedelta(hours=4)).strftime('%Y%m%d')
