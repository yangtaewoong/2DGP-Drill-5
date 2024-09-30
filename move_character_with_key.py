from pico2d import *
#  높이 159 * i

open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('run_animation.png')


def handle_events():
    global running,dirx,diry

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1

running = True
x = 800 // 2
y = 100
frame = 0
dirx = 0
diry = 0

def draw_character():
    global dirx,diry
    if dirx > 0:
        character.clip_draw(frame * 95, 159, 95, 159, x, y,50,100)
    elif dirx < 0:
        character.clip_draw(frame * 95, 159*2, 95, 159, x, y,50,100)
    elif diry > 0:
        character.clip_draw(frame * 95, 0, 95, 159, x, y,50,100)
    elif diry < 0:
        character.clip_draw(frame * 95, 159*3, 95, 159, x, y,50,100)
    else:
        character.clip_draw(frame * 95, 159 * 3, 95, 159, x, y,50,100)

while running:
    clear_canvas()
    ground.draw(400, 100)
    draw_character()
    update_canvas()
    handle_events()
    frame = (frame + 1) % 12
    x = max(25, min(800 - 25, x + dirx * 5))
    y = max(50, min(600 - 50, y + diry * 5))
    delay(0.05)

close_canvas()

