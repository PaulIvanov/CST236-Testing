
class RequirementTrace(object):
    req_text = ""

    def __init__(self, text):
        self.req_text = text
        self.func_name = []

Requirements = {}
Stories = []

class JSTrace(object):
    js_text = ""

    def __init__(self, text):
        self.js_text = text
        self.func_name = []


def requirements(req_list):
    def wrapper(func):
        def add_req_and_call(*args, **kwargs):
            for req in req_list:
                if req not in Requirements.keys():
                    raise Exception('Requirement {0} not defined'.format(req))
                Requirements[req].func_name.append(func.__name__)
            return func(*args, **kwargs)

        return add_req_and_call

    return wrapper


with open('lab_requirements.txt') as f:
    for line in f.readlines():
        if '#0' in line:
            req_id, desc = line.split(' ', 1)
            Requirements[req_id] = RequirementTrace(desc)

        elif line.startswith('*'):
            garbage, text = line.split(' ', 1)
            Stories.append(JSTrace(text.strip()))


def jobStory(story):
    def wrapper(func):
        def add_job_and_call(*args, **kwargs):
            for job in Stories:
                if story == job.js_text:
                    job.func_name.append(func.__name__)
                    break
            else:
                raise Exception('Job story not defined')
            return func(*args, **kwargs)

        return add_job_and_call
    return wrapper
