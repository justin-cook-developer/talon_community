import time
import contextlib
from talon.voice import Context, Key, press
from talon import ctrl

def normal_mode():
    # get out of any text box
    press('escape')
    # make sure we are in normal mode
    press('escape')

def page_mode():
    normal_mode()
    # insert ignore mode
    press("ctrl-alt-escape")

@contextlib.contextmanager
def page_mode_context():
    page_mode()
    yield
    normal_mode()

def send_string_to_page(string=None):
    def function(m):
        with page_mode_context():
            time.sleep(0.3)
            for character in string:
                press(character)
    return function

def send_key_to_page(key=None):
    def function(m):
        with page_mode_context():
            time.sleep(0.3)
            press(key)
    return function

def compose(m):
    page_mode()

ctx = Context("gmail", func=lambda app, win: win.title.endswith("- Gmail"))
ctx.keymap(
    {
        "inbox": send_string_to_page("gi"),
        "help" : send_key_to_page('shift-?'),
        "search mail" : send_key_to_page('/')
        "compose" : send_key_to_page('c'),
        "compose new tab" : send_key_to_page('d'),      
    }
)
