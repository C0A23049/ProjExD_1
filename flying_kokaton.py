import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)#KK左右反転
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    tmr = 0
    key_x = 0
    key_y = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200
        key_x = 0
        key_y = 0
        screen.blit(bg_img, [-x, 0]) # sucreen ssufaceに背景画像
        screen.blit(bg_img_2, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bg_img_2, [-x+4800, 0])
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]: 
            key_y -= 1
        if key_lst[pg.K_DOWN]: 
            key_y += 1
        if key_lst[pg.K_LEFT]: 
            key_x -= 1
        if key_lst[pg.K_RIGHT]: 
            key_x += 1
        if not key_lst[pg.K_RIGHT]: 
            key_x -= 1
        kk_rct.move_ip((key_x, key_y))
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()