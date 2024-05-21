import math
import os
import random
import sys
import time
import pygame as pg
from pygame.sprite import Group

WIDTH, HEIGHT = 1200, 900

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def calc_orientation(org: pg.Rect, dst: pg.Rect) -> tuple[float, float]:
    """
    オブジェクト同士のベクトル計算メソッド
    引数: org: pg.Rect, dst: pg.Rect (orgからみたdstのベクトルを計算)
    戻り値: orgからみたdstのx方向の距離, orgからみたdstのy方向の距離
    """
    x_diff, y_diff = dst.centerx - org.centerx, dst.centery - org.centery
    norm = math.sqrt(x_diff ** 2 + y_diff ** 2)
    return x_diff / norm, y_diff / norm
  
def main():
    """
    main関数
    """
    tmr = 0
    clock = pg.time.Clock()
    pg.display.set_caption("roguelike")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    img = pg.image.load(f"fig/Sogen.png")

    # Initialize the mixer and load the background music
    pg.mixer.init()
    pg.mixer.music.load(f"fig/maou_bgm_fantasy08.mp3")  # Ensure you have the correct path to your music file
    pg.mixer.music.play(-1)  # Play the music on a loop

    while True:
        key_lst = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
        screen.blit(img, [0, 0])

        pg.display.update()
        tmr += 1
        clock.tick(50)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
