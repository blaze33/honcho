try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import re

LINE = re.compile(r'^([A-Za-z0-9_]+):\s*(.+)$')
LINE2 = re.compile(r'^\s+(.+)$')


class Procfile(object):
    def __init__(self, contents):
        self.commands = OrderedDict()
        current_command = None

        for line in contents.splitlines():
            m = LINE.match(line)
            if m:
                current_command = m.group(1)
                self.commands[m.group(1)] = m.group(2)
            elif current_command:
                m2 = LINE2.match(line)
                if m2:
                    self.commands[current_command] += ' ' + m2.group(1)
