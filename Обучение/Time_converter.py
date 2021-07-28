def time_to_float(t):
    t = t.split(":")
    h = int(t[0])
    m = t[-1]
    m = int(m) / 60
    tf = h + m
    return tf



def float_to_time(x):
    x = str(x)
    x = x.split(".")
    m = "0." + x[-1]
    m = float(m)
    m = m * 60
    h = x[0]
    hm = f"{h}:{int(m)}"
    return hm

time = time_to_float("6:52") + time_to_float("0:08") + (time_to_float("0:07") * 3) + time_to_float("0:08")
time = float_to_time(time)
print(time)