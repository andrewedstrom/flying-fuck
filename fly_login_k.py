import re
from thefuck.shells import shell
from thefuck.utils import for_app

regex = "certificate signed by unknown authority"

@for_app('fly')
def match(command):
    return (regex in command.stderr)

def get_new_command(command):
    return command.script + " -k"

# Optional:
enabled_by_default = True

priority = 1000  # Lower first, default is 1000

requires_output = True
