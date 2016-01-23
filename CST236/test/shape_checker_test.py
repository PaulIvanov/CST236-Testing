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



"""
Class Name: TestQuestionAnswer
param: Testcase object
Brief: Class that tests the Interface functions
in question_answer.py

Last Modified       Author          Summary
1/12/2016           Paul Ivanov     Init
"""
class TestQuestionAnswer(TestCase):

    #check for keywords to work
    @requirements(['#0006', '#0008', '#0010', '#0011'])
    def test_question_ask_bad_keyword(self):
        new_interface = Interface()
        result = new_interface.ask("Is paul awesome?")
        self.assertEqual(result, NOT_A_QUESTION_RETURN)

    @requirements(['#0006', '#0008', '#0010', '#0011'])
    def test_question_ask_mark_only(self):
        new_interface = Interface()
        result = new_interface.ask("?")
        self.assertEqual(result, NOT_A_QUESTION_RETURN)

    @requirements(['#0006', '#0008', '#0009', '#0010', '#0011'])
    def test_question_ask_blank(self):
        new_interface = Interface()
        result = new_interface.ask(' ')
        self.assertEqual(result, NOT_A_QUESTION_RETURN)

    @requirements(['#0006','#0007', '#0008', '#0010', '#0011', '#0013', '#0014'])
    def test_question_ask_keyword_what(self):
        new_interface = Interface()
        result = new_interface.ask("What are you?")
        self.assertEqual(result, UNKNOWN_QUESTION)

    @requirements(['#0006','#0007', '#0008', '#0010', '#0011', '#0013', '#0014'])
    def test_question_ask_keyword_why(self):
        new_interface = Interface()
        result = new_interface.ask("Why is paul awesome?")
        self.assertEqual(result, UNKNOWN_QUESTION)

    @requirements(['#0006','#0007', '#0008', '#0010', '#0011', '#0013', '#0014'])
    def test_question_ask_keyword_how(self):
        new_interface = Interface()
        result = new_interface.ask("How Is paul awesome?")
        self.assertEqual(result, UNKNOWN_QUESTION)

    @requirements(['#0006','#0007', '#0008', '#0010', '#0011', '#0013', '#0014'])
    def test_question_ask_keyword_where(self):
        new_interface = Interface()
        result = new_interface.ask("Where Is paul from?")
        self.assertEqual(result, UNKNOWN_QUESTION)

    @requirements(['#0006','#0007', '#0008', '#0010', '#0011', '#0013', '#0014'])
    def test_question_ask_keyword_who(self):
        new_interface = Interface()
        result = new_interface.ask("Who Is paul ivanov?")
        self.assertEqual(result, UNKNOWN_QUESTION)

    @requirements(['#0006','#0007', '#0008', "#0009", '#0010', '#0011', '#0014'])
    def test_question_ask_no_question_mark(self):
        new_interface = Interface()
        result = new_interface.ask("How Is paul awesome")
        self.assertEqual(result, NOT_A_QUESTION_RETURN)

    @requirements(['#0006','#0007', '#0008', "#0009", '#0010', '#0011', '#0014'])
    def test_question_ask_no_spaces(self):
        new_interface = Interface()
        result = new_interface.ask("HowIs paulawesome")
        self.assertEqual(result, NOT_A_QUESTION_RETURN)

    @requirements(['#0006','#0007', '#0008', '#0010', '#0011', '#0014'])
    def test_question_ask_no_spaces(self):
        new_interface = Interface()
        result = new_interface.ask("HowIs paulawesome?")
        self.assertEqual(result, NOT_A_QUESTION_RETURN)

    @requirements(['#0006','#0007', '#0008', '#0010', '#0011', '#0013', '#0014', '#0015', '#0016'])
    def test_question_ask_100_similar(self):
        new_interface = Interface()
        test_string = "How is paul awesome?"
        result = new_interface.ask(test_string)
        new_interface.teach("He just is.")
        result = new_interface.ask(test_string)
        self.assertEqual(result, "He just is.")

    @requirements(['#0006','#0007', '#0008', '#0010', '#0011', '#0013', '#0014', '#0015', '#0016'])
    def test_question_ask_100_no_question(self):
        new_interface = Interface()
        test_string = "How is paul awesome?"

        result = new_interface.ask(test_string)
        new_interface.teach("He just is.")

        test_string = test_string.strip('?')
        result = new_interface.ask(test_string)
        self.assertEqual(result, NOT_A_QUESTION_RETURN)

    @requirements(['#0006','#0007', '#0008', '#0010', '#0011', '#0013', '#0014', '#0015', '#0016'])
    def test_question_ask_90_similar(self):
        new_interface = Interface()
        test_string = "How is pual awesom?"
        result = new_interface.ask(test_string)
        new_interface.teach("He just is.")
        result = new_interface.ask(test_string)
        self.assertEqual(result, "He just is.")

    @requirements(['#0006','#0007', '#0008', '#0010', '#0011', '#0013', '#0014', '#0015', '#0016'])
    def test_question_ask_89_similar(self):
        new_interface = Interface()
        test_string = "How is paul awesome?"
        result = new_interface.ask(test_string)
        new_interface.teach("He just is.")
        test_string2 = "How is pual awesum?"
        result = new_interface.ask(test_string2)
        self.assertEqual(result, UNKNOWN_QUESTION)

    @requirements(['#0006', '#0007', '#0008', '#0010', '#0011', '#0013', '#0014', '#0015', '#0016'])
    def test_question_ask_0_similar(self):
        new_interface = Interface()
        test_string1 = "How is paul awesome?"
        result = new_interface.ask(test_string1)
        new_interface.teach("He just is.")
        dif_str = "jack do knot scar."
        result = new_interface.ask(dif_str)
        self.assertEqual(result, NOT_A_QUESTION_RETURN)

    @requirements(['#0001', '#0002', '#0006', '#0007', '#0010', '#0011', '#0012', '#0013', '#0014', '#0015', '#0016'])
    def test_question_triangle_generator(self):
        new_interface = Interface()
        test_string1 = "What type of triangle is 2 2 2?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "equilateral")

    @requirements(['#0001', '#0002', '#0006', '#0007', '#0008', "#0009", '#0010', '#0011', '#0013', '#0012', '#0014', '#0015', '#0016'])
    def test_question_triangle_generator_no_question(self):
        new_interface = Interface()
        test_string1 = "What type of triangle is 2 2 2"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, NOT_A_QUESTION_RETURN)

    @requirements(['#0001', '#0002', '#0006', '#0007', '#0008', '#0010', '#0011', '#0013', '#0014', '#0015', '#0016'])
    def test_question_triangle_generator_invalid(self):
        new_interface = Interface()
        test_string1 = "What type of triangle is 2 0 2?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "invalid")

    @requirements(['#0001', '#0002', '#0006', '#0007', '#0008', '#0010', '#0011', '#0013', '#0014', '#0015', '#0016'])
    def test_question_triangle_generator_isosceles(self):
        new_interface = Interface()
        test_string1 = "What type of triangle is 2 3 2?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "isosceles")

    @requirements(['#0001', '#0002', '#0006', '#0007', '#0008', '#0010', '#0011', '#0013', '#0014', '#0015', '#0016'])
    def test_question_triangle_generator_scalene(self):
        new_interface = Interface()
        test_string1 = "What type of triangle is 1 2 3?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "scalene")

    @requirements(['#0003', '#0004', '#0005', '#0006', '#0007', '#0008', '#0010', '#0011', '#0013', '#0014', '#0015', '#0016'])
    def test_question_quad_generator_rect(self):
        new_interface = Interface()
        test_string1 = "What type of quadrilateral is 2 2 4 4 90 90 90 90?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "rectangle")

    @requirements(['#0003', '#0004', '#0005', '#0006', '#0007', '#0008', '#0010', '#0011', '#0013', '#0014', '#0015', '#0016'])
    def test_question_quad_generator_disconnected(self):
        new_interface = Interface()
        test_string1 = "What type of quadrilateral is 2 2 4 4 99 90 90 90?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "disconnected")

    @requirements(['#0015', '#0017', '#0021'])
    def test_question_prev_question_none(self):
        new_interface = Interface()
        result = new_interface.teach()
        self.assertEqual(result, NO_QUESTION)

    @requirements(['#0006', '#0007', '#0008', '#0010', '#0011', '#0013', '#0014', '#0015', '#0016', '#0018'])
    def test_question_prev_question_known_answer(self):
        new_interface = Interface()
        test_string1 = "How is paul awesome?"
        result = new_interface.ask(test_string1)
        result = new_interface.teach("He just is.")
        result = new_interface.teach("Shouldn't allow change")
        self.assertEqual(result, NO_TEACH)

    @requirements(['#0006', '#0007', '#0008', '#0010', '#0011', '#0013', '#0014', '#0015', '#0016', '#0019', '#0020'])
    def test_question_prev_function_ptr(self):
        new_interface = Interface()
        test_string1 = "How did a function ptr get here?"
        result = new_interface.ask(test_string1)
        result = new_interface.teach(get_quadrilateral_type)
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "invalid")

















