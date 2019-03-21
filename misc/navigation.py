from talon.voice import Context, Key

ctx = Context("navigation")

keymap = {
    # Requires activation of System Preferences -> Shortcuts -> Input Sources
    # -> "Select the previous input source"
    "change language": Key("ctrl-space"),
    # moving
    "tarsh": Key("shift-tab"),
    # scrolling
    "scroll down": [Key("down")] * 30,
    "scroll up": [Key("up")] * 30,
    # NB home and end do not work in all apps
    "(scroll way down | doomway)": Key("cmd-down"),
    "(scroll way up | jeepway)": Key("cmd-up"),
    # from std.py
    "new window": Key("cmd-n"),
    "next window": Key("cmd-`"),
    "last window": Key("cmd-shift-`"),
    "next app": Key("cmd-tab"),
    "last app": Key("cmd-shift-tab"),
    "next tab": Key("cmd-shift-]"),
    "new tab": Key("cmd-t"),
    "(last | prevous | preev) tab": Key("cmd-shift-["),
    "next space": Key("cmd-alt-ctrl-right"),
    "last space": Key("cmd-alt-ctrl-left"),
    "(marco | search)": Key("cmd-f"),
}

ctx.keymap(keymap)

