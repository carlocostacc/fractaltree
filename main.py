import pygame as pg
import settings
from pointer import Pointer
from fractaltree import FractalTree
from railslider import Rail


pg.init()
# clock
clock = pg.time.Clock()


def screen_info_and_setfsrcreen():
    fullscreen_sz = pg.display.Info().current_w, pg.display.Info().current_h
    print('screen size =', fullscreen_sz)
    #if pg.display.Info().current_w != settings.width or pg.display.Info().current_h != settings.height:
    #    settings.screensize = (pg.display.Info().current_w - 100, pg.display.Info().current_h - 100)


screen_info_and_setfsrcreen()

screen = pg.display.set_mode(settings.screensize, pg.RESIZABLE)
# drawline for branches

offset_x = 0
offset_y = 0
dragging = False
def mousetraking(point):
    global offset_x
    global offset_y
    if event.type == pg.MOUSEBUTTONDOWN:

        if event.button == 1:
            if point.collidepoint(*pg.mouse.get_pos()):
                point.dragging = True
                (Xmouse, Ymouse) = pg.mouse.get_pos()
                offset_x = point.posx - Xmouse
                offset_y = point.posy - Ymouse
                point.update(point.posx, point.posy)

    elif event.type == pg.MOUSEBUTTONUP:
        if event.button == 1:
            point.dragging = False

    elif event.type == pg.MOUSEMOTION:
        if point.dragging:
            mouse_x, mouse_y = event.pos
            point.update(mouse_x + offset_x, mouse_y + offset_y)

    if point.dragging == False or event.type == pg.MOUSEBUTTONUP:
        point.update(point.posx, point.posy)


# main loop
rail = Rail(20, 20, screen)
pointer = Pointer(rail.posx + settings.railwidth/2 - settings.pointerwidth/2, rail.posy - settings.pointerheight/2 + rail.height/2,screen)
pointer.settravel(settings.railwidth)
rail1 = Rail(20, 45, screen)
pointer1 =Pointer(rail1.posx + settings.railwidth/2 - settings.pointerwidth/2, rail1.posy - settings.pointerheight/2 + rail1.height/2, screen)
pointer1.settravel(settings.railwidth)
tree = FractalTree(screen, pointer.getangle(), pointer1.getvalue())
dragging = False
displaying = True
while displaying:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            displaying = False
    screen.fill(settings.white)
    rail.update()
    rail1.update()
    mousetraking(pointer)
    mousetraking(pointer1)
    tree.update(pointer.getangle(), pointer1.getcolor())
    pg.display.flip()
    clock.tick(60)


pg.quit()