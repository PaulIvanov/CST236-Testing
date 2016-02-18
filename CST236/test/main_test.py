from source.main import Interface, NOT_A_QUESTION_RETURN, UNKNOWN_QUESTION, NO_QUESTION, NO_TEACH, CLEARED_MEMORY
from test.plugins.ReqTracer import requirements
from test.plugins.ReqTracer import jobStory
from datetime import datetime
import test.shape_checker_test
from getpass import getuser
from source.shape_checker import get_quadrilateral_type


"""
Class Name: TestQuestionAnswer
param: Testcase object
Brief: Class that tests the Interface functions
in question_answer.py

Last Modified       Author          Summary
1/12/2016           Paul Ivanov     Init
"""
class TestQuestionAnswer(test.shape_checker_test.TestCase):

    #check for keywords to work
    @requirements(['#0006', '#0008', '#0010', '#0011'])
    def test_question_not_string(self):
        new_interface = Interface()
        self.assertRaisesRegexp(Exception, 'Not A String', new_interface.ask, 5)

    @requirements(['#0006', '#0008', '#0010', '#0011'])
    def test_question_ask_bad_keyword(self):
        new_interface = Interface()
        result = new_interface.ask("paul awesome?")
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

    @requirements(['#0015', '#0019', '#0020'])
    def test_question_ask_correct_valid(self):
        new_interface = Interface()
        test_string = "How is paul awesome?"
        result = new_interface.ask(test_string)
        new_interface.teach("He just is.")

        new_interface.correct("He is not awesome")
        result = new_interface.ask(test_string)
        self.assertEqual(result, "He is not awesome")

    @requirements(['#0015', '#0019', '#0020'])
    def test_question_ask_correct_invalid(self):
        new_interface = Interface()
        test_string = "How is paul awesome?"
        result = new_interface.correct("He is not awesome")
        self.assertEqual(result, NO_QUESTION)


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


