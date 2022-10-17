from pico2d import *

open_canvas()

bg_jungle = load_image('background_jungle.png')
character = load_image('char1.png')
enemy = load_image('enemy1_1.png')

x = 0
frame = 0
while (x<800):
    clear_canvas()
    bg_jungle.draw(400,300)
    character.draw(200,300)
    enemy.clip_draw(frame*100,0,103,120,600,300)
    x+=5
    update_canvas()
    frame = (frame + 1) % 5
    delay(0.05)
    get_events()

close_canvas()