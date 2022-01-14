import inspect
import os
import sys

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import pglet
from pglet import Button, Checkbox, Text, Textbox


def main(page):
    def add_clicked(e):
        page.add(Checkbox(label=new_task.value))

    new_task = Textbox(placeholder="Whats needs to be done?")

    page.add(
        Text(value="Todos", size="large", align="center"),
        new_task,
        Button("Add", on_click=add_clicked),
    )


pglet.app("todo-app", target=main, permissions="*", local=True)
