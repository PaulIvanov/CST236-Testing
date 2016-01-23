import datetime
import math


def get_datetime():
    time = datetime.datetime.now()
    time = time.replace(second=0, microsecond=0)
    return str(time)


def get_fibonacci(n=1):
    if not isinstance(n, (int, float)):
        return 'invalid number'

    if n <= 0:
        return 'invalid number'

    n = math.floor(n)
    if n < 2:
        return n
    return get_fibonacci(n-2) + get_fibonacci(n-1)

