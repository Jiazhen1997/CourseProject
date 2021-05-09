
from datetime import datetime
import pytz

__author__ = 'Daniel'


class TimeParser():
    dt_formats = [
        '%Y-%m-%d %H:%M:%S %Z',  
        '%Y-%m-%d %H:%M:%S',     
    ]

    def parse(self, dt_str, dt_format):
        return datetime.strptime(dt_str, dt_format)


def localtime(utc_dt, tz_str):
    
    tz = pytz.timezone(tz_str)
    local_dt = tz.normalize(utc_dt.astimezone(tz))
    return local_dt


def utctime(dt, tz_str):
    
    tz = pytz.timezone(tz_str)
    local_dt = tz.localize(dt)
    utc_dt = pytz.utc.normalize(local_dt.astimezone(pytz.utc))
    return utc_dt
