import numpy as np

# -------------- constante --------------
import pygame
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

x, y = 200, 200
pas = 10

# -------------- fonction --------------


def createPts():
    pts = {}
    for i in [-1, 1]:
        for j in [-1, 1]:
            for k in [-1, 1]:
                pts["{}_{}_{}".format(i, j, k)] = np.array([i, j, k])
    return pts


def calculAngle(tx, ty, tz, vector):
    cx, sx = np.cos(tx), np.sin(tx)
    cy, sy = np.cos(ty), np.sin(ty)
    cz, sz = np.cos(tz), np.sin(tz)
    mx = np.array([[1, 0, 0],
                   [0, cx, -sx],
                   [0, sx, cx]])
    my = np.array([[cy, 0, sy],
                   [0, 1, 0],
                   [-sy, 0, cy]])
    mz = np.array([[cz, -sz, 0],
                   [sz, cz, 0],
                   [0, 0, 1]])
    return (np.dot(np.dot(mx, np.dot(my, mz)), vector))


# --------------- script --------------
pts = createPts()

for i in pts:
    print(pts[i])
raise ValueError()

pygame.init()
dis = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Cube 3D')
pygame.display.update()

i = 0
game_over = False
while not game_over:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                game_over = True
        """
            if event.key == pygame.K_z:
                y -= pas
            if event.key == pygame.K_q:
                x -= pas
            if event.key == pygame.K_s:
                y += pas
            if event.key == pygame.K_d:
                x += pas
        """
        dis.fill(black)
        for j in pts:
            pygame.draw.circle(dis, red, pts[0], 10)
        # x_init, y_init, weight, height
        pygame.draw.rect(dis, blue, [x, y, 10, 10])
        pygame.display.update()
        i += 1
        print(i)
pygame.quit()
quit()
