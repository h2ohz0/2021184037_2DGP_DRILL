from pico2d import*
import math

open_canvas()

character = load_image('character.png')

a=0
while(a==0):
    clear_canvas_now()
    character.draw_now(x,y)
    delay(0.01)
