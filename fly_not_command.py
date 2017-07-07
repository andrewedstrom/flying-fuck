import re
from thefuck.utils import for_app

regex = "Unknown command `(.+)', did you mean `(.+)'\?"

@for_app('fly')
def match(command):
    return (re.search(regex,command.stderr))

def get_new_command(command):
    m = re.search(regex,command.stderr)
    new_command = command.script.replace(m.group(1),m.group(2))
    return new_command

# Optional:
enabled_by_default = True

priority = 1000  # Lower first, default is 1000

requires_output = True
