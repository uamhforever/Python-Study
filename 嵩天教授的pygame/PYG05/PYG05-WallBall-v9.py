import pygame, sys

pygame.init()
icon = pygame.image.load("PYG03-flower.png")
pygame.display.set_icon(icon)
vInfo = pygame.display.Info()
size = width, height = 640, 480
speed = [1, 1]
BLACK = 0, 0, 0
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
# screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
# screen = pygame.display.set_mode(size, pygame.NOFRAME)
# print(pygame.display.Info())

pygame.display.set_caption("Pygame壁球游戏之旅")
ball = pygame.image.load("PYG02-ball.gif")
ball_rect = ball.get_rect()
fps = 300
fclock = pygame.time.Clock()
still = False
bgColor = pygame.Color("black")

def RGBChannel(a):
    return 0 if a<0 else (255 if a>255 else int(a))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1) * int(speed[0] / abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                still = True
        elif event.type == pygame.MOUSEBUTTONUP:
            still = False
            if event.button == 1:
                ball_rect = ball_rect.move(event.pos[0] - ball_rect.left, event.pos[1] - ball_rect.top)
    if  pygame.display.get_active() and not still:
        ball_rect = ball_rect.move(speed[0], speed[1])
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = - speed[0]
        if ball_rect.right > width and speed[0] > 0:
            speed[0] = - speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = - speed[1]
        if ball_rect.bottom > height and speed[1] > 0:
            speed[1] = - speed[1]

    bgColor.r = RGBChannel(ball_rect.left/width*255)
    bgColor.g = RGBChannel(ball_rect.top / height * 255)
    bgColor.b = RGBChannel(min(speed[0], speed[1]) / max(speed[0], speed[1], 1) * 255)
    screen.fill(bgColor)
    screen.blit(ball, ball_rect)
    pygame.display.update()
    fclock.tick(fps)