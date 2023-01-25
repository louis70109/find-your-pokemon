import pytz
from pytz import timezone

tpe_tz = timezone('Asia/Taipei')


def utc_to_tpe(d):
    """
    Convert UTC datetime to TPE datetime (with timezone info)
    """
    return pytz.utc.localize(d).astimezone(tpe_tz)


def tpe_to_utc_str(d):
    """
    Convert TPE datetime to UTC datetime
    """
    return tpe_tz.localize(d).astimezone(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')