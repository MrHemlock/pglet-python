import inspect
import json
import os
import signal
import sys
import threading
import time

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import pglet
from pglet import Message, Page, ReconnectingWebSocket, Stack, Text, Toolbar


def main():
    i = 1
    evt = threading.Event()
    while True:
        print(i)
        i = i + 1
        # time.sleep(2)
        evt.wait(20)


# th = threading.Thread(target=main, args=(), daemon=True)
# th.start()
def on_exit():
    print("Exit!")


# signal.signal(signal.SIGINT, on_exit)


def app_main(page):
    print("New session!")


pglet.app(target=app_main, server="http://sdd:5000")

# ws = ReconnectingWebSocket("http://aaa:6000")
# ws.connect()
# main()

# print("Press ENTER to exit")
# input()
