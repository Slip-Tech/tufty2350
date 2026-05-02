messages = ["Many Fucks", "Some Fucks", "No Fucks!!"]
colours = ["lime", "yellow", "red"]
current = 0

def update():
    global current  

    if badge.pressed(BUTTON_UP):
        current = (current - 1) #% len(messages)

    if badge.pressed(BUTTON_DOWN):
        current = (current + 1) #% len(messages)
    
    if current <= 0:
        current = 0

    if current > 2:
        current = 2  

    elif current == 1:
        screen.pen = color.rgb(212, 206, 44)
        screen.clear()

    elif current == 2:
        screen.pen = color.red
        screen.clear()

    else:
        screen.pen = color.lime
        screen.clear()

    screen.font = rom_font.bacteria
    screen.pen = color.white

    bounds = rect(20, 47, 175, 90)
    message = messages[current]
    text.draw(screen, message, bounds)

run(update)