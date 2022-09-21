from pico2d import*

open_canvas()

character = load_image('character.png')

a=0
while(a==0):
    x = 0
    while(x<800):
        clear_canvas_now()
        character.draw_now(x,90)
        x = x+2
        delay(0.01)
    y=0
    while(y<600):
        clear_canvas_now()
        character.draw_now(800,y)
        y = y+2
        delay(0.01)
    x = 800
    while(x>0):
        clear_canvas_now()
        character.draw_now(x,600)
        x = x-2
        delay(0.01)
    y = 600
    while(y>0):
        clear_canvas_now()
        character.draw_now(0,y)
        y=y-2
        delay(0.01)

