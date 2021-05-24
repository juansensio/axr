import pygame

pygame.init() #Inicializar Pygame
screen = pygame.display.set_mode((600, 800)) #Definir la ventana (x,y)
clock = pygame.time.Clock() #Definir clock interno

#Variables
FPS = 30 #Frames Por Segundo
running = 1 
x = 0
y = 0

while running == 1: #Bucle de Juego
    #Imprimir en pantalla
    screen.fill((0,0,0)) #Lenar la pantalla con un color
    cabeza = pygame.draw.rect(screen, (255,255,255),[x,y,24,24])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            if event.key == pygame.K_RIGHT:
                x += 10
            if event.key == pygame.K_UP:
                y -= 10
            if event.key == pygame.K_DOWN:
                y += 10
    clock.tick(FPS) #Actualizar actos en funcion de los FPS
    pygame.display.update() #Actualizar Pantalla

pygame.quit()
quit()