import human_readable
import datetime as dt


def format_duration(seconds):
    delta = dt.timedelta(seconds=seconds)
    return human_readable.precise_delta(delta)

