import time
import datetime
from datetime import timedelta

time_tuple = time.strptime("2023-04-07", '%Y-%m-%d')
year, month, day = time_tuple[:3]
now = datetime.date(year, month, day)

this_month_start = datetime.datetime(now.year, now.month, 1).date()
this_month_end = (datetime.datetime(now.year, now.month + 1, 1) - timedelta(days=1)).date()
last_month_end = this_month_start - timedelta(days=1)
last_month_start = datetime.datetime(last_month_end.year, last_month_end.month, 1).date()
this_week_start = now - timedelta(days=now.weekday())
this_week_end = now + timedelta(days=6 - now.weekday())
last_week_start = now - timedelta(days=now.weekday() + 7)
last_week_end = now - timedelta(days=now.weekday() + 1)

left_day = now - timedelta(days=15)
time_tuple = time.strptime("2023-04-11", '%Y-%m-%d')
year, month, day = time_tuple[:3]
now = datetime.date(year, month, day)
right_day = now + timedelta(days=15)
print(this_week_end)
print(right_day)

import re

sentence = '点击个商品'
s1 = re.findall(r'-?\d+\.?\d*', sentence)
print(s1)
# s = int(re.findall(r'-?\d+\.?\d*', sentence)[0])
# print(s1)
