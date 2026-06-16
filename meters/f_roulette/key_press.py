import random
messages = ["F*ck You!", "F*ck Them!", "F*ck Me!", "F*ck This!", "F*ck Everything!", "F*ck Sake!", "F*ck That!", "F*ck It!"]
current = 0

# Getting all our dimensions together
centre_x = screen.width * 0.5
centre_y = screen.height * 0.42

def update():
    global current  

    screen.pen = color.white
    screen.clear()

    if badge.pressed(BUTTON_UP) or badge.pressed(BUTTON_DOWN):
        current = random.randrange(0, 8)
        screen.clear()

    message = messages[current]
    bounds = rect(10, 30, 140, 110)
    
    screen.font = rom_font.ignore
    screen.pen = color.black

    text.draw(screen, message, bounds)
    

run(update)