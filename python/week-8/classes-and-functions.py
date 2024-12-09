class Time: 
    """represents the time of day. attributes: hour, minute, second"""

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def print_time(timeobj):
    print(f"{timeobj.hour}:{timeobj.minute}:{timeobj.second}")

print_time(time)

def is_after(t1, t2):
    total_t1 = (t1.hour * 60 * 60) + (t1.minute * 60) + t1.second
    total_t2 = (t2.hour * 60 * 60) + (t2.minute * 60) + t2.second
    return total_t1 > total_t2


def add_time(t1, t2): 
    sum = Time() 
    sum.hour = t1.hour + t2.hour 
    sum.minute = t1.minute + t2.minute 
    sum.second = t1.second + t2.second 
    return sum