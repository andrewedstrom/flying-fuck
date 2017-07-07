import re

regex = "run the following(?: to log in)?:\n\s+(fly .+)\n"

def match(command):
    return (re.search(regex,command.stderr.lower()))


def get_new_command(command):
    m = re.search(regex,command.stderr.lower())
    new_command = m.group(1)
    return [new_command, new_command + " -k"]

# Optional:
enabled_by_default = True

priority = 1000  # Lower first, default is 1000

requires_output = True
