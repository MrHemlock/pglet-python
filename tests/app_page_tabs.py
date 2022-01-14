import inspect
import os
import sys

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import pglet
from pglet import Button, Checkbox, Page, Stack, Tab, Tabs, Text, Textbox

page = pglet.page("index", no_window=True)

page.clean()

page.title = "Counter"
page.update()

stack2 = Tabs(tabs=[Tab(text="all"), Tab(text="active"), Tab(text="completed")])

page.add(stack2)

input("Press Enter to exit...")
