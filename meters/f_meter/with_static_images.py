messages = ["No F*cks!!", "Some F*cks", "Many F*cks"]
current = 2
sprite_middle = image.load("/system/assets/middle.png")
sprite_down = image.load("/system/assets/down.png")
sprite_up = image.load("/system/assets/up.png")


def update():
    global current  

    if badge.pressed(BUTTON_UP) and current < 2:
        current += 1

    if badge.pressed(BUTTON_DOWN) and current > 0:
        current -= 1

    elif current == 1:
        screen.pen = color.rgb(212, 206, 44)
        screen.clear()
        screen.blit(sprite_down, vec2(70, 80))

    elif current == 2:
        screen.pen = color.lime
        screen.clear()
        screen.blit(sprite_up, vec2(70, 80))
    else:
        screen.pen = color.red
        screen.clear()
        screen.blit(sprite_middle, vec2(70, 80))

    screen.font = rom_font.bacteria
    screen.pen = color.white

    bounds = rect(20, 47, 175, 90)
    message = messages[current]
    text.draw(screen, message, bounds)

run(update)