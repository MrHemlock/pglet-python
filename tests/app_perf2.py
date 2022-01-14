import inspect
import os
import sys

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import pglet
from pglet import (Button, Checkbox, Icon, Page, SearchBox, Stack, Tab, Tabs,
                   Text, Textbox)

page = pglet.page("index", no_window=True)

page.clean()

page.title = "Perf tuning"
page.update()

items = Stack(id="icons", horizontal=True, wrap=True)

stack = Stack(id="container", controls=[SearchBox(), items])

for n in range(10):
    s = Stack(
        id=f"outer-{n}",
        controls=[Stack(id=f"inner-{n}", controls=[Text(value=f"C{n}")])],
    )

    # items.controls.append(Text(f'C{n}'))
    items.controls.append(s)

# page.add(stack)

page.add(
    Stack(controls=[SearchBox(placeholder="search 1")]),
    Checkbox(label="Check, check!"),
    items,
)

input("Press Enter to exit...")
