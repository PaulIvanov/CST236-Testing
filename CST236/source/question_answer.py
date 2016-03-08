"""
:mod:`source.question_answer.py`
============================================
Last Modified       Author             Summary
??/??/????          Paul Ivanov     Init

The following code class is representing a data structure to store two strings that
contain a question key to an answer value
"""

# This class does not need any public methods.
# pylint: disable=R0903
class QA(object):
    """
    Class: QA

    Desc: The following code is a data structure to store two strings that
          contain a question key to an answer value
    """
    def __init__(self, question, answer, default=False):
        self.default = default
        self.question = question
        self.function = None
        self.value = None
        if hasattr(answer, '__call__'):
            self.function = answer
        else:
            self.value = answer
