# https://stackoverflow.com/questions/48416511/how-to-convert-utc-to-est-with-python-and-take-care-of-daylight-saving-automatic?noredirect=1&lq=1
# You'll need to use the pytz module (available from PyPI):

import pytz
from datetime import datetime

est = pytz.timezone('US/Eastern')
utc = pytz.utc
fmt = '%Y-%m-%d %H:%M:%S %Z%z'

winter = datetime(2016, 1, 24, 18, 0, 0, tzinfo=utc)
summer = datetime(2016, 7, 24, 18, 0, 0, tzinfo=utc)

print winter.strftime(fmt)
print summer.strftime(fmt)

print winter.astimezone(est).strftime(fmt)
print summer.astimezone(est).strftime(fmt)