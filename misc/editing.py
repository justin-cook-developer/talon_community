from talon.voice import Context, Key

ctx = Context("editing")

keymap = {"copy": Key("cmd-c"), "paste": Key("cmd-v"),  "sage": Key("cmd-s"), "dizzle": Key("cmd-z"), "rizzle": Key("cmd-shift-z")}

ctx.keymap(keymap)
