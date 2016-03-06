"""
:functions for answers for source.main.interface
============================================
Last Modified       Author             Summary
1/25/2016           Paul Ivanov        Init

The following code are the implementations for some of the functions
used in interface object made in main.py
"""
# It says I am redifing pow, but I am using the built-in pow function
# pylint: disable=W0622
import datetime
from math import pow, fmod, floor, pi
import getpass


def get_datetime():
    """
    retrieves the current date and time

    :returns: current time and date
    :rtype: string
    """
    time = datetime.datetime.now()
    time = time.replace(second=0, microsecond=0)
    return str(time)


def get_fibonacci(n_digit='c'):
    """
    retrieves the nth digit of the fibonacci sequence

    :param n_digit: the nth number wished for
    :type  n_digit: int

    :returns: A string if an error is found, or an int if the number is found
    :rtype: string
    """
    if n_digit == 'c':
        return "no parameter given in get_fibonacci"

    if n_digit < 0:
        return 'invalid'

    n_digit = floor(n_digit)
    if n_digit < 2:
        return n_digit
    return get_fibonacci(n_digit-2) + get_fibonacci(n_digit-1)


def get_pi_digit(n_digit=0):
    """
    retrieves the nth digit of the fibonacci sequence

    :param n_digit: the nth number wished for
    :type  n_digit: int

    :returns: A string if an error is found, or an int if the number is found
    :rtype: string
    """
    if n_digit <= 0:
        return 'invalid'

    n_digit = floor(n_digit-1)
    n_digit = floor(pi * pow(10, n_digit))
    n_digit = fmod(n_digit, 10)
    return n_digit


def open_door():
    """
    Says a smart-ass remark after being called.

    :returns: a string that says they cant do that and concats the current user's
    name
    :rtype: string
    """
    user = getpass.getuser()
    result = ("I'm afraid I can't do that " + user)
    return result


def convert_num(num=0, type1='cm', type2='cm'):
    """
    converts a unit of measurement from unit1 to unit2

    :param num: number wished to convert
    :type  num: int or double

    :param type1: current unit of measurement
    :type  type1: string

    :param type1: Wanted unit of measurement
    :type  type1: string

    :returns: new converted number
    :rtype: double
    """
    conversion_table = \
        {
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
    """
    Replies with a remark to the user

    :returns: It will reply with a kind hello with the current users name
    :rtype: string1
    """
    user = getpass.getuser()
    result = ("Hello, I am " + user + "'s guide.")
    return result


def answer_to_universe():
    """
    Function that returns the answer to universe

    :returns: 42
    :rtype: int
    """
    return 42


def adder(num1='a', num2='a'):
    """
    Function that returns the sum of two numbers

    :param num1: first number
    :type  num1: int or double

    :param num2: second number
    :type  num2: int or double

    :returns: sum of both numbers
    :rtype:   int or float
    """
    if not isinstance(num1, (int, float)):
        return 'invalid'

    if not isinstance(num2, (int, float)):
        return 'invalid'

    return num1 + num2


def subtractor(num1='a', num2='a'):
    """
    Function that returns the difference of two numbers

    :param num1: first number
    :type  num1: int or double

    :param num2: second number
    :type  num2: int or double

    :returns: difference of both numbers
    :rtype:   int or float
    """
    if not isinstance(num1, (int, float)):
        return 'invalid'

    if not isinstance(num2, (int, float)):
        return 'invalid'

    return num1 - num2


def divider(num1='a', num2='a'):
    """
    Function that returns the divisor of two numbers

    :param num1: first number
    :type  num1: int or double

    :param num2: second number
    :type  num2: int or double

    :returns: divisor of both numbers
    :rtype:   int or float
    """
    if not isinstance(num1, (int, float)):
        return 'invalid'

    if not isinstance(num2, (int, float)):
        return 'invalid'

    if num2 == 0:
        return "Can't divide by zero"

    return num1/num2


def multiplier(num1='a', num2='a'):
    """
    Function that returns the product of two numbers

    :param num1: first number
    :type  num1: int or double

    :param num2: second number
    :type  num2: int or double

    :returns: product of both numbers
    :rtype:   int or float
    """
    if not isinstance(num1, (int, float)):
        return 'invalid'

    if not isinstance(num2, (int, float)):
        return 'invalid'

    return num1 * num2


def get_mod(quotient='a', divisor='a'):
    """
    Function that returns the product of two numbers

    :param quotient: The number that will be modulated
    :type  quotient: int or double

    :param divisor: Clock size
    :type  divisor: int or double

    :returns: modulated number
    :rtype:   int
    """
    if not isinstance(quotient, (int, float)):
        return 'invalid'

    if not isinstance(divisor, (int, float)):
        return 'invalid'

    return quotient % divisor


def get_emotion():
    """
    Function that returns the systems current emotional state

    :returns: string that describes a student's current emotion
    :rtype:   str
    """
    return "Unstable"


def get_name():
    """
    Function that returns the systems current name

    :returns: current name of system
    :rtype:   str
    """
    return "Juan"





