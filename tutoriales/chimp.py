import os
import sys
from chimp import Chimp, Fist
import pygame
from pygame.locals import *
from utils import *

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')

pygame.init()

screen = pygame.display.set_mode((468, 60))
pygame.display.set_caption('Monkey Fever')
pygame.mouse.set_visible(0)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

if pygame.font:
    font = pygame.font.Font(None, 36)
    text = font.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10))
    textpos = text.get_rect(centerx=background.get_width()/2)
    background.blit(text, textpos)

screen.blit(background, (0, 0))
pygame.display.flip()

whiff_sound = load_sound('./data/chimp/whiff.wav')
punch_sound = load_sound('./data/chimp/punch.wav')

chimp = Chimp('./data/chimp/chimp.bmp')
fist = Fist('./data/chimp/fist.bmp')
allsprites = pygame.sprite.RenderPlain((fist, chimp))
clock = pygame.time.Clock()

going = True
while going:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            going = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            going = False
        elif event.type == MOUSEBUTTONDOWN:
            if fist.punch(chimp):
                punch_sound.play()  # punch
                chimp.punched()
            else:
                whiff_sound.play()  # miss
        elif event.type == MOUSEBUTTONUP:
            fist.unpunch()

    allsprites.update()
    screen.blit(background, (0, 0))
    allsprites.draw(screen)
    pygame.display.flip()

pygame.quit()
