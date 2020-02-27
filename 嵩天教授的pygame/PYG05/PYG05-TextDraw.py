import  pygame, sys
import pygame.freetype

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pygame文字绘制")
GOLD = 255, 255, 0

f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttf", 36)
f1Rect = f1.render_to(screen, (200,160)
                      , "世界和平", fgcolor=GOLD, size=50)
f2Surf, f2Rect = f1.render("新的文字", fgcolor=GOLD, size=20)

while True:
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            sys.exit()
    screen.blit(f2Surf, (20,5))
    pygame.display.update()
