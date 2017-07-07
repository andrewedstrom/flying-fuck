import re
from thefuck.shells import shell
from thefuck.utils import for_app

regex = "run the following(?: to log in)?:\n\s+(fly .+)\n"

@for_app('fly')
def match(command):
    return (re.search(regex,command.stderr.lower()))


def get_new_command(command):
    m = re.search(regex,command.stderr.lower())
    new_command = m.group(1)
    return [shell.and_(new_command, command.script),
            shell.and_(new_command + " -k", command.script)]

# Optional:
enabled_by_default = True

priority = 1000  # Lower first, default is 1000

requires_output = True
