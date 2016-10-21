import sys
from termcolor import colored, cprint

cprint('Hello, World!', 'cyan', attrs=['bold'])

print()

cprint("Attention!", 'red', file=sys.stderr)
