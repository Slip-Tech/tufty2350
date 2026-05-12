messages = ["No F*cks!!", "Some F*cks", "Many F*cks"]
colours = ["red", "yellow", "lime"]
current = 2

def update():
    global current  

    if badge.pressed(BUTTON_UP) and current < 2:
        current += 1

    if badge.pressed(BUTTON_DOWN) and current > 0:
        current -= 1

    elif current == 1:
        screen.pen = color.rgb(212, 206, 44)
        screen.clear()

    elif current == 2:
        screen.pen = color.lime
        screen.clear()

    else:
        screen.pen = color.red
        screen.clear()

    screen.font = rom_font.bacteria
    screen.pen = color.white

    bounds = rect(20, 47, 175, 90)
    message = messages[current]
    text.draw(screen, message, bounds)

run(update)