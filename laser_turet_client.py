import pygame, os

WIDTH = 900
HEIGHT = 800

pygame.init()
dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.update()
pygame.display.set_caption('mouse_cords')

game_over=False
while not game_over:
    mouseX, mouseY = pygame.mouse.get_pos()
    pygame.draw.line(dis , (255, 0, 0), (0, mouseY), (WIDTH, mouseY))
    pygame.draw.line(dis ,(0, 255, 0), (mouseX, 0), (mouseX, HEIGHT))
    pygame.display.update()
    dis.fill((0, 0, 0))
    print(mouseX, mouseY)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
pygame.quit()
quit()