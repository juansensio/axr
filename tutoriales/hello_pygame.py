import sys, pygame, os
pygame.init()

size = width, height = 500, 500
#speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

main_dir = os.path.split(os.path.abspath(__file__))[0]

file = os.path.join(main_dir, "data", 'intro_ball.png')

ball = pygame.image.load(file)#.convert()
#ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # ballrect = ballrect.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

    screen.fill(black)
    ball = pygame.draw.circle(screen, white, (30, 30), 10) 
    pygame.display.flip()