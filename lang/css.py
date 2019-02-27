from talon.voice import Context, Key, press
import talon.clip as clip
from ..utils import text, parse_words, parse_words_as_integer, insert, word, join_words

def context_func(app, win):
    if app.bundle == 'com.google.Chrome': return True
    elif win.doc.endswith(".css"): return True
    return False

context = Context('css', func=context_func)

def CursorText(s):
    left, right = s.split('{.}', 1)
    return [left + right, Key(' '.join(['left'] * len(right)))]

# use 'pee' formatter for properties, in std.py
# 'pee background color' will output 'background-color: '

context.keymap({
  'paw with' : 'width: ',
  'paw color' : CursorText('rgba({.})'),
  # animation
  'keyframe' : '@keyframes ',
  # media queries
  'media general' : CursorText('@media screen and ({.})'),
  # media query attributesk
  'minimum height' : CursorText('min-height: {.}'),
  'maximum height' : CursorText('max-height: {.}'),
  'minimum with' : CursorText('min-width: {.}'),
  'maximum with' : CursorText('max-width: {.}'),
  # units
  'you pick' : 'px',
  'you dag' : 'deg',
  # flex box properties
  'flex line content' : 'align-content: ',
  'flex line items' : 'align-items: ',
  'flex line self' : 'align-self: ',
  'flex solid' : 'flex-wrap: ',
  'flex shrink': 'flex-shrink: ',
  # flex box property values
  'flex and' : 'flex-end',
  'flex solid none' : 'nowrap',
  'flex solid real' : 'wrap',
})
