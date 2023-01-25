# -------------- constante --------------
import pygame
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

x, y = 200, 200
pas = 10
# --------------- script --------------
pygame.init()
dis = pygame.display.set_mode((1200, 600))

pygame.display.set_caption('Reinforcement learning for network buffer')
pygame.display.update()

game_over = False
i = 0
while not game_over:
    for event in pygame.event.get():
        print(event)  # prints out all the actions that take place on the screen
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                game_over = True
            if event.key == pygame.K_z:
                y -= pas
            if event.key == pygame.K_q:
                x -= pas
            if event.key == pygame.K_s:
                y += pas
            if event.key == pygame.K_d:
                x += pas
        # x_init, y_init, weight, height
        dis.fill(black)
        pygame.draw.rect(dis, blue, [x, y, 10, 10])
        pygame.display.update()
        i += 1
        print(i)
pygame.quit()
quit()
