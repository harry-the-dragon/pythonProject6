import pygame
import sys
import time
pygame.init()



bg_color = (200, 200, 160)
line_color = (23, 145, 135)
circle_color = (29, 121, 200)
cross_color = (255, 0, 0)
font1 = pygame.font.SysFont('comicsans',30,True)
font2 = pygame.font.SysFont('comicsans',20,True)

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Timer")
win.fill(bg_color)
clock = pygame.time.Clock()


def draw_time_frame ():
    pygame.draw.rect(win, cross_color, pygame.Rect(150,250,200,150))
    text = font1.render('Press space to start timing', True, circle_color)
    win.blit(text,(50,100))
    pygame.display.flip()
#
#def local_time():
    # seconds = time.time()
    # local_time = time.ctime(seconds)
    # timetext = font2.render(str(local_time), True, cross_color )
    # win.blit(timetext, (10,10))
    # pygame.display.update()

# def stopwatch():
#     starttime = time.time()
#     lasttime = starttime
#     lapnum = 1

#     while 



draw_time_frame()
#local_time()


while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif keys[pygame.K_ESCAPE]:
            sys.exit()

        clock.tick(30)
        theTime = time.strftime("%D:%H:%M:%S", time.localtime())
        timeText = font2.render(str(theTime), True, (255, 255, 255), (0, 0, 0))
        win.blit(timeText, (10, 10))

        pygame.display.update()
