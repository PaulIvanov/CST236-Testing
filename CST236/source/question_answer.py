class QA(object):
    def __init__(self, question, answer, default=False):
        self.default = default
        self.question = question
        self.function = None
        self.value = None
        if hasattr(answer, '__call__'):
            self.function = answer
        else:
            self.value = answer