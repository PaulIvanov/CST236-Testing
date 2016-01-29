"""
Test for source.shape_checker
Last Modified         Editor            Summary
??/??/????            Joshua Kimball    Init
1/12/2016             Paul Ivanov       Added TestGetQuadrilateralType Class
"""

from source.shape_checker import get_triangle_type
from source.shape_checker import get_quadrilateral_type
from source.main import Interface, NOT_A_QUESTION_RETURN, UNKNOWN_QUESTION, NO_QUESTION, NO_TEACH
from unittest import TestCase
from test.plugins.ReqTracer import requirements


class TestGetTriangleType(TestCase):

    # int tests
    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(1, 1, 2)
        self.assertEqual(result, 'isosceles')

    #float tests
    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_all_float(self):
        result = get_triangle_type(1.0, 1.0, 1.0)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_all_float(self):
        result = get_triangle_type(1.0, 3.0, 2.0)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_all_float(self):
        result = get_triangle_type(1.0, 1.0, 2.0)
        self.assertEqual(result, 'isosceles')

    #char tests
    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_all_char(self):
        result = get_triangle_type('a', 'b', 'c')
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_all_char(self):
        result = get_triangle_type('a', 'b', 'c')
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_all_char(self):
        result = get_triangle_type('g', 'x', 'c')
        self.assertEqual(result, 'invalid')

    #int/float combo tests
    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_int_float_combo(self):
        result = get_triangle_type(1, 1.0, 1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_int_float_combo(self):
        result = get_triangle_type(1.5, 3, 2.2)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_int_float_combo(self):
        result = get_triangle_type(1.5, 1.5, 2)
        self.assertEqual(result, 'isosceles')

    # tuple tests
    @requirements(['#0001'])
    def test_get_triangle_equilateral_tuple(self):
        tup1 = (1, 1, 1)
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001'])
    def test_get_triangle_scalene_tuple(self):
        tup1 = (1, 3, 5)
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001'])
    def test_get_triangle_isosceles_tuple(self):
        tup1 = (1, 1, 2)
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_invalid_tuple(self):
        tup1 = (1, 1, 1, 1)
        result = get_triangle_type(tup1)
        self.assertEqual(result, 'invalid')

    # list tests
    @requirements(['#0001'])
    def test_get_triangle_equilateral_list(self):
        list1 = (1, 1, 1)
        result = get_triangle_type(list1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001'])
    def test_get_triangle_scalene_list(self):
        list1 = (1, 3, 5)
        result = get_triangle_type(list1)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001'])
    def test_get_triangle_isosceles_list(self):
        list1 = (1, 1, 2)
        result = get_triangle_type(list1)
        self.assertEqual(result, 'isosceles')

    @requirements(['#0001'])
    def test_get_triangle_invalid_list(self):
        list1 = (1, 1, 1, 1)
        result = get_triangle_type(list1)
        self.assertEqual(result, 'invalid')

    # dictionary tests
    @requirements(['#0001'])
    def test_get_triangle_equilateral_dict(self):
        dict1 = {'one': 1, 'two': 1, 'three': 1}
        result = get_triangle_type(dict1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001'])
    def test_get_triangle_scalene_dict(self):
        dict1 = {'one': 1, 'two': 3, 'three': 2}
        result = get_triangle_type(dict1)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001'])
    def test_get_triangle_isosceles_dict(self):
        dict1 = {'one': 1, 'two': 1, 'three': 2}
        result = get_triangle_type(dict1)
        self.assertEqual(result, 'isosceles')

    @requirements(['#0001'])
    def test_get_triangle_invalid_dict(self):
        dict1 = {'one': 1, 'two': 1, 'three': 1, 'four': 2}
        result = get_triangle_type(dict1)
        self.assertEqual(result, 'invalid')

    # two input 0 and negatives
    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_two_input(self):
        result = get_triangle_type(1, 0, 1)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_two_input(self):
        result = get_triangle_type(0, -5, 2)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_two_input(self):
        result = get_triangle_type(-5, -5, -5)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_invalid_two_input(self):
        result = get_triangle_type(0, 0, 0)
        self.assertEqual(result, 'invalid')


"""
Class Name: TestGetQuadrilateralType
param: Testcase object
Brief: Class that tests the get_quadrilateral_type and get_rectangle_type functions
in shape_checker.py

Last Modified       Author          Summary
1/12/2016           Paul Ivanov     Init
"""
class TestGetQuadrilateralType(TestCase):

    # all int tests
    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_square_all_int(self):
        result = get_quadrilateral_type(1, 1, 1, 1, 90, 90, 90, 90)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rectangle_all_int(self):
        result = get_quadrilateral_type(1, 2, 2, 1, 90, 90, 90,90)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_invalid_sides_all_int(self):
        result = get_quadrilateral_type(1, 2, 3, 4, 90, 90, 90,90)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_disconnected_all_int(self):
        result = get_quadrilateral_type(1, 1, 1, 1, 80, 90, 90, 90)
        self.assertEqual(result, 'disconnected')

    @requirements(['#0003', '#0003', '#0005'])
    def test_get_quad_rhombus_all_int(self):
        result = get_quadrilateral_type(1, 2, 2, 1, 80, 100, 90, 90)
        self.assertEqual(result, 'rhombus')

    # float
    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_square_all_float(self):
        result = get_quadrilateral_type(1.0, 1.0, 1.0, 1.0, 90.0, 90.0, 90.0, 90.0)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rectangle_all_float(self):
        result = get_quadrilateral_type(1.5, 2.0, 2.0, 1.5, 90.0, 90.0, 90.0, 90.0)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_invalid_sides_all_float(self):
        result = get_quadrilateral_type(1.0, 2.9, 3.7, 4.0, 90.0, 90.0, 90.0, 90.0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_disconnected_all_float(self):
        result = get_quadrilateral_type(1.0, 1.0, 1.0, 1.0, 80.0, 90.0, 90.0, 90.0)
        self.assertEqual(result, 'disconnected')


    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rhombus_all_float(self):
        result = get_quadrilateral_type(1.0, 2.0, 2.0, 1.0, 80.0, 100.0, 90.0, 90.0)
        self.assertEqual(result, 'rhombus')

    # Char test
    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_square_mixed_char(self):
        result = get_quadrilateral_type('a', 1.0, 'd', 1.0, 90.0, 90.0, 90.0, 90.0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rectangle_mixed_char(self):
        result = get_quadrilateral_type(1.5, 2.0, 2.0, 1.5, 90.0, 'a', 90.0, 90.0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_invalid_sides_all_char(self):
        result = get_quadrilateral_type('A', 'v', 'e', 'q', 's', 'p', 'm', 's')
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_disconnected_mixed_char(self):
        result = get_quadrilateral_type(1.0, 1.0, 1.0, 1.0, 'a', 90.0, 90.0, 90.0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rhombus_all_mixed_char(self):
        result = get_quadrilateral_type(1.0, 2.0, 2.0, 'a', 'a', 100.0, 90.0, 90.0)
        self.assertEqual(result, 'invalid')

    # float/ int mix
    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_square_int_float(self):
        result = get_quadrilateral_type(1, 1.0, 1, 1.0, 90.0, 90, 90.0, 90)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rectangle_int_float(self):
        result = get_quadrilateral_type(1.5, 2, 2.0, 1.5, 90, 90.0, 90.0, 90.0)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_invalid_sides_int_float(self):
        result = get_quadrilateral_type(1.0, 2.9, 3.7, 4, 90.0, 90, 90.0, 90.0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_disconnected_int_float(self):
        result = get_quadrilateral_type(1.0, 1.0, 1, 1.0, 80.0, 90, 90.0, 90.0)
        self.assertEqual(result, 'disconnected')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rhombus_int_float(self):
        result = get_quadrilateral_type(1.0, 2.0, 2.0, 1.0, 80, 100.0, 90, 90.0)
        self.assertEqual(result, 'rhombus')

    # negative and 0
    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_zero_int(self):
        result = get_quadrilateral_type(1, 0, 1, 1, 0, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_negative_int(self):
        result = get_quadrilateral_type(-1, 1, 1, 1, -90, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_all_zeroes_int(self):
        result = get_quadrilateral_type(0, 0, 0, 0, 0, 0, 0, 0)
        self.assertEqual(result, 'invalid')
