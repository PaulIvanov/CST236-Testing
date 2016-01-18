from nose2.events import Plugin
from ReqTracer import Requirements


class MyPlugin(Plugin):
    configSection = 'reqTracer'

    def afterSummaryReport(self, event):
        with open("TraceOutput.txt", 'w') as w:
            for key,item in sorted(Requirements.items()):
                # reformat this text file
                w.write(key + ':' + str(item.func_name) + '\n')
