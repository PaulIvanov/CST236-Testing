"""
:mod:`source.main.py`
============================================
Last Modified       Author             Summary
??/??/????          Joshua Kimball     Init

The following code is an API for asking various questions
"""

import re
import difflib
from source.question_answer import QA
from source.shape_checker import get_triangle_type, get_quadrilateral_type
from source.answers import get_datetime, get_fibonacci, get_pi_digit,\
    open_door, convert_num, answer_to_universe
from source.answers import hello, adder, subtractor, get_emotion,\
    get_name, divider, multiplier, get_mod

import source.git_utils


NOT_A_QUESTION_RETURN = "Was that a question?"
UNKNOWN_QUESTION = "I don't know, please provide the answer"
NO_QUESTION = 'Please ask a question first'
NO_TEACH = 'I don\'t know about that. I was taught differently'
CLEARED_MEMORY = 'Memory Cleared'

# I did not implement this. Joshua said not to worry about it
# pylint: disable=R0902
class Interface(object):
    """
    Class: Interface

    Desc: Class that takes in a question and attempts to answer the question
        If it doesnt know the answer, it asks for the answer
    ============================================
    Last Modified       Author             Summary
    ??/??/????          Joshua Kimball     Init
    """

    def __init__(self):
        self.how_dict = {}
        self.what_dict = {}
        self.where_dict = {}
        self.who_dict = {}
        self.question_answer_buffer = ''
        self.__log_file_name = "Question_Answer.log"

        with open(self.__log_file_name, "w") as log_file:
            log_file.write("QUESTIONS: \n")

        self.keywords = ['How', 'What', 'Where', 'Who', "Why", "Hello?", "Is"]
        self.question_mark = chr(0x3F)

        self.question_answers = {
            'What type of triangle is ': QA('What type of triangle is ',
                                            get_triangle_type, True),
            'What type of quadrilateral is ': QA('What type of quadrilateral is ',
                                                 get_quadrilateral_type, True),
            'What time is it ': QA('What time is it ', get_datetime, True),
            'What is the n digit of fibonacci ': QA('What is the n digit of fibonacci ',
                                                    get_fibonacci, True),
            'What is the n digit of pi': QA('What is the n digit of pi', get_pi_digit, True),
            'What is the answer to life the universe and everything?':
                QA('What is the answer to life the universe and everything?',
                   answer_to_universe, True),
            'Hello?': QA('Hello?', hello, True),
            'What is n + n ': QA('What is +', adder, True),
            'What is n - n ': QA('What is -', subtractor, True),
            'What is n divided by n ': QA('What is n divided by n', divider, True),
            'What is n multiplied by n ': QA('What is n multiplied by n', multiplier, True),
            'What is n mod n ': QA('What is mod ', get_mod, True),
            'How are you?': QA('How are you?', get_emotion, True),
            'What is your name?': QA('What is your name?', get_name, True),
            'What are all the questions you know?': QA('What are all the questions you know?',
                                                       self.get_questions, True),

            'Is the <file path> in the repo?': QA('Is the in the repo ',
                                                  source.git_utils.is_file_in_repo, True),
            'What is the status of ': QA('What is the status of ',
                                         source.git_utils.get_git_file_info, True),
            'What is the deal with ': QA('What is the deal with ',
                                         source.git_utils.get_file_info, True),
            'What branch is ?': QA('What branch is ', source.git_utils.get_repo_branch, True),
            'Where did <file path> come from?': QA('Where did come from',
                                                   source.git_utils.get_repo_url, True)
        }
        self.statement_answers = {
            'Please clear memory': QA('Please clear memory', 'Memory Cleared', True),
            'Open the door hal.': QA('Open the door hal ', open_door, True),
            'Convert <number> <units> to <units>': QA('convert <number> to ', convert_num, True)
        }
        self.last_question = None


    def ask(self, question=""):
        """
        Takes in a question and attempts to answer it

        :param question: question that was asked
        :type  question: str

        :returns: answer
        :rtype: int or float or str or date time
        """
        if not isinstance(question, str):
            self.last_question = None
            raise Exception('Not A String!')
        if question[-1] != self.question_mark or question.split(' ')[0] not in self.keywords:
            self.last_question = None

            if question.startswith("Convert"):
                question = question.rstrip('.')
                question = question.lstrip('Convert')
                question = question.lstrip(' ')
                # The delimiter is a throw away var to correctly parse a conversion
                number, unit1, delimiter, unit2 = question.split(' ', 4)  # pylint: disable=W0612

                try:
                    # Reason for pylint if this fails, it throws an exception
                    number = float(number)

                except ValueError:
                    return self.__write_answer_to_log("invalid input", question)

                return self.__write_answer_to_log(convert_num(number, unit1, unit2), question)

            if question in self.statement_answers:
                answer = self.__parse_question(self.statement_answers, question)

                if answer == 'Memory Cleared':
                    # special case, the answer will be the signal to clr mem
                    return self.__write_answer_to_log(self.__clr_mem(), question)

                else:
                    return self.__write_answer_to_log(answer, question)
            else:
                return self.__write_answer_to_log(NOT_A_QUESTION_RETURN, question)
        else:
            return self.__write_answer_to_log(self.__parse_question(self.question_answers,
                                                                    question), question)

    def teach(self, answer=""):
        """
        Takes in a answer and sets the last question answered to return the new

        :param answer: answer that was given
        :type  answer: str
        """
        if self.last_question is None:
            return NO_QUESTION
        elif self.last_question in self.question_answers.keys():
            return NO_TEACH
        else:
            self.__add_answer(answer)


    def correct(self, answer=""):
        """
        Takes in a answer and sets the last question answered to return the new answer

        :param answer: answer that was given
        :type  answer: str
        """
        if self.last_question is None:
            return NO_QUESTION
        else:
            self.__add_answer(answer)


    def __add_answer(self, answer):
        """
        private function that adds the answer to the last asked question

        :param answer: answer that was given
        :type  answer: str
        """
        self.question_answers[self.last_question] = QA(self.last_question, answer)

    def __parse_question(self, my_dict, question):
        """
        private function that parses the current question for arguments and question

        :param my_dict: Container for the parsed question words
        :type  my_dict: dict

        :param question: current question asked
        :type  question: str
        """
        parsed_question = ""
        args = []
        for keyword in question[:-1].split(' '):
            try:
                if self.is_valid_path(keyword):
                    args.append(keyword)
                    continue

                if '\\' in keyword and ':' not in keyword:
                    path = args.pop()
                    args.append((path + ' ' + keyword))

                    continue

                args.append(float(keyword))

            # Joshua's implementation
            except:  # pylint: disable=W0702
                parsed_question += "{0} ".format(keyword)
        parsed_question = parsed_question[0:-1]
        self.last_question = parsed_question
        for answer in my_dict.values():
            if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                if answer.function is None:
                    return answer.value
                else:
                    try:
                        return answer.function(*args)
                    except Exception as ex:
                        print ex
                        raise Exception("Too many extra parameters")
        # Joshua's implementation
        else:  # pylint: disable=W0120
            return UNKNOWN_QUESTION

    def __clr_mem(self):
        """
        private function that clears all not default questions from the QA dict

        :returns: Memory has been cleared
        :rtype: str
        """
        temp = {}
        for key in self.question_answers:
            item = self.question_answers[key]
            temp[key] = item

        for key in self.question_answers:
            item = self.question_answers.get(key)
            if item.default is False:
                temp.pop(key)

        self.question_answers = temp

        return CLEARED_MEMORY

    def get_questions(self):
        """
        method that retrieves full list of available questions

        :returns: full list of available questions
        :rtype: list
        """
        question_list = []
        for key in self.question_answers:
            question_list.append(key)

        for key in self.statement_answers:
            question_list.append(key)

        return question_list

    # This is needed for the question parsing
    # pylint: disable=R0201
    def is_valid_path(self, path='invalid'):
        """
        checks to see if the given string is a path

        :param path: investigated string
        :type  path: str

        :returns: true if the path is valid, false if not
        :rtype: bool
        """
        return re.match(r'[a-zA-Z]:\\', path)


    def __write_answer_to_log(self, answer, question):
        """
        writes the given question and answer to a log file

        :param answer: given answer
        :type  answer: str

        :param question: given question
        :type  question: str

        :returns: passes the answer back to avoid screwing anything up
        :rtype: str
        """
        with open(self.__log_file_name, "a") as log_file:
            log_file.write(str(question)+": " + str(answer) + '\n')
            return answer