class TestInterfaceAddedQs(test.shape_checker_test.TestCase):
    # datetime tests
    @jobStory('When I ask "What time is it?" I want to be given the current date/time so I can stay up to date')
    def test_question_datetime_correct(self):
        new_interface = Interface()
        test_string1 = "What time is it?"
        result = new_interface.ask(test_string1)
        curr_time = datetime.now()
        curr_time = curr_time.replace(second=0, microsecond=0)
        self.assertEqual(result, str(curr_time))

    # fibonacci sequence
    @jobStory('When I ask "What is the n digit of fibonacci" I want to receive the answer so I don\'t have to figure it out myself')
    def test_fibonacci_n_int(self):
        new_interface = Interface()
        test_string1 = "What is the 5 digit of fibonacci?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, 5)

    @jobStory('When I ask "What is the n digit of fibonacci" I want to receive the answer so I don\'t have to figure it out myself')
    def test_fibonacci_n_float(self):
        new_interface = Interface()
        test_string1 = "What is the 5.3 digit of fibonacci?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, 5)

    @jobStory('When I ask "What is the n digit of fibonacci" I want to receive the answer so I don\'t have to figure it out myself')
    def test_fibonacci_n_negative_int(self):
        new_interface = Interface()
        test_string1 = "What is the -5 digit of fibonacci?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "invalid")

    @jobStory('When I ask "What is the n digit of fibonacci" I want to receive the answer so I don\'t have to figure it out myself')
    def test_fibonacci_zero(self):
        new_interface = Interface()
        test_string1 = "What is the 0 digit of fibonacci?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, 0)

    @jobStory('When I ask "What is the n digit of fibonacci" I want to receive the answer so I don\'t have to figure it out myself')
    def test_fibonacci_char(self):
        new_interface = Interface()
        test_string1 = "What is the X digit of fibonacci?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "no parameter given in get_fibonacci")

    # get Pi digits
    @jobStory("When I ask \"What is the n digit of pi\" I want to receive the answer so I don't have to figure it out myself")
    def test_get_digit_pi_correct_int(self):
        new_interface = Interface()
        test_string1 = "What is the 3 digit of pi?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, 4)

    @jobStory("When I ask \"What is the n digit of pi\" I want to receive the answer so I don't have to figure it out myself")
    def test_get_digit_pi_correct2(self):
        new_interface = Interface()
        test_string1 = "What is the 5 digit of pi?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, 5)

    @jobStory("When I ask \"What is the n digit of pi\" I want to receive the answer so I don't have to figure it out myself")
    def test_get_digit_pi_zero(self):
        new_interface = Interface()
        test_string1 = "What is the 0 digit of pi?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "invalid")

    @jobStory("When I ask \"What is the n digit of pi\" I want to receive the answer so I don't have to figure it out myself")
    def test_get_digit_pi_negative(self):
        new_interface = Interface()
        test_string1 = "What is the -1 digit of pi?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "invalid")

    @jobStory("When I ask \"What is the n digit of pi\" I want to receive the answer so I don't have to figure it out myself")
    def test_get_digit_pi_char(self):
        new_interface = Interface()
        test_string1 = "What is the X digit of pi?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "invalid")

    @jobStory("When I ask \"What is the n digit of pi\" I want to receive the answer so I don't have to figure it out myself")
    def test_get_digit_pi_float(self):
        new_interface = Interface()
        test_string1 = "What is the 1.5 digit of pi?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, 3)

    @jobStory("When I ask \"What is the n digit of pi\" I want to receive the answer so I don't have to figure it out myself")
    def test_get_digit_no_para(self):
        new_interface = Interface()
        test_string1 = "What is the no digit of pi?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "invalid")

    # test clear memory
    @jobStory("When I ask \"Please clear memory\" I was the application to clear user set questions and answers so I can reset the application")
    def test_clear_mem(self):
        new_interface = Interface()
        test_string1 = "What is a good question to delete?"
        q_answer = "this one"
        result = new_interface.ask(test_string1)
        new_interface.teach(q_answer)
        result = new_interface.ask(test_string1)
        self.assertEqual(result, q_answer)

        new_interface.ask("Please clear memory")
        result = new_interface.ask(test_string1)
        self.assertEqual(result, UNKNOWN_QUESTION)

    # test open the door
    @jobStory("When I say \"Open the door hal\", I want the application to say \"I'm afraid I can't do that <user name> so I know that is not an option")
    def test_open_door(self):
        new_interface = Interface()
        test_string1 = "Open the door hal."
        result = new_interface.ask(test_string1)
        expected_user = getuser()
        expected_result = ("I'm afraid I can't do that " + expected_user)
        self.assertEqual(result, expected_result)

    # test conversions
    @jobStory("When I ask \"Convert <number> <units> to <units>\" I want to receive the converted value and units so I can know the answer.")
    def test_conversion_cm_m_int(self):
        new_interface = Interface()
        test_string1 = "Convert 100 cm to m."
        result = new_interface.ask(test_string1)
        expected_result = 1
        self.assertEqual(result, expected_result)

    @jobStory("When I ask \"Convert <number> <units> to <units>\" I want to receive the converted value and units so I can know the answer.")
    def test_conversion_cm_m_float(self):
        new_interface = Interface()
        test_string1 = "Convert 99.0 cm to m."
        result = new_interface.ask(test_string1)
        expected_result = 0.99
        self.assertEqual(result, expected_result)

    @jobStory("When I ask \"Convert <number> <units> to <units>\" I want to receive the converted value and units so I can know the answer.")
    def test_conversion_m_km(self):
        new_interface = Interface()
        test_string1 = "Convert 100 m to km."
        result = new_interface.ask(test_string1)
        expected_result = 0.1
        self.assertEqual(result, expected_result)

    @jobStory("When I ask \"Convert <number> <units> to <units>\" I want to receive the converted value and units so I can know the answer.")
    def test_conversion_km_m(self):
        new_interface = Interface()
        test_string1 = "Convert 1 km to m."
        result = new_interface.ask(test_string1)
        expected_result = 1000
        self.assertEqual(result, expected_result)

    @jobStory("When I ask \"Convert <number> <units> to <units>\" I want to receive the converted value and units so I can know the answer.")
    def test_conversion_mm_km(self):
        new_interface = Interface()
        test_string1 = "Convert 100 mm to km."
        result = new_interface.ask(test_string1)
        expected_result = 0.0001
        self.assertEqual(result, expected_result)

    @jobStory("When I ask \"Convert <number> <units> to <units>\" I want to receive the converted value and units so I can know the answer.")
    def test_conversion_lbs_kg(self):
        new_interface = Interface()
        test_string1 = "Convert 100 kg to lbs."
        result = new_interface.ask(test_string1)
        expected_result = 220
        self.assertAlmostEqual(result, expected_result)

    @jobStory("When I ask \"Convert <number> <units> to <units>\" I want to receive the converted value and units so I can know the answer.")
    def test_conversion_kg_lbs(self):
        new_interface = Interface()
        test_string1 = "Convert 220 lbs to kg."
        result = new_interface.ask(test_string1)
        expected_result = 100
        self.assertAlmostEqual(result, expected_result)

    @jobStory("When I ask \"Convert <number> <units> to <units>\" I want to receive the converted value and units so I can know the answer.")
    def test_conversion_kg_g(self):
        new_interface = Interface()
        test_string1 = "Convert 1 kg to g."
        result = new_interface.ask(test_string1)
        expected_result = 1000
        self.assertEqual(result, expected_result)

    @jobStory("When I ask \"Convert <number> <units> to <units>\" I want to receive the converted value and units so I can know the answer.")
    def test_conversion_kg_mg(self):
        new_interface = Interface()
        test_string1 = "Convert 1 kg to mg."
        result = new_interface.ask(test_string1)
        expected_result = 10000
        self.assertEqual(result, expected_result)

    @jobStory("When I ask \"Convert <number> <units> to <units>\" I want to receive the converted value and units so I can know the answer.")
    def test_conversion_gallon_pint(self):
        new_interface = Interface()
        test_string1 = "Convert 1 gallon to pint."
        result = new_interface.ask(test_string1)
        expected_result = 8
        self.assertEqual(result, expected_result)

    @jobStory("When I ask \"Convert <number> <units> to <units>\" I want to receive the converted value and units so I can know the answer.")
    def test_conversion_gallon_quart(self):
        new_interface = Interface()
        test_string1 = "Convert 1 gallon to quart."
        result = new_interface.ask(test_string1)
        expected_result = 4
        self.assertEqual(result, expected_result)

    @jobStory("When I ask \"Convert <number> <units> to <units>\" I want to receive the converted value and units so I can know the answer.")
    def test_conversion_no_num_given(self):
        new_interface = Interface()
        test_string1 = "Convert P gallon to quart."
        result = new_interface.ask(test_string1)
        self.assertEqual(result, 'invalid input')

    @jobStory("When I ask \"Convert <number> <units> to <units>\" I want to receive the converted value and units so I can know the answer.")
    def test_conversion_invalid_conversion1(self):
        new_interface = Interface()
        test_string1 = "Convert 10 km to lbs."
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "invalid conversion")

    @jobStory("When I ask \"Convert <number> <units> to <units>\" I want to receive the converted value and units so I can know the answer.")
    def test_conversion_invalid_conversion2(self):
        new_interface = Interface()
        test_string1 = "Convert 10 mm to lbs."
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "invalid conversion")

    @jobStory("When I ask \"Convert <number> <units> to <units>\" I want to receive the converted value and units so I can know the answer.")
    def test_conversion_invalid_conversion3(self):
        new_interface = Interface()
        test_string1 = "Convert 10 cm to gallon."
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "invalid conversion")

    @jobStory("When I ask \"Convert <number> <units> to <units>\" I want to receive the converted value and units so I can know the answer.")
    def test_conversion_invalid_conversion4(self):
        new_interface = Interface()
        test_string1 = "Convert 100 mg to km."
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "invalid conversion")

    @jobStory("When I ask \"Convert <number> <units> to <units>\" I want to receive the converted value and units so I can know the answer.")
    def test_conversion_invalid_conversion5(self):
        new_interface = Interface()
        test_string1 = "Convert 10 mg to pint."
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "invalid conversion")

    @jobStory("When I ask for a numeric conversion I want at least 10 different units I can convert from/to")
    def test_conversion_invalid_conversion6(self):
        new_interface = Interface()
        test_string1 = "Convert 10 lbs to cm."
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "invalid conversion")

    @jobStory("When I ask for a numeric conversion I want at least 10 different units I can convert from/to")
    def test_conversion_invalid_conversion7(self):
        new_interface = Interface()
        test_string1 = "Convert 10 km to lbs."
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "invalid conversion")

    @jobStory("When I ask for a numeric conversion I want at least 10 different units I can convert from/to")
    def test_conversion_invalid_conversion8(self):
        new_interface = Interface()
        test_string1 = "Convert 10 gallon to lbs."
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "invalid conversion")

    # hello question
    @jobStory("When I ask \"Hello?\", I want the application to say \"Hi, I am <user name>'s guide.\"")
    def test_hello_valid(self):
        new_interface = Interface()
        test_string1 = "Hello?"
        result = new_interface.ask(test_string1)
        user = getuser()
        expected_result = ("Hello, I am " + user + "'s guide.")
        self.assertEqual(result, expected_result)

    @jobStory("When I ask \"Hello?\", I want the application to say \"Hi, I am <user name>'s guide.\"")
    def test_hello_invalid(self):
        new_interface = Interface()
        test_string1 = "Hello."
        result = new_interface.ask(test_string1)
        self.assertEqual(result, NOT_A_QUESTION_RETURN)


    #the universe
    @jobStory("When I ask \"What is the answer to life the universe and everything?\" I want the application to answer with the number 42")
    def test_universe_valid(self):
        new_interface = Interface()
        test_string1 = "What is the answer to life the universe and everything?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, 42)

    @jobStory("When I ask \"What is the answer to life the universe and everything?\" I want the application to answer with the number 42")
    def test_universe_invalid(self):
        new_interface = Interface()
        test_string1 = "What is the answer to life the universe and everything"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, NOT_A_QUESTION_RETURN)

    # test_adder
    @jobStory("When I ask \"What is n + n?\", I want the application to add the two number and return the sum so I know how to add them.")
    def test_adder_int(self):
        new_interface = Interface()
        test_string = "What is 2 + 2?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 4)

    @jobStory("When I ask \"What is n + n?\", I want the application to add the two number and return the sum so I know how to add them.")
    def test_adder_float(self):
        new_interface = Interface()
        test_string = "What is 2.5 + 2.5?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 5)

    @jobStory("When I ask \"What is n + n?\", I want the application to add the two number and return the sum so I know how to add them.")
    def test_adder_float_int(self):
        new_interface = Interface()
        test_string = "What is 2 + 2.5?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 4.5)

    @jobStory("When I ask \"What is n + n?\", I want the application to add the two number and return the sum so I know how to add them.")
    def test_adder_one_number(self):
        new_interface = Interface()
        test_string = "What is n + 2.5?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 'invalid')

    @jobStory("When I ask \"What is n + n?\", I want the application to add the two number and return the sum so I know how to add them.")
    def test_adder_one_number2(self):
        new_interface = Interface()
        test_string = "What is 2.5 + n?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 'invalid')

    @jobStory("When I ask \"What is n + n?\", I want the application to add the two number and return the sum so I know how to add them.")
    def test_adder_no_param(self):
        new_interface = Interface()
        test_string = "What is + ?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 'invalid')

    @jobStory("When I ask \"What is n + n?\", I want the application to add the two number and return the sum so I know how to add them.")
    def test_adder_too_many_param(self):
        new_interface = Interface()
        test_string = "What is 5 + 5 + 5 +5?"
        self.assertRaisesRegexp(Exception, "Too many extra parameters", new_interface.ask, test_string)

    @jobStory("When I ask \"What is n + n?\", I want the application to add the two number and return the sum so I know how to add them.")
    def test_adder_negative_int(self):
        new_interface = Interface()
        test_string = "What is -6 + 5?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, -1)

    #subtractor
    @jobStory("When I ask \"What is n - n?\", I want the application to subtract the two numbers and return the difference.")
    def test_subtractor_int(self):
        new_interface = Interface()
        test_string = "What is 5 - 4?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 1)

    @jobStory("When I ask \"What is n - n?\", I want the application to subtract the two numbers and return the difference.")
    def test_subtractor_float(self):
        new_interface = Interface()
        test_string = "What is 5.9 - 4.0?"
        result = new_interface.ask(test_string)
        self.assertAlmostEqual(result, 1.9)

    @jobStory("When I ask \"What is n - n?\", I want the application to subtract the two numbers and return the difference.")
    def test_subtractor_float_int(self):
        new_interface = Interface()
        test_string = "What is 5.9 - 4?"
        result = new_interface.ask(test_string)
        self.assertAlmostEqual(result, 1.9)

    @jobStory("When I ask \"What is n - n?\", I want the application to subtract the two numbers and return the difference.")
    def test_subtractor_negative_int(self):
        new_interface = Interface()
        test_string = "What is -5 - 4?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, -9)

    @jobStory("When I ask \"What is n - n?\", I want the application to subtract the two numbers and return the difference.")
    def test_subtractor_invalid(self):
        new_interface = Interface()
        test_string = "What is - ?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 'invalid')

    @jobStory("When I ask \"What is n - n?\", I want the application to subtract the two numbers and return the difference.")
    def test_subtractor_char_int(self):
        new_interface = Interface()
        test_string = "What is n - 4?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 'invalid')

    @jobStory("When I ask \"What is n divided by n?\", I want the application to divide the two numbers and return the dividend.")
    def test_divide_int(self):
        new_interface = Interface()
        test_string = "What is 4 divided by 4?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 1)

    @jobStory("When I ask \"What is n divided by n?\", I want the application to divide the two numbers and return the dividend.")
    def test_divide_float(self):
        new_interface = Interface()
        test_string = "What is 4.0 divided by 1?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 4)

    @jobStory("When I ask \"What is n divided by n?\", I want the application to divide the two numbers and return the dividend.")
    def test_divide_char(self):
        new_interface = Interface()
        test_string = "What is n divided by 4?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 'invalid')

    @jobStory("When I ask \"What is n divided by n?\", I want the application to divide the two numbers and return the dividend.")
    def test_divide_zero_numerator(self):
        new_interface = Interface()
        test_string = "What is 0 divided by 3?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 0)

    @jobStory("When I ask \"What is n divided by n?\", I want the application to divide the two numbers and return the dividend.")
    def test_divide_no_numerator(self):
        new_interface = Interface()
        test_string = "What is n divided by n?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 'invalid')

    @jobStory("When I ask \"What is n divided by n?\", I want the application to divide the two numbers and return the dividend.")
    def test_divide_zero_denominator(self):
        new_interface = Interface()
        test_string = "What is 4 divided by 0?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, "Can't divide by zero")

    @jobStory("When I ask \"What is n multiplied by n?\", I want the application to multiply the two numbers and return the product.")
    def test_multiply_zero_multiply(self):
        new_interface = Interface()
        test_string = "What is 4 multiplied by 0?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 0)

    @jobStory("When I ask \"What is n multiplied by n?\", I want the application to multiply the two numbers and return the product.")
    def test_multiply_one(self):
        new_interface = Interface()
        test_string = "What is 4 multiplied by 1?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 4)

    @jobStory("When I ask \"What is n multiplied by n?\", I want the application to multiply the two numbers and return the product.")
    def test_multiply_char(self):
        new_interface = Interface()
        test_string = "What is n multiplied by p?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 'invalid')

    @jobStory("When I ask \"What is n multiplied by n?\", I want the application to multiply the two numbers and return the product.")
    def test_multiply_one_inp(self):
        new_interface = Interface()
        test_string = "What is 4 multiplied by p?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 'invalid')


    @jobStory("When I ask \"What is n mod n?\", I want the application to modulus the two numbers and return the remainder.")
    def test_mod_one_correct(self):
        new_interface = Interface()
        test_string = "What is 4 mod 1?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 0)

    @jobStory("When I ask \"What is n mod n?\", I want the application to modulus the two numbers and return the remainder.")
    def test_mod_no_inp(self):
        new_interface = Interface()
        test_string = "What is mod ?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 'invalid')


    @jobStory("When I ask \"What is n mod n?\", I want the application to modulus the two numbers and return the remainder.")
    def test_mod_one_inp2(self):
        new_interface = Interface()
        test_string = "What is 1 mod n?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 'invalid')


    @jobStory("When I ask \"What is n mod n?\", I want the application to modulus the two numbers and return the remainder.")
    def test_mod_one_inp(self):
        new_interface = Interface()
        test_string = "What is 4 mod 1?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 0)


    # test emotion
    @jobStory("When I ask \"How are you?\", I want the application to tell me how it feels so I know how it feels.")
    def test_emotion_valid(self):
        new_interface = Interface()
        test_string = "How are you?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 'Unstable')

    @jobStory("When I ask \"How are you?\", I want the application to tell me how it feels so I know how it feels.")
    def test_emotion_invalid(self):
        new_interface = Interface()
        test_string = "How are you"
        result = new_interface.ask(test_string)
        self.assertEqual(result, NOT_A_QUESTION_RETURN)

    # test name
    @jobStory("When I ask \"What is your name?\", I want the application to tell me its name so I know it.")
    def test_name_valid(self):
        new_interface = Interface()
        test_string = "What is your name?"
        result = new_interface.ask(test_string)
        self.assertEqual(result, 'Juan')

    @jobStory("When I ask \"What is your name?\", I want the application to tell me its name so I know it.")
    def test_name_invalid(self):
        new_interface = Interface()
        test_string = "What is your name"
        result = new_interface.ask(test_string)
        self.assertEqual(result, NOT_A_QUESTION_RETURN)

    @jobStory("When I ask \"What are all the questions you know?\", I want the application to give me a list of all the questions with known answers.")
    def test_questionlist(self):
        new_interface = Interface()
        test_string = "What are all the questions you know?"
        result = new_interface.ask(test_string)
        exp_result = new_interface.get_questions()
        self.assertEqual(result, exp_result)


    # TODO: Add more testcases for datetime--- Add 5 stories and add the stories to tests