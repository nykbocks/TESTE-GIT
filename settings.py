import pygame

pygame.display.set_caption("JOGO MELHOR  QUE SUPER CHICKEN JUMPER") 
screen = pygame.display.set_mode((800, 600))
x=0
y=0
xx=x+30
yy=y+30
rotate = 0
img = pygame.image.load("image2.png")
img_w=img.get_width()
img_h=img.get_height()
ima = pygame.transform.scale(img, (img_w/4, img_h/4))
pos = [0,0]
walk_x = [False,False]
walk_y = [False,False]
def rotate_and_blit(image, angle, x, y):
    image_rotated = pygame.transform.rotate(image, angle)
    return screen.blit(image_rotated, (x, y))
                                     
    