"""
:mod:`source.source1` -- Example source code
============================================
Last Modified       Author             Summary
??/??/????          Joshua Kimball     Init
1/12/2016           Paul Ivanov        Added Quadrilateral functions

The following example code determines if a set of 3 sides of a triangle is
equilateral, scalene or iscoceles
"""
# R0913 disable because the function needs to take in 4 sides and 4 angles and was not specified
#   to create a list for the parameters
# pylint: disable=R0913

# pylint: disable=R0916

def get_triangle_type(side_a=0, side_b=0, side_c=0):
    """
    Determine if the given triangle is equilateral, scalene or Isosceles

    :param side_a: line a
    :type side_a: float or int or tuple or list or dict

    :param side_b: line b
    :type side_b: float

    :param side_c: line c
    :type side_c: float

    :return: "equilateral", "isosceles", "scalene" or "invalid"
    :rtype: str
    """
    if isinstance(side_a, (tuple, list)) and len(side_a) == 3:
        side_c = side_a[2]
        side_b = side_a[1]
        side_a = side_a[0]

    # side_a will occasionally be a dict based on requirements
    if isinstance(side_a, dict) and len(side_a.keys()) == 3:  # pylint: disable=E1101
        values = []
        for value in side_a.values(): # pylint: disable=E1101
            values.append(value)
        side_a = values[0]
        side_b = values[1]
        side_c = values[2]

    if not (isinstance(side_a, (int, float)) and isinstance(side_b, (int, float)) and
            isinstance(side_c, (int, float))):
        return "invalid"

    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return "invalid"

    if side_a == side_b and side_b == side_c:
        return "equilateral"

    elif side_a == side_b or side_a == side_c or side_b == side_c:
        return "isosceles"
    else:
        return "scalene"


def get_rectangle_type(side_a=0, side_b=0, side_c=0, side_d=0):
    """
    Determine if the given parameters define a square or a circle

    :param side_a: line a
    :type side_a: float, int

    :param side_b: line b
    :type side_b: float, int

    :param side_c: line c
    :type side_c: float, int

    :param side_d: line d
    :type side_d: float, int

    :return: "square", "rectangle" or "invalid"
    :rtype: str
    """

    if not (isinstance(side_a, (int, float)) and isinstance(side_b, (int, float)) and
            isinstance(side_c, (int, float)) and isinstance(side_d, (int, float))):
        return "invalid"

    if side_a <= 0 or side_b <= 0 or side_c <= 0 or side_d <= 0:
        return "invalid"

    if side_a == side_b and side_b == side_c and side_c == side_d:
        return "square"

    # disabled this because I needed to check for the certain combination of sides
    # pylint: disable=R0916
    elif (side_a == side_b and side_c == side_d or side_a == side_c and
          side_b == side_d or side_a == side_d and side_b == side_c):  # pylint: disable=R0916
        return "rectangle"

    else:
        return "invalid"


def get_quadrilateral_type(side1=0, side2=0, side3=0, side4=0, angle1=0,
                           angle2=0, angle3=0, angle4=0):
    """
    Determine if the given parameters define a quadrilateral type shape

    :param side1: line a
    :type side1: float, int

    :param side2: line b
    :type side2: float, int

    :param side3: line c
    :type side3: float, int

    :param side4: line d
    :type side4: float, int

    :param angle1: line angle_a
    :type angle1: float, int

    :param angle2: line angle_b
    :type angle2: float, int

    :param angle3: line angle_c
    :type angle3: float, int

    :param angle4: line angle_d
    :type angle4: float, int

    :return: "square", "rectangle", "rhombus", "invalid" or "disconnected"
    :rtype: str
    """

    if not (isinstance(side1, (int, float)) and isinstance(side2, (int, float)) and
            isinstance(side3, (int, float)) and isinstance(side4, (int, float))):
        return "invalid"

    if not (isinstance(angle1, (int, float)) and isinstance(angle2, (int, float)) and
            isinstance(angle3, (int, float)) and isinstance(angle4, (int, float))):
        return "invalid"

    # Checks if anything is 0, none should ever be
    # pylint: disable=R0916
    if (side1 <= 0 or side2 <= 0 or side3 <= 0 or side4 <= 0 or
            angle1 <= 0 or angle2 <= 0 or angle3 <= 0 or angle4 <= 0):  # pylint: disable=R0916
        return "invalid"

    if (angle1 == 90) and (angle2 == 90) and (angle3 == 90) and (angle4 == 90):
        return get_rectangle_type(side1, side2, side3, side4)

    else:
        if angle1 + angle2 + angle3 + angle4 == 360:
            return "rhombus"
        else:
            return "disconnected"
