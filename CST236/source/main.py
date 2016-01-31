from source.question_answer import QA
from source.shape_checker import get_triangle_type, get_quadrilateral_type
from source.answers import get_datetime, get_fibonacci, get_pi_digit, open_door, convert_num, answer_to_universe
from source.answers import hello, adder, subtractor, get_emotion, get_name, divider, multiplier, get_mod
import difflib
NOT_A_QUESTION_RETURN = "Was that a question?"
UNKNOWN_QUESTION = "I don't know, please provide the answer"
NO_QUESTION = 'Please ask a question first'
NO_TEACH = 'I don\'t know about that. I was taught differently'
CLEARED_MEMORY = 'Memory Cleared'


class Interface(object):
    def __init__(self):
        self.how_dict = {}
        self.what_dict = {}
        self.where_dict = {}
        self.who_dict = {}

        self.keywords = ['How', 'What', 'Where', 'Who', "Why", "Hello?"]
        self.question_mark = chr(0x3F)

        self.question_answers = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type, True),
            'What type of quadrilateral is ': QA('What type of quadrilateral is ', get_quadrilateral_type, True),
            'What time is it ': QA('What time is it ', get_datetime, True),
            'What is the n digit of fibonacci ': QA('What is the n digit of fibonacci ', get_fibonacci, True),
            'What is the n digit of pi': QA('What is the n digit of pi', get_pi_digit, True),
            'What is the answer to life the universe and everything?': QA('What is the answer to life the universe and everything?',
                                                                          answer_to_universe, True),
            'Hello?': QA('Hello?', hello, True),
            'What is n + n ': QA('What is +', adder, True),
            'What is n - n ': QA('What is -', subtractor, True),
            'What is n divided by n ': QA('What is n divided by n', divider, True),
            'What is n multiplied by n ': QA('What is n multiplied by n', multiplier, True),
            'What is n mod n ': QA('What is mod ', get_mod, True),
            'How are you?': QA('How are you?', get_emotion, True),
            'What is your name?': QA('What is your name?', get_name, True),
            'What are all the questions you know?': QA('What are all the questions you know?', self.get_questions, True)
        }
        self.statement_answers = {
            'Please clear memory': QA('Please clear memory', 'Memory Cleared', True),
            'Open the door hal.': QA('Open the door hal ', open_door, True),
            'Convert <number> <units> to <units>': QA('convert <number> to ', convert_num, True)
        }
        self.last_question = None


    def ask(self, question=""):
        if not isinstance(question, str):
            self.last_question = None
            raise Exception('Not A String!')
        if question[-1] != self.question_mark or question.split(' ')[0] not in self.keywords:
            self.last_question = None

            if question.startswith("Convert"):
                question = question.rstrip('.')
                question = question.lstrip('Convert')
                question = question.lstrip(' ')
                number, unit1, delimiter, unit2 = question.split(' ', 4)

                try:
                    number = float(number)

                except ValueError:
                    return "invalid input"

                return convert_num(number, unit1, unit2)


            if question in self.statement_answers:
                answer = self.__parse_question(self.statement_answers, question)

                if answer == 'Memory Cleared':
                    #special case, the answer will be the signal to clr mem
                    return self.__clr_mem()

                else:
                    return answer
            else:
                return NOT_A_QUESTION_RETURN

        else:
            return self.__parse_question(self.question_answers, question)


    def teach(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        elif self.last_question in self.question_answers.keys():
            return NO_TEACH
        else:
            self.__add_answer(answer)


    def correct(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        else:
            self.__add_answer(answer)


    def __add_answer(self, answer):
        self.question_answers[self.last_question] = QA(self.last_question, answer)


    def __parse_question(self, dict, question):
        parsed_question = ""
        args = []
        for keyword in question[:-1].split(' '):
            try:
                args.append(float(keyword))
            except:
                parsed_question += "{0} ".format(keyword)
        parsed_question = parsed_question[0:-1]
        self.last_question = parsed_question
        for answer in dict.values():
            if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                if answer.function is None:
                    return answer.value
                else:
                    try:
                        return answer.function(*args)
                    except Exception as ex:
                        print ex
                        raise Exception("Too many extra parameters")
        else:
            return UNKNOWN_QUESTION

    def __clr_mem(self):

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
        question_list = []
        for key in self.question_answers:
            question_list.append(key)

        for key in self.statement_answers:
            question_list.append(key)

        return question_list

