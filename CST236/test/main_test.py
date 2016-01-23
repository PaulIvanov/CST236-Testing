from source.main import Interface, NOT_A_QUESTION_RETURN, UNKNOWN_QUESTION, NO_QUESTION, NO_TEACH
from test.plugins.ReqTracer import requirements
from test.plugins.ReqTracer import jobStory
from datetime import datetime
import test.shape_checker_test


class TestInterfaceAdded(test.shape_checker_test.TestCase):
    def test_question_datetime_correct(self):
        new_interface = Interface()
        test_string1 = "What time is it?"
        result = new_interface.ask(test_string1)
        curr_time = datetime.now()
        curr_time = curr_time.replace(second=0, microsecond=0)
        self.assertEqual(result, str(curr_time))


    def test_fibonacci_n_int(self):
        new_interface = Interface()
        test_string1 = "What is the 5 digit of fibonacci?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, 5)


    def test_fibonacci_n_float(self):
        new_interface = Interface()
        test_string1 = "What is the 5.3 digit of fibonacci?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, 5)


    def test_fibonacci_n_negative_int(self):
        new_interface = Interface()
        test_string1 = "What is the -5 digit of fibonacci?"
        result = new_interface.ask(test_string1)
        self.assertEqual(result, "invalid number")
