from talon.voice import Context, Key

ctx = Context("navigation")

keymap = {
    # Requires activation of System Preferences -> Shortcuts -> Input Sources
    # -> "Select the previous input source"
    "change language": Key("ctrl-space"),
    # Application navigation
    "swick": Key("cmd-tab"),
    "new window": Key("cmd-n"),
    "(next window | gibby)": Key("cmd-`"),
    "(last window | shibby)": Key("cmd-shift-`"),
"next space": Key("cmd-alt-ctrl-right"),
    "last space": Key("cmd-alt-ctrl-left"),
    # deleting
    # '(delete line)': Key('cmd-right cmd-backspace'),
    "steffi": Key("alt-ctrl-backspace"),
    "stippy": Key("alt-ctrl-delete"),
    "carmex": Key("alt-backspace"),
    "kite": Key("alt-delete"),
    "snipple": Key("cmd-shift-left delete"),
    "(delete this line | snipper)": Key("cmd-shift-right delete"),
    "slurp": Key("backspace delete"),
    "(delete this word | slurpies)": Key("alt-backspace alt-delete"),
    # moving
    "tarp": Key("tab"),
    "tarsh": Key("shift-tab"),
    "shocker": [Key("cmd-left enter up")],
    "wonkrim": Key("alt-ctrl-left"),
    "wonkrish": Key("alt-ctrl-right"),
    "fame": Key("alt-left"),
    "fish": Key("alt-right"),
    "ricky": Key("cmd-right"),
    "lefty": Key("cmd-left"),
    "crimp": Key("left"),
    "chris": Key("right"),
    "jeep": Key("up"),
    "(down | dune | doom)": Key("down"),
    # scrolling
    "scroll down": [Key("down")] * 30,
    "scroll up": [Key("up")] * 30,
    # NB home and end do not work in all apps
    "(scroll way down | doomway)": Key("cmd-down"),
    "(scroll way up | jeepway)": Key("cmd-up"),
    "page up": [Key("pageup")],
    "page down": [Key("pagedown")],
    # searching
    "(search | marco)": Key("cmd-f"),
    "marneck": Key("cmd-g"),
    "marpreev": Key("cmd-shift-g"),
    "marthis": [Key("alt-right"), Key("shift-alt-left"), Key("cmd-f"), Key("enter")],
}

ctx.keymap(keymap)
