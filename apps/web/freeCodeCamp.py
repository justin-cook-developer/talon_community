from talon.voice import Context, Key, press

ctx = Context(
  "freecodecamp",
  func=lambda app, win: "freeCodeCamp" in win.title,
)


# to find title: print(ui.active_window().title)

ctx.keymap({
  'next exercise' : Key("tab tab enter"),
})


