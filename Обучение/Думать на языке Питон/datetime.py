import datetime


class Time(object):
    '''Текст'''


time1 = Time()

time1.hour = 11
time1.minute = 1
time1.second = 29

time2 = Time()

time2.hour = 11
time2.minute = 1
time2.second = 30


def print_time(t):
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))


def is_after(t1, t2):
    tt1 = '%.2d:%.2d:%.2d' % (t1.hour, t1.minute, t1.second)
    tt2 = '%.2d:%.2d:%.2d' % (t2.hour, t2.minute, t2.second)
    print(tt1 > tt2)


def add_time1(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


test_time = Time()
test_time.hour = 1
test_time.minute = 0
test_time.second = 0

test_time2 = Time()
test_time2.hour = 1
test_time2.minute = 0
test_time2.second = 0


def increment(time, seconds):
    secs = time_to_int(time) + seconds
    res = int_to_time(secs)
    return '%.2d:%.2d:%.2d' % (res.hour, res.minute, res.second)


def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def add_time(t1, t2):
    assert valid_time(t1) and valid_time(t2), 'Неверное время'
    seconds = time_to_int(t1) + time_to_int(t2)
    res = int_to_time(seconds)
    return '%.2d:%.2d:%.2d' % (res.hour, res.minute, res.second)


def mul_time(time, mult):
    res = int_to_time(time_to_int(time) * mult)
    return '%.2d:%.2d:%.2d' % (res.hour, res.minute, res.second)


def time_to_km(time, km):
    seconds = time_to_int(time)
    km_per_sec = km / seconds
    seconds_to_1km_needed = 1 / km_per_sec
    res = int_to_time(seconds_to_1km_needed)
    print('%.2d:%.2d:%.2d' % (res.hour, res.minute, res.second))


time_race = Time()
time_race.hour = 1
time_race.minute = 0
time_race.second = 0

distance = 6



