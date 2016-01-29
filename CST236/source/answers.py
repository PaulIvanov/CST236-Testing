"""
:functions for answers for source.main.interface
============================================
Last Modified       Author             Summary
1/25/2016           Paul Ivanov        Init

The following code are the implementations for some of the functions used in interface object made in main.py
"""

import datetime
import math
from math import pow, fmod, floor, pi
import getpass


def get_datetime():
    time = datetime.datetime.now()
    time = time.replace(second=0, microsecond=0)
    return str(time)


def get_fibonacci(n='c'):
    if n == 'c':
        return "no parameter given in get_fibonacci"

    if not isinstance(n, (int, float)):
        return 'invalid'

    if n < 0:
        return 'invalid'

    n = math.floor(n)
    if n < 2:
        return n
    return get_fibonacci(n-2) + get_fibonacci(n-1)


def get_pi_digit(n=0):
    if n <= 0:
        return 'invalid'

    if not isinstance(n, (int, float)):
        return 'invalid'

    n = floor(n-1)
    n = floor(pi * pow(10, n))
    n = fmod(n, 10)
    return n


def open_door():
    user = getpass.getuser()
    result = ("I'm afraid I can't do that " + user)
    return result


def convert_num(num=0, type1='cm', type2='cm'):
    conversion_table = {
                            'km': 1000,
                            'm': 1,
                            'cm': 0.01,
                            'mm': 0.001,
                            'lbs': .454545454545454545454545,
                            'kg': 1,
                            'g': 0.001,
                            'mg': 0.0001,
                            'gallon': 1,
                            'quart': 0.25,
                            'pint': 0.125
                        }

    if type1 in list(['km', 'm', 'cm', 'mm']):
        if type2 not in list(['km', 'm', 'cm', 'mm']):
            return "invalid conversion"

    if type1 in list(['lbs', 'kg', 'g', 'mg']):
        if type2 not in list(['lbs', 'kg', 'g', 'mg']):
            return "invalid conversion"

    if type1 in list(['gallon', 'quart', 'pint']):
        if type2 not in list(['gallon', 'quart', 'pint']):
            return "invalid conversion"

    result = (num*conversion_table[type1])/conversion_table[type2]

    return result


def hello():
    user = getpass.getuser()
    result = ("Hello, I am " + user + "'s guide.")
    return result


def answer_to_universe():
    return 42


def adder(num1='a', num2='a'):
    if not isinstance(num1, (int, float)):
        return 'invalid'

    if not isinstance(num2, (int, float)):
        return 'invalid'

    return num1 + num2


def subtractor(num1='a', num2='a'):
    if not isinstance(num1, (int, float)):
        return 'invalid'

    if not isinstance(num2, (int, float)):
        return 'invalid'

    return num1 - num2


def get_emotion():
    return "Unstable"


def get_name():
    return "Juan"



