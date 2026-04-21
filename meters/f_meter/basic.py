messages = ["Many F*cks", "Some F*cks", "No F*cks!!"]
colours = ["lime", "yellow", "red"]
current = 0

def update():
    global current

    if badge.pressed(BUTTON_UP):
        current = (current - 1) % len(messages)

    if badge.pressed(BUTTON_DOWN):
        current = (current + 1) % len(messages)
  
    if current == 1:
        screen.pen = color.rgb(212, 206, 44)
        screen.clear()
    elif current == 2:
        screen.pen = color.red
        screen.clear()
    else:
        screen.pen = color.lime
        screen.clear()

    screen.pen = color.white
    screen.font = rom_font.smart

    text = messages[current]
    width, _ = screen.measure_text(text)
    x = (screen.width / 2) - (width / 2)

    screen.text(text, x, 45)

run(update)
