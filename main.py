import pygame, sys
from settings import *
import pygame.gfxdraw
pygame.init()
e = True

while e:
    print(screen)
    if x < 400 and y < 300:
        x+=0.1
        y+=0.1

    screen.fill((255, 255, 255))
    pygame.gfxdraw.box(screen,(x,y,xx,yy), (0,0,255))   
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                walk_x[1] = True
            elif event.key == pygame.K_a:
                walk_x[0] = True
            elif event.key == pygame.K_s:
                walk_y[0] = True
            elif event.key == pygame.K_w:
                walk_y[1] = True
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                       #x+
                walk_x[1] = False
            elif event.key == pygame.K_a:
                       #x-
                walk_x[0] = False
            elif event.key == pygame.K_s:
                      #y-
                walk_y[0] = False
            elif event.key == pygame.K_w:
                      #y+                
                walk_y[1] = False
        if walk_x[0] == True:
            pos[0]-=5
            rotate = "left"
        if walk_x[1] == True:
            pos[0]+=5
            rotate = "right"
        if walk_y[0] == True:
            pos[1]+=5
            rotate = "down"
        if walk_y[1] == True:
            pos[1]-=5
            rotate = "up"
    if rotate == "up":    
        rotate_and_blit(ima, 0, pos[0], pos[1])
    elif rotate == "down":    
        rotate_and_blit(ima, 180, pos[0], pos[1])
    elif rotate == "left":    
        rotate_and_blit(ima, 90, pos[0], pos[1])
    elif rotate == "right":    
        rotate_and_blit(ima, -90, pos[0], pos[1])
    if rotate == 0:
        rotate_and_blit(ima, 0, pos[0], pos[1])
    pygame.display.update()