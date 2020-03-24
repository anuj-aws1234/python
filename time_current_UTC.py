import pytz
import datetime
from datetime import timedelta

country = 'Asia/Calcutta'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The Time in {} is {}".format(country, local_time))
print("UTC timing one hour back is {}".format(datetime.datetime.utcnow() - timedelta(hours = 1)))
