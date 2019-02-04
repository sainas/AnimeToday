import pytz
import datetime

def bostondate():
    date_format = '%Y-%m-%d'
    date_utc = datetime.datetime.now(tz=pytz.utc)
    date_est = date_utc.astimezone(pytz.timezone('US/Pacific')).strftime(date_format)
    return date_est