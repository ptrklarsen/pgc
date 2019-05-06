from datetime import *

raw_today = date.today()
today = raw_today.strftime("%y%m%d")
raw_yesterday = raw_today - timedelta(days=1)
yesterday = raw_yesterday.strftime("%y%m%d")