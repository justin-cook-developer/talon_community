from talon.voice import Context, Key, press
import talon.clip as clip
from ..utils import text, parse_words, parse_words_as_integer, insert, word, join_words

def verifyExtension(app, win):
    return win.doc.endswith(".js") or win.doc.endswith(".ts") or win.doc.endswith(".jsx") or "freeCodeCamp" in win.title

context = Context("javascript", func=verifyExtension)

def remove_spaces_around_dashes(m):
    words = parse_words(m)
    s = ' '.join(words)
    s = s.replace(' – ', '-')
    insert(s)

def CursorText(s):
    left, right = s.split('{.}', 1)
    return [left + right, Key(' '.join(['left'] * len(right)))]


context.keymap({
    'const [<dgndictation>]': ['const ', text],
    'let [<dgndictation>]': ['let ', text],
    'static': 'static ',
    'args': ['()', Key('left')],
    'index': ['[]', Key('left')],
    'block': [' {}', Key('left enter')],
    'empty array': '[]',
    'empty object': '{}',
    'call': '()',

    'state func': 'function ',
    'state return': 'return ',
    'state constructor': 'constructor ',
    'state if': ['if ()', Key('left')],
    'state else': ' else',
    'state else if': [' else if ()', Key('left')],
    'state while': ['while ()', Key('left')],
    'state for': ['for ()', Key('left')],
    'state switch': ['switch ()', Key('left')],
    'state case': ['case \nbreak;', Key('up')],
    'state goto': 'goto ',
    'state important': 'import ',
    'state class': 'class ',
    'state extends': 'extends ',
    'state super': 'super',

    'comment js': '// ',
    'word no': 'null',
    'arrow': ' => ',
    'assign': ' = ',
    'asink': 'async ',
    'oh wait': ' await ',

    'op (minus | subtract)': ' - ',
    'op (plus | add)': ' + ',
    'op (times | multiply)': ' * ',
    'op divide': ' / ',
    'op mod': ' % ',
    '[op] (minus | subtract) equals': ' -= ',
    '[op] (plus | add) equals': ' += ',
    '[op] (times | multiply) equals': ' *= ',
    '[op] divide equals': ' /= ',
    '[op] mod equals': ' %= ',

    '(op | is) greater [than]': ' > ',
    '(op | is) less [than]': ' < ',
    '(op | is) equal': ' === ',
    '(op | is) not equal': ' !== ',
    '(op | is) greater [than] or equal': ' >= ',
    '(op | is) less [than] or equal': ' <= ',
    '(op (power | exponent) | to the power [of])': ' ** ',
    'op and': ' && ',
    'op or': ' || ',
})
