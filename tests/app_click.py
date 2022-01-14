import inspect
import json
import os
import sys
import time

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import pglet
from pglet import Button, Message, Page, Text, Toolbar

os.environ["PGLET_LOG_LEVEL"] = "debug"


def main(page: Page):
    def on_click(e):
        page.add(Text(f"{time.time()} - {page.session_id}"))

    page.add(Button("Click!", on_click=on_click))


pglet.app("click-click", target=main, web=False)
