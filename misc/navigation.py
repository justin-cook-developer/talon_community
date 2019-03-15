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
}

ctx.keymap(keymap)

