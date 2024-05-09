import pygame
import sys
import time
from pygame import gfxdraw
pygame.init()
screen = pygame.display.set_mode((640, 320))
pygame.display.toggle_fullscreen()
clock = pygame.time.Clock()
running = True
color = (0,255,0)
my_font = pygame.font.SysFont('Perfect DOS VGA 437 Win', 10)
def draw_pixel(screen,x,y,c):
    pygame.gfxdraw.pixel(screen,x,y,c)
cursorpos = 10
cursorrow = 10
inputstr = ""
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                cursorrow = cursorrow + 10
                cursorpos = 10
                text_surface = my_font.render('>', False, color)
                screen.blit(text_surface, (0,cursorrow))
                if inputstr == "test":
                    text_surface = my_font.render('test command', False, color)
                    cursorrow = cursorrow+ 10
                    screen.blit(text_surface, (cursorpos,cursorrow))
                    cursorrow = cursorrow+ 10
                    text_surface = my_font.render('>', False, color)
                    screen.blit(text_surface, (0,cursorrow))
                elif inputstr == "exit":
                     running = False
                elif inputstr == "mksub":
                    text_surface = my_font.render('creating submenu', False, color)
                    cursorrow = cursorrow+ 10
                    screen.blit(text_surface, (cursorpos,cursorrow))
                    cursorrow = cursorrow+ 10
                    text_surface = my_font.render('>', False, color)
                    screen.blit(text_surface, (0,cursorrow))
                elif inputstr == "cls":
                    text_surface = my_font.render('robco terminal', False, color)
                    cursorrow = cursorrow+ 10
                    screen.blit(text_surface, (cursorpos,cursorrow))
                    cursorrow = cursorrow+ 10
                    text_surface = my_font.render('>', False, color)
                    screen.blit(text_surface, (0,cursorrow))
                elif inputstr.startswith("run"):
                    print("running program")
                inputstr = ""
            elif event.key == pygame.K_SPACE:
                cursorpos = cursorpos + 10
                inputstr = inputstr + " "

            else:
                text_surface = my_font.render(pygame.key.name(event.key), False, color)
                screen.blit(text_surface, (cursorpos,cursorrow))
                cursorpos = cursorpos + 10
                inputstr = inputstr + pygame.key.name(event.key)
                
    text_surface = my_font.render('robco terminal', False, color)
    screen.blit(text_surface, (0,0))
    text_surface = my_font.render('>', False, color)
    screen.blit(text_surface, (0,10))


    # crt cal
    draw_pixel(screen,0,0,color)
    draw_pixel(screen,254,0,color)
    draw_pixel(screen,0,127,color)
    draw_pixel(screen,254,127,color)
    # crt cal
    pygame.display.flip()#push to robco color graphics adapter card's buffer
    clock.tick(15)#vertical sinc signal

pygame.quit()
