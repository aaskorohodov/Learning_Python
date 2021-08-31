def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __lt__(self, other):
        '''<'''
        t1 = self.hour, self.minute, self.second
        t2 = other.hour, other.minute, other.second
        return t1 < t2

    def __gt__(self, other):
        '''>'''
        t1 = self.hour, self.minute, self.second
        t2 = other.hour, other.minute, other.second
        return t1 > t2

    def __eq__(self, other):
        '''=='''
        t1 = self.hour, self.minute, self.second
        t2 = other.hour, other.minute, other.second
        return t1 == t2

time = Time(0, 1, 0)
time1 = Time(0, 1, 0)

print(time == time1)

# print(time + time1)



class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_x_y(self):
        print(self.x, self.y)

    def __str__(self):
        return f'[{self.x} {self.y}]'

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_points(other)
        else:
            return self.add_point_tuple(other)

    def add_points(self, other):
        res = Point()
        res.x = self.x + other.x
        res.y = self.y + other.y
        return res

    def add_point_tuple(self, other):
        res = Point()
        res.x = self.x + other[0]
        res.y = self.y + other[1]
        return res

    def __radd__(self, other):
        return self.__add__(other)

a = Point(1, 1)
b = Point(1, 4)
c = (10, 20)

#print(Point.add_point_tuple(a, c))

def print_attributes(obj):
    for attr in obj.__dict__:
        print (attr, getattr(obj, attr))


#print_attributes(a)