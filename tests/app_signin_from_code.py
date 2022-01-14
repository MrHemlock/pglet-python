import inspect
import os
import sys

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import pglet
from pglet import Button, Checkbox, Text, Textbox


def main(page):

    logged_user = Text(page.user_name)

    def signout_clicked(e):
        page.signout()

    def page_signin(e):
        logged_user.value = page.user_name
        page.update()

    def page_signout(e):
        logged_user.value = "Not logged in"
        page.update()

    page.on_signin = page_signin
    page.on_signout = page_signout

    page.add(logged_user, Button("Signout", on_click=signout_clicked))


pglet.app("pglet-signin-test", target=main, local=True, permissions="*")
