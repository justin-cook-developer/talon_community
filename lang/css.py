from talon.voice import Context, Key, press
import talon.clip as clip
from ..utils import text, parse_words, parse_words_as_integer, insert, word, join_words

def context_func(app, win):
    if app.bundle == 'com.google.Chrome': return True
    return False

context = Context('css', func=context_func)

def CursorText(s):
    left, right = s.split('{.}', 1)
    return [left + right, Key(' '.join(['left'] * len(right)))]

# use 'pee' formatter for properties, in std.py
# 'pee background color' will output 'background-color: '

context.keymap({
  'paw color' : CursorText('rgba({.})'),
  # units
  'you pick' : ['px;', Key('enter')],
})
