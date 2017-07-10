#!/usr/bin/python
from datetime import datetime, timedelta


def Content_posting_Time(Addtime):
    ten_minutes_from_now = datetime.now() + timedelta(minutes=Addtime)
    hour_and_minute = '{:%H:%M}'.format(ten_minutes_from_now)
    e = datetime.strptime(hour_and_minute, "%H:%M").strftime("%I %M %p")
    d = e.split()
    return d


