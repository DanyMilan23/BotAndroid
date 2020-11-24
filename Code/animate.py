import itertools
from colorama import Fore, Style,init
import time

def animate(message):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        print("\r"+Style.BRIGHT+Fore.GREEN+message+c+Fore.RESET, end="")
        time.sleep(0.1)