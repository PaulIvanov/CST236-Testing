from nose2.events import Plugin
from ReqTracer import Requirements, Stories

class MyPlugin(Plugin):
    configSection = 'reqTracer'

    def afterSummaryReport(self, event):
        with open("TraceOutput.txt", 'w') as w:
            for key, item in sorted(Requirements.items()):
                # reformat this text file
                w.write(key + ':' + str(item.func_name) + '\n')

            for item in Stories:
                w.write(item.js_text + ': ' + str(item.func_name) + '\n')
